# # # # # extract.py
# # # # from flask import Blueprint, request, jsonify
# # # # from app.utils.openrouter_client import call_openrouter
# # # # from app.utils.memory import merge_memory, save_memory
# # # # import json
# # # # import re

# # # # extract_bp = Blueprint('extract', __name__)

# # # # @extract_bp.route('/extract', methods=['POST'])
# # # # def extract():
# # # #     user_input = request.json.get('message', '')
# # # #     existing_memory = request.json.get('memory', {})
# # # #     user_id = request.json.get('user_id', None)

# # # #     if not user_input:
# # # #         print("❌ No 'message' found in request body")
# # # #         return jsonify({"error": "Missing 'message' in request body"}), 400

# # # #     if not user_id:
# # # #         print("❌ No 'user_id' provided")
# # # #         return jsonify({"error": "Missing 'user_id' in request"}), 400

# # # #     print("===== [/extract ROUTE HIT] =====")
# # # #     print(f"💬 User message: {user_input}")
# # # #     print("📂 Existing memory (before merge):")
# # # #     print(json.dumps(existing_memory, indent=2))

# # # #     prompt = f"""
# # # # You are extracting personal facts **about the user** from their message.

# # # # Your job:
# # # # - Convert useful facts into a dynamic, flat JSON object.
# # # # - The keys should be auto-generated based on the content. For example:
# # # #   - "I’m moving to Bangalore next week" → {{"city": "Bangalore"}}
# # # #   - "It’s my 23rd birthday today!" → {{"age": "23"}}
# # # #   - "I'm jobless again lol" → {{"job_status": "unemployed"}}
# # # # - You may reuse or update previous facts if there's a new update (e.g., new age, new city, new job).
# # # # - DO NOT include any facts about the AI (Jino) itself.
# # # # - DO NOT add commentary or explanation. Just the JSON.
# # # # - Be smart about sarcasm and tone, but don’t make things up.

# # # # User message: "{user_input}"
# # # # """.strip()

# # # #     models = [
# # # #         "deepseek/deepseek-r1:free",
# # # #         "mistralai/mixtral-8x7b-instruct"
# # # #     ]

# # # #     updated_memory = None
# # # #     extracted_json = None
# # # #     final_result = None
# # # #     final_model = None
# # # #     memory_updated = False

# # # #     for model in models:
# # # #         try:
# # # #             print(f"⚙️ Trying model: {model}")
# # # #             result = call_openrouter(
# # # #                 model=model,
# # # #                 messages=[{"role": "user", "content": prompt}],
# # # #                 temperature=0,
# # # #                 max_tokens=300
# # # #             )

# # # #             raw_response = result.get("content", "").strip()
# # # #             print(f"📦 Raw model response: {raw_response}")

# # # #             cleaned = re.sub(r"```json|```", "", raw_response).strip()

# # # #             if not cleaned:
# # # #                 print("⚠️ Cleaned response is empty. Trying next model...")
# # # #                 continue

# # # #             extracted_json = json.loads(cleaned)

# # # #             if not extracted_json or not isinstance(extracted_json, dict) or extracted_json == {}:
# # # #                 print("⚠️ No valid JSON extracted. Trying next model...")
# # # #                 continue

# # # #             # Merge only if we got something useful
# # # #             updated_memory = merge_memory(existing_memory, extracted_json)
# # # #             memory_updated = updated_memory != existing_memory  # Check if anything changed
# # # #             final_result = result
# # # #             final_model = model

# # # #             if memory_updated:
# # # #                 save_memory(user_id, updated_memory)
# # # #                 print("✅ Memory updated and saved.")
# # # #             else:
# # # #                 print("ℹ️ No new info extracted. Keeping existing memory intact.")

# # # #             print("🧠 [Extracted from model]:")
# # # #             print(json.dumps(extracted_json, indent=2))
# # # #             print("🧠 [Updated JINO Memory]:")
# # # #             print(json.dumps(updated_memory, indent=2))
# # # #             break

# # # #         except json.JSONDecodeError as jde:
# # # #             print(f"❌ JSON decode failed for model {model}: {str(jde)}")
# # # #             continue
# # # #         except Exception as e:
# # # #             print(f"💥 Unexpected error for model {model}: {str(e)}")
# # # #             continue

# # # #     # Fallback: if everything failed, just use existing memory
# # # #     if updated_memory is None:
# # # #         print("🚫 All models failed. Returning existing memory as fallback.")
# # # #         updated_memory = existing_memory

# # # #     return jsonify({
# # # #         "extracted": updated_memory,
# # # #         "judgement": {},  # Still reserved for sarcasm later
# # # #         "tokens_used": final_result.get("tokens", {}) if final_result else {},
# # # #         "model_used": final_model if final_model else "none",
# # # #         "memory_updated": memory_updated  # ✅ this is new
# # # #     }), 200


# # # from flask import Blueprint, request, jsonify
# # # from app.utils.openrouter_client import call_openrouter
# # # from app.utils.memory import merge_memory, save_memory
# # # from datetime import datetime
# # # import json
# # # import re

# # # extract_bp = Blueprint('extract', __name__)

# # # @extract_bp.route('/extract', methods=['POST'])
# # # def extract():
# # #     user_input = request.json.get('message', '')
# # #     existing_memory = request.json.get('memory', {})
# # #     user_id = request.json.get('user_id', None)
# # #     chat_id = request.json.get('chat_id', 'chat_1')  # fallback if not given

# # #     if not user_input:
# # #         print("❌ No 'message' found in request body")
# # #         return jsonify({"error": "Missing 'message' in request body"}), 400

# # #     if not user_id:
# # #         print("❌ No 'user_id' provided")
# # #         return jsonify({"error": "Missing 'user_id' in request"}), 400

# # #     print("===== [/extract ROUTE HIT] =====")
# # #     print(f"💬 User message: {user_input}")
# # #     print("📂 Existing memory (before merge):")
# # #     print(json.dumps(existing_memory, indent=2))

# # #     prompt = f"""
# # # You are extracting personal facts **about the user** from their message.

# # # Your job:
# # # - Convert useful facts into a dynamic, flat JSON object.
# # # - The keys should be auto-generated based on the content. For example:
# # #   - "I’m moving to Bangalore next week" → {{"city": "Bangalore"}}
# # #   - "It’s my 23rd birthday today!" → {{"age": "23"}}
# # #   - "I'm jobless again lol" → {{"job_status": "unemployed"}}
# # # - You may reuse or update previous facts if there's a new update (e.g., new age, new city, new job).
# # # - DO NOT include any facts about the AI (Jino) itself.
# # # - DO NOT add commentary or explanation. Just the JSON.
# # # - Be smart about sarcasm and tone, but don’t make things up.

# # # Additionally, if you can judge the **user's emotional state or personality** based on this message, return a second JSON object called "judgement" like this:

# # # "judgement": {{
# # #   "judgement": "User seems very hopeful despite facing tough times.",
# # #   "category": "emotional_state",
# # #   "confidence": "medium"
# # # }}

# # # Only include "judgement" if it's meaningful or emotionally insightful.

# # # User message: "{user_input}"
# # # """.strip()

# # #     models = [
# # #         "deepseek/deepseek-r1:free",
# # #         "mistralai/mixtral-8x7b-instruct"
# # #     ]

# # #     updated_memory = None
# # #     extracted_json = None
# # #     final_result = None
# # #     final_model = None
# # #     memory_updated = False
# # #     judgement_entry = {}

# # #     for model in models:
# # #         try:
# # #             print(f"⚙️ Trying model: {model}")
# # #             result = call_openrouter(
# # #                 model=model,
# # #                 messages=[{"role": "user", "content": prompt}],
# # #                 temperature=0,
# # #                 max_tokens=400
# # #             )

# # #             raw_response = result.get("content", "").strip()
# # #             print(f"📦 Raw model response: {raw_response}")

# # #             cleaned = re.sub(r"```json|```", "", raw_response).strip()
# # #             if not cleaned:
# # #                 print("⚠️ Cleaned response is empty. Trying next model...")
# # #                 continue

# # #             parsed = json.loads(cleaned)

# # #             if not parsed or not isinstance(parsed, dict):
# # #                 print("⚠️ Response not a valid dict. Trying next model...")
# # #                 continue

# # #             # Separate memory and judgement if both exist
# # #             memory_data = {k: v for k, v in parsed.items() if k != "judgement"}
# # #             judgement_data = parsed.get("judgement", None)

# # #             if memory_data:
# # #                 updated_memory = merge_memory(existing_memory, memory_data)
# # #                 memory_updated = updated_memory != existing_memory
# # #                 if memory_updated:
# # #                     save_memory(user_id, updated_memory)
# # #                     print("✅ Memory updated and saved.")
# # #                 else:
# # #                     print("ℹ️ No new info extracted. Keeping existing memory intact.")
# # #                 print("🧠 [Extracted from model]:")
# # #                 print(json.dumps(memory_data, indent=2))
# # #                 print("🧠 [Updated JINO Memory]:")
# # #                 print(json.dumps(updated_memory, indent=2))

# # #             # Handle judgement memory
# # #             if judgement_data and isinstance(judgement_data, dict) and "judgement" in judgement_data:
# # #                 judgement_entry = {
# # #                     "timestamp": datetime.utcnow().isoformat(),
# # #                     "category": judgement_data.get("category", "emotional_state"),
# # #                     "judgement": judgement_data.get("judgement"),
# # #                     "confidence": judgement_data.get("confidence", "medium")
# # #                 }

# # #                 # Inject into updated_memory under jino_judgement
# # #                 updated_memory.setdefault("jino_judgement", {})
# # #                 updated_memory["jino_judgement"].setdefault(chat_id, [])
# # #                 updated_memory["jino_judgement"][chat_id].append(judgement_entry)
# # #                 save_memory(user_id, updated_memory)  # Save updated judgement too

# # #                 print("🧠 [JINO Judgement Added]:")
# # #                 print(json.dumps(judgement_entry, indent=2))
# # #             else:
# # #                 print("🫥 No judgement returned or it's empty.")

# # #             final_result = result
# # #             final_model = model
# # #             break

# # #         except json.JSONDecodeError as jde:
# # #             print(f"❌ JSON decode failed for model {model}: {str(jde)}")
# # #             continue
# # #         except Exception as e:
# # #             print(f"💥 Unexpected error for model {model}: {str(e)}")
# # #             continue

# # #     if updated_memory is None:
# # #         print("🚫 All models failed. Returning existing memory as fallback.")
# # #         updated_memory = existing_memory

# # #     return jsonify({
# # #         "extracted": updated_memory,
# # #         "judgement": judgement_entry,
# # #         "tokens_used": final_result.get("tokens", {}) if final_result else {},
# # #         "model_used": final_model if final_model else "none",
# # #         "memory_updated": memory_updated
# # #     }), 200

# # from flask import Blueprint, request, jsonify
# # from app.utils.openrouter_client import call_openrouter
# # from app.utils.memory import merge_memory, save_memory
# # from datetime import datetime
# # import json
# # import re

# # extract_bp = Blueprint('extract', __name__)

# # @extract_bp.route('/extract', methods=['POST'])
# # def extract():
# #     user_input = request.json.get('message', '')
# #     existing_memory = request.json.get('memory', {})
# #     user_id = request.json.get('user_id', None)
# #     chat_id = request.json.get('chat_id', 'chat_1')

# #     if not user_input:
# #         return jsonify({"error": "Missing 'message' in request body"}), 400

# #     if not user_id:
# #         return jsonify({"error": "Missing 'user_id' in request"}), 400

# #     print("===== [/extract ROUTE HIT] =====")
# #     print(f"💬 User message: {user_input}")

# #     prompt = f"""
# # You are extracting personal facts **about the user** from their message.

# # Return two separate JSON blocks:

# # 1. "jino_memory": factual memory only (like name, city, job, etc.)
# # 2. "jino_judgement": emotional memory (like moods, opinions, personality insight)

# # Format:
# # {{
# #   "jino_memory": {{
# #     "key1": "value1",
# #     ...
# #   }},
# #   "jino_judgement": {{
# #     "judgement": "User seems frustrated but optimistic.",
# #     "category": "emotional_state",
# #     "confidence": "high"
# #   }}
# # }}

# # DO NOT wrap with markdown or explanation. Just pure JSON.

# # User message: "{user_input}"
# # """.strip()

# #     models = [
# #         # "deepseek/deepseek-r1:free",
# #         "mistralai/mixtral-8x7b-instruct"
# #     ]

# #     final_model = None
# #     final_result = None
# #     memory_updated = False
# #     updated_memory = existing_memory
# #     judgement_entry = {}

# #     for model in models:
# #         try:
# #             print(f"⚙️ Trying model: {model}")
# #             result = call_openrouter(
# #                 model=model,
# #                 messages=[{"role": "user", "content": prompt}],
# #                 temperature=0.3,
# #                 max_tokens=400
# #             )

# #             raw_response = result.get("content", "").strip()
# #             print(f"📦 Raw model response:\n{raw_response}")

# #             cleaned = re.sub(r"```json|```", "", raw_response).strip()
# #             parsed = json.loads(cleaned)

# #             if not isinstance(parsed, dict):
# #                 print("⚠️ Model returned non-dict JSON. Skipping.")
# #                 continue

# #             memory_data = parsed.get("jino_memory", {})
# #             judgement_data = parsed.get("jino_judgement", {})

# #             # ----- Save factual memory -----
# #             if isinstance(memory_data, dict) and memory_data:
# #                 updated_memory = merge_memory(existing_memory, memory_data)
# #                 memory_updated = updated_memory != existing_memory
# #                 if memory_updated:
# #                     save_memory(user_id, updated_memory)
# #                     print("✅ jino_memory updated and saved.")
# #                 else:
# #                     print("ℹ️ No new factual memory changes.")
# #             else:
# #                 print("🫥 No valid jino_memory returned.")

# #             # ----- Save judgement memory -----
# #             if isinstance(judgement_data, dict) and "judgement" in judgement_data:
# #                 judgement_entry = {
# #                     "timestamp": datetime.utcnow().isoformat(),
# #                     "category": judgement_data.get("category", "emotional_state"),
# #                     "judgement": judgement_data.get("judgement"),
# #                     "confidence": judgement_data.get("confidence", "medium")
# #                 }

# #                 updated_memory.setdefault("jino_judgement", {})
# #                 updated_memory["jino_judgement"].setdefault(chat_id, [])
# #                 updated_memory["jino_judgement"][chat_id].append(judgement_entry)
# #                 save_memory(user_id, updated_memory)

# #                 print("🧠 [JINO Judgement Added]:")
# #                 print(json.dumps(judgement_entry, indent=2))
# #             else:
# #                 print("🫥 No valid jino_judgement returned.")

# #             final_result = result
# #             final_model = model
# #             break

# #         except json.JSONDecodeError as jde:
# #             print(f"❌ JSON decode failed for {model}: {str(jde)}")
# #             continue
# #         except Exception as e:
# #             print(f"💥 Unexpected error from {model}: {str(e)}")
# #             continue

# #     return jsonify({
# #         "extracted": updated_memory,
# #         "judgement": judgement_entry,
# #         "tokens_used": final_result.get("tokens", {}) if final_result else {},
# #         "model_used": final_model or "none",
# #         "memory_updated": memory_updated
# #     }), 200




# from flask import Blueprint, request, jsonify
# from app.utils.openrouter_client import call_openrouter
# from app.utils.memory import merge_memory, save_memory
# from datetime import datetime
# import json
# import re

# extract_bp = Blueprint('extract', __name__)

# @extract_bp.route('/extract', methods=['POST'])
# def extract():
#     user_input = request.json.get('message', '')
#     existing_memory = request.json.get('memory', {})
#     user_id = request.json.get('user_id', None)
#     chat_id = request.json.get('chat_id', 'chat_1')

#     if not user_input:
#         return jsonify({"error": "Missing 'message' in request body"}), 400

#     if not user_id:
#         return jsonify({"error": "Missing 'user_id' in request"}), 400

#     print("===== [/extract ROUTE HIT] =====")
#     print(f"💬 User message: {user_input}")

#     prompt = f"""
# You are extracting personal facts **about the user** from their message.

# Return two separate JSON blocks:

# 1. "jino_memory": factual memory only (like name, city, job, etc.)
# 2. "jino_judgement": emotional memory (like moods, opinions, personality insight)

# Format:
# {{
#   "jino_memory": {{
#     "key1": "value1",
#     ...
#   }},
#   "jino_judgement": {{
#     "judgement": "User seems frustrated but optimistic.",
#     "category": "emotional_state",
#     "confidence": "high"
#   }}
# }}

# DO NOT wrap with markdown or explanation. Just pure JSON.

# User message: "{user_input}"
# """.strip()

#     models = [
#         "mistralai/mixtral-8x7b-instruct"
#     ]

#     final_model = None
#     final_result = None
#     memory_updated = False
#     updated_memory = existing_memory
#     judgement_entry = {}

#     for model in models:
#         try:
#             print(f"⚙️ Trying model: {model}")
#             result = call_openrouter(
#                 model=model,
#                 messages=[{"role": "user", "content": prompt}],
#                 temperature=0.3,
#                 max_tokens=400
#             )

#             raw_response = result.get("content", "").strip()
#             print(f"📦 Raw model response:\n{raw_response}")

#             # Fix common AI formatting issues
#             cleaned = raw_response.replace("\\_", "_")
#             cleaned = re.sub(r"```json|```", "", cleaned).strip()

#             try:
#                 parsed = json.loads(cleaned)
#             except json.JSONDecodeError as jde:
#                 print(f"❌ JSON decode failed after cleanup: {str(jde)}")
#                 print("🧽 Cleaned content that failed:\n", cleaned)
#                 continue

#             if not isinstance(parsed, dict):
#                 print("⚠️ Model returned non-dict JSON. Skipping.")
#                 continue

#             memory_data = parsed.get("jino_memory", {})
#             judgement_data = parsed.get("jino_judgement", {})

#             # ----- Save factual memory -----
#             if isinstance(memory_data, dict) and memory_data:
#                 updated_memory = merge_memory(existing_memory, memory_data)
#                 memory_updated = updated_memory != existing_memory
#                 if memory_updated:
#                     save_memory(user_id, updated_memory)
#                     print("✅ jino_memory updated and saved.")
#                 else:
#                     print("ℹ️ No new factual memory changes.")
#             else:
#                 print("🫥 No valid jino_memory returned.")

#             # ----- Save judgement memory -----
#             if isinstance(judgement_data, dict) and "judgement" in judgement_data:
#                 judgement_entry = {
#                     "timestamp": datetime.utcnow().isoformat(),
#                     "category": judgement_data.get("category", "emotional_state"),
#                     "judgement": judgement_data.get("judgement"),
#                     "confidence": judgement_data.get("confidence", "medium")
#                 }

#                 updated_memory.setdefault("jino_judgement", {})
#                 updated_memory["jino_judgement"].setdefault(chat_id, [])
#                 updated_memory["jino_judgement"][chat_id].append(judgement_entry)
#                 save_memory(user_id, updated_memory)

#                 print("🧠 [JINO Judgement Added]:")
#                 print(json.dumps(judgement_entry, indent=2))
#             else:
#                 print("🫥 No valid jino_judgement returned.")

#             final_result = result
#             final_model = model
#             break

#         except Exception as e:
#             print(f"💥 Unexpected error from {model}: {str(e)}")
#             continue

#     return jsonify({
#         "extracted": updated_memory,
#         "judgement": judgement_entry,
#         "tokens_used": final_result.get("tokens", {}) if final_result else {},
#         "model_used": final_model or "none",
#         "memory_updated": memory_updated
#     }), 200

from flask import Blueprint, request, jsonify
from app.utils.openrouter_client import call_openrouter
from app.utils.memory import merge_memory, save_memory, save_judgement
from datetime import datetime
import json
import re

extract_bp = Blueprint('extract', __name__)

@extract_bp.route('/extract', methods=['POST'])
def extract():
    user_input = request.json.get('message', '')
    existing_memory = request.json.get('memory', {})
    user_id = request.json.get('user_id', None)
    chat_id = request.json.get('chat_id', 'chat_1')

    if not user_input:
        return jsonify({"error": "Missing 'message' in request body"}), 400

    if not user_id:
        return jsonify({"error": "Missing 'user_id' in request"}), 400

    print("===== [/extract ROUTE HIT] =====")
    print(f"💬 User message: {user_input}")

    prompt = f"""
You are extracting personal facts **about the user** from their message.

Return two separate JSON blocks:

1. "jino_memory": factual memory only (like name, city, job, etc.)
2. "jino_judgement": emotional memory (like moods, opinions, personality insight)

Format:
{{
  "jino_memory": {{
    "key1": "value1"
  }},
  "jino_judgement": {{
    "judgement": "User seems frustrated but optimistic.",
    "category": "emotional_state",
    "confidence": "high"
  }}
}}

DO NOT wrap with markdown or explanation. Just pure JSON.

User message: "{user_input}"
""".strip()

    models = [
        "mistralai/mixtral-8x7b-instruct"
    ]

    final_model = None
    final_result = None
    memory_updated = False
    updated_memory = existing_memory
    judgement_entry = {}

    for model in models:
        try:
            print(f"⚙️ Trying model: {model}")
            result = call_openrouter(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3,
                max_tokens=400
            )

            raw_response = result.get("content", "").strip()
            print(f"📦 Raw model response:\n{raw_response}")

            # Fix common AI formatting issues
            cleaned = raw_response.replace("\\_", "_")
            cleaned = re.sub(r"```json|```", "", cleaned).strip()

            try:
                parsed = json.loads(cleaned)
            except json.JSONDecodeError as jde:
                print(f"❌ JSON decode failed after cleanup: {str(jde)}")
                print("🧽 Cleaned content that failed:\n", cleaned)
                continue

            if not isinstance(parsed, dict):
                print("⚠️ Model returned non-dict JSON. Skipping.")
                continue

            memory_data = parsed.get("jino_memory", {})
            judgement_data = parsed.get("jino_judgement", {})

            # ----- Save factual memory -----
            if isinstance(memory_data, dict) and memory_data:
                updated_memory = merge_memory(existing_memory, memory_data)
                memory_updated = updated_memory != existing_memory
                if memory_updated:
                    save_memory(user_id, updated_memory)
                    print("✅ jino_memory updated and saved.")
                else:
                    print("ℹ️ No new factual memory changes.")
            else:
                print("🫥 No valid jino_memory returned.")

            # ----- Save judgement memory -----
            if isinstance(judgement_data, dict) and "judgement" in judgement_data:
                judgement_entry = {
                    "timestamp": datetime.utcnow().isoformat(),
                    "category": judgement_data.get("category", "emotional_state"),
                    "judgement": judgement_data.get("judgement"),
                    "confidence": judgement_data.get("confidence", "medium")
                }

                save_judgement(user_id, chat_id, judgement_entry)
                print("🧠 [JINO Judgement Saved]:")
                print(json.dumps(judgement_entry, indent=2))
            else:
                print("🫥 No valid jino_judgement returned.")

            final_result = result
            final_model = model
            break

        except Exception as e:
            print(f"💥 Unexpected error from {model}: {str(e)}")
            continue

    return jsonify({
        "extracted": updated_memory,
        "judgement": judgement_entry,
        "tokens_used": final_result.get("tokens", {}) if final_result else {},
        "model_used": final_model or "none",
        "memory_updated": memory_updated
    }), 200
