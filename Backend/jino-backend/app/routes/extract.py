# # # # # from flask import Blueprint, request, jsonify
# # # # # from app.utils.openrouter_client import call_openrouter
# # # # # from app.utils.memory import merge_memory, save_memory, save_judgement
# # # # # from datetime import datetime
# # # # # import json
# # # # # import re

# # # # # extract_bp = Blueprint('extract', __name__)

# # # # # @extract_bp.route('/extract', methods=['POST'])
# # # # # def extract():
# # # # #     user_input = request.json.get('message', '')
# # # # #     existing_memory = request.json.get('memory', {})
# # # # #     convo_summary_list = request.json.get('convo_summary', [])  # 🧠 New input
# # # # #     user_id = request.json.get('user_id', None)
# # # # #     chat_id = request.json.get('chat_id', 'chat_1')

# # # # #     if not user_input:
# # # # #         return jsonify({"error": "Missing 'message' in request body"}), 400

# # # # #     if not user_id:
# # # # #         return jsonify({"error": "Missing 'user_id' in request"}), 400

# # # # #     print("===== [/extract ROUTE HIT] =====")
# # # # #     print(f"💬 User message: {user_input}")

# # # # #     # --- Base prompt for memory + judgement extraction ---
# # # # #     base_prompt = f"""
# # # # # You are extracting personal facts **about the user** from their message.

# # # # # Return two separate JSON blocks:

# # # # # 1. "jino_memory": factual memory only (like name, city, job, etc.)
# # # # # 2. "jino_judgement": emotional memory (like moods, opinions, personality insight)

# # # # # Format:
# # # # # {{
# # # # #   "jino_memory": {{
# # # # #     "key1": "value1"
# # # # #   }},
# # # # #   "jino_judgement": {{
# # # # #     "judgement": "User seems frustrated but optimistic.",
# # # # #     "category": "emotional_state",
# # # # #     "confidence": "high"
# # # # #   }}
# # # # # }}

# # # # # DO NOT wrap with markdown or explanation. Just pure JSON.

# # # # # User message: "{user_input}"
# # # # # """.strip()

# # # # #     # --- If convo summary list is provided, append this to prompt ---
# # # # #     convo_summary_prompt = ""
# # # # #     if convo_summary_list and isinstance(convo_summary_list, list):
# # # # #         convo_summary_prompt = "\n\nNow also summarize the following conversation:\n"
# # # # #         for entry in convo_summary_list[-6:]:  # FIFO – just last 6 to keep it snappy
# # # # #             msg = entry.get("message", "")
# # # # #             ts = entry.get("timestamp", "")
# # # # #             sender = entry.get("sender", "user")
# # # # #             role = "User" if sender == "user" else "Jino"
# # # # #             convo_summary_prompt += f"{role} ({ts}): {msg}\n"

# # # # #         convo_summary_prompt += """
# # # # # Return an additional key: "jino_convo_summary"

# # # # # It should be:
# # # # # {
# # # # #   "jino_convo_summary": {
# # # # #     "summary": "Brief but rich summary of last 6 interactions.",
# # # # #     "latest_timestamp": "ISO_8601_time_of_last_message"
# # # # #   }
# # # # # }
# # # # # """

# # # # #     full_prompt = base_prompt + convo_summary_prompt

# # # # #     models = [
# # # # #         "mistralai/mixtral-8x7b-instruct"
# # # # #     ]

# # # # #     final_model = None
# # # # #     final_result = None
# # # # #     memory_updated = False
# # # # #     updated_memory = existing_memory
# # # # #     judgement_entry = {}
# # # # #     convo_summary_output = {}

# # # # #     for model in models:
# # # # #         try:
# # # # #             print(f"⚙️ Trying model: {model}")
# # # # #             result = call_openrouter(
# # # # #                 model=model,
# # # # #                 messages=[{"role": "user", "content": full_prompt}],
# # # # #                 temperature=0.3,
# # # # #                 max_tokens=500
# # # # #             )

# # # # #             raw_response = result.get("content", "").strip()
# # # # #             print(f"📦 Raw model response:\n{raw_response}")

# # # # #             # Fix common formatting junk
# # # # #             cleaned = raw_response.replace("\\_", "_")
# # # # #             cleaned = re.sub(r"```json|```", "", cleaned).strip()

# # # # #             # Ensure cleaned response is valid JSON (check if it's empty or malformed)
# # # # #             if not cleaned:
# # # # #                 print("❌ Cleaned response is empty!")
# # # # #                 continue

# # # # #             try:
# # # # #                 parsed = json.loads(cleaned)
# # # # #             except json.JSONDecodeError as jde:
# # # # #                 print(f"❌ JSON decode failed after cleanup: {str(jde)}")
# # # # #                 print("🧽 Cleaned content that failed:\n", cleaned)
# # # # #                 continue

# # # # #             if not isinstance(parsed, dict):
# # # # #                 print("⚠️ Model returned non-dict JSON. Skipping.")
# # # # #                 continue

# # # # #             # ----- Memory -----
# # # # #             memory_data = parsed.get("jino_memory", {})
# # # # #             if isinstance(memory_data, dict) and memory_data:
# # # # #                 updated_memory = merge_memory(existing_memory, memory_data)
# # # # #                 memory_updated = updated_memory != existing_memory
# # # # #                 if memory_updated:
# # # # #                     save_memory(user_id, updated_memory)
# # # # #                     print("✅ jino_memory updated and saved.")
# # # # #                 else:
# # # # #                     print("ℹ️ No new factual memory changes.")
# # # # #             else:
# # # # #                 print("🫥 No valid jino_memory returned.")

# # # # #             # ----- Judgement -----
# # # # #             judgement_data = parsed.get("jino_judgement", {})
# # # # #             if isinstance(judgement_data, dict) and "judgement" in judgement_data:
# # # # #                 judgement_entry = {
# # # # #                     "timestamp": datetime.utcnow().isoformat(),
# # # # #                     "category": judgement_data.get("category", "emotional_state"),
# # # # #                     "judgement": judgement_data.get("judgement"),
# # # # #                     "confidence": judgement_data.get("confidence", "medium")
# # # # #                 }

# # # # #                 save_judgement(user_id, chat_id, judgement_entry)
# # # # #                 print("🧠 [JINO Judgement Saved]:")
# # # # #                 print(json.dumps(judgement_entry, indent=2))
# # # # #             else:
# # # # #                 print("🫥 No valid jino_judgement returned.")

# # # # #             # ----- Convo Summary (NEW STUFF) -----
# # # # #             convo_summary = parsed.get("jino_convo_summary", {})
# # # # #             if isinstance(convo_summary, dict) and "summary" in convo_summary:
# # # # #                 convo_summary_output = convo_summary
# # # # #                 print("🧾 [Convo Summary Extracted]:")
# # # # #                 print(json.dumps(convo_summary_output, indent=2))
# # # # #             else:
# # # # #                 print("⚠️ No valid convo summary found or malformed.")

# # # # #             final_result = result
# # # # #             final_model = model
# # # # #             break

# # # # #         except Exception as e:
# # # # #             print(f"💥 Unexpected error from {model}: {str(e)}")
# # # # #             continue

# # # # #     # Save memory and judgement to local storage on frontend side (replace it here for your frontend code)
# # # # #     response = {
# # # # #         "extracted": updated_memory,
# # # # #         "judgement": judgement_entry,
# # # # #         "convo_summary": convo_summary_output,
# # # # #         "tokens_used": final_result.get("tokens", {}) if final_result else {},
# # # # #         "model_used": final_model or "none",
# # # # #         "memory_updated": memory_updated
# # # # #     }

# # # # #     return jsonify(response), 200

# # # # from flask import Blueprint, request, jsonify
# # # # from app.utils.openrouter_client import call_openrouter
# # # # from app.utils.memory import merge_memory, save_memory, save_judgement
# # # # from datetime import datetime
# # # # import json
# # # # import re

# # # # extract_bp = Blueprint('extract', __name__)

# # # # @extract_bp.route('/extract', methods=['POST'])
# # # # def extract():
# # # #     user_input = request.json.get('message', '')
# # # #     existing_memory = request.json.get('memory', {})
# # # #     convo_summary_list = request.json.get('convo_summary', [])  # 🧠 New input
# # # #     user_id = request.json.get('user_id', None)
# # # #     chat_id = request.json.get('chat_id', 'chat_1')

# # # #     if not user_input:
# # # #         return jsonify({"error": "Missing 'message' in request body"}), 400

# # # #     if not user_id:
# # # #         return jsonify({"error": "Missing 'user_id' in request"}), 400

# # # #     print("===== [/extract ROUTE HIT] =====")
# # # #     print(f"💬 User message: {user_input}")

# # # #     # --- Base prompt for memory + judgement extraction ---
# # # #     base_prompt = f"""
# # # # You are extracting personal facts **about the user** from their message.

# # # # Return two separate JSON blocks:

# # # # 1. "jino_memory": factual memory only (like name, city, job, etc.)
# # # # 2. "jino_judgement": emotional memory (like moods, opinions, personality insight)

# # # # Format:
# # # # {{
# # # #   "jino_memory": {{
# # # #     "key1": "value1"
# # # #   }},
# # # #   "jino_judgement": {{
# # # #     "judgement": "User seems frustrated but optimistic.",
# # # #     "category": "emotional_state",
# # # #     "confidence": "high"
# # # #   }}
# # # # }}

# # # # DO NOT wrap with markdown or explanation. Just pure JSON.

# # # # User message: "{user_input}"
# # # # """.strip()

# # # #     # --- If convo summary list is provided, append this to prompt ---
# # # #     convo_summary_prompt = ""
# # # #     if convo_summary_list and isinstance(convo_summary_list, list):
# # # #         convo_summary_prompt = "\n\nNow also summarize the following conversation:\n"
# # # #         for entry in convo_summary_list[-6:]:  # FIFO – just last 6 to keep it snappy
# # # #             msg = entry.get("message", "")
# # # #             ts = entry.get("timestamp", "")
# # # #             sender = entry.get("sender", "user")
# # # #             role = "User" if sender == "user" else "Jino"
# # # #             convo_summary_prompt += f"{role} ({ts}): {msg}\n"

# # # #         convo_summary_prompt += """
# # # # Return an additional key: "jino_convo_summary"

# # # # It should be:
# # # # {
# # # #   "jino_convo_summary": {
# # # #     "summary": "Brief but rich summary of last 6 interactions.",
# # # #     "latest_timestamp": "ISO_8601_time_of_last_message"
# # # #   }
# # # # }
# # # # """

# # # #     full_prompt = base_prompt + convo_summary_prompt

# # # #     models = [
# # # #         "mistralai/mixtral-8x7b-instruct"
# # # #     ]

# # # #     final_model = None
# # # #     final_result = None
# # # #     memory_updated = False
# # # #     updated_memory = existing_memory
# # # #     judgement_entry = {}
# # # #     convo_summary_output = {}

# # # #     for model in models:
# # # #         try:
# # # #             print(f"⚙️ Trying model: {model}")
# # # #             result = call_openrouter(
# # # #                 model=model,
# # # #                 messages=[{"role": "user", "content": full_prompt}],
# # # #                 temperature=0.3,
# # # #                 max_tokens=500
# # # #             )

# # # #             raw_response = result.get("content", "").strip()
# # # #             print(f"📦 Raw model response:\n{raw_response}")

# # # #             # Fix common formatting junk
# # # #             cleaned = raw_response.replace("\\_", "_")
# # # #             cleaned = re.sub(r"```json|```", "", cleaned).strip()

# # # #             # Ensure cleaned response is valid JSON (check if it's empty or malformed)
# # # #             if not cleaned:
# # # #                 print("❌ Cleaned response is empty!")
# # # #                 continue

# # # #             try:
# # # #                 parsed = json.loads(cleaned)
# # # #             except json.JSONDecodeError as jde:
# # # #                 print(f"❌ JSON decode failed after cleanup: {str(jde)}")
# # # #                 print("🧽 Cleaned content that failed:\n", cleaned)
# # # #                 continue

# # # #             if not isinstance(parsed, dict):
# # # #                 print("⚠️ Model returned non-dict JSON. Skipping.")
# # # #                 continue

# # # #             # ----- Memory -----
# # # #             memory_data = parsed.get("jino_memory", {})
# # # #             if isinstance(memory_data, dict) and memory_data:
# # # #                 updated_memory = merge_memory(existing_memory, memory_data)
# # # #                 memory_updated = updated_memory != existing_memory
# # # #                 if memory_updated:
# # # #                     save_memory(user_id, updated_memory)
# # # #                     print("✅ jino_memory updated and saved.")
# # # #                 else:
# # # #                     print("ℹ️ No new factual memory changes.")
# # # #             else:
# # # #                 print("🫥 No valid jino_memory returned.")

# # # #             # ----- Judgement -----
# # # #             judgement_data = parsed.get("jino_judgement", {})
# # # #             if isinstance(judgement_data, dict) and "judgement" in judgement_data:
# # # #                 judgement_entry = {
# # # #                     "timestamp": datetime.utcnow().isoformat(),
# # # #                     "category": judgement_data.get("category", "emotional_state"),
# # # #                     "judgement": judgement_data.get("judgement"),
# # # #                     "confidence": judgement_data.get("confidence", "medium")
# # # #                 }

# # # #                 save_judgement(user_id, chat_id, judgement_entry)
# # # #                 print("🧠 [JINO Judgement Saved]:")
# # # #                 print(json.dumps(judgement_entry, indent=2))
# # # #             else:
# # # #                 print("🫥 No valid jino_judgement returned.")

# # # #             # ----- Convo Summary (NEW STUFF) -----
# # # #             convo_summary = parsed.get("jino_convo_summary", {})
# # # #             if isinstance(convo_summary, dict) and "summary" in convo_summary:
# # # #                 convo_summary_output = convo_summary
# # # #                 print("🧾 [Convo Summary Extracted]:")
# # # #                 print(json.dumps(convo_summary_output, indent=2))
# # # #             else:
# # # #                 print("⚠️ No valid convo summary found or malformed.")

# # # #             final_result = result
# # # #             final_model = model
# # # #             break

# # # #         except Exception as e:
# # # #             print(f"💥 Unexpected error from {model}: {str(e)}")
# # # #             continue

# # # #     # Save memory and judgement to local storage on frontend side (replace it here for your frontend code)
# # # #     response = {
# # # #         "extracted": updated_memory,
# # # #         "judgement": judgement_entry,
# # # #         "convo_summary": convo_summary_output,
# # # #         "tokens_used": final_result.get("tokens", {}) if final_result else {},
# # # #         "model_used": final_model or "none",
# # # #         "memory_updated": memory_updated
# # # #     }

# # # #     return jsonify(response), 200



# # # from flask import Blueprint, request, jsonify
# # # from app.utils.openrouter_client import call_openrouter
# # # from app.utils.memory import merge_memory, save_memory, save_judgement
# # # from datetime import datetime
# # # import json
# # # import re

# # # extract_bp = Blueprint('extract', __name__)

# # # @extract_bp.route('/extract', methods=['POST'])
# # # def extract():
# # #     user_input = request.json.get('message', '')
# # #     existing_memory = request.json.get('memory', {})
# # #     convo_summary_list = request.json.get('convo_summary', [])  # 🧠 New input
# # #     user_id = request.json.get('user_id', None)
# # #     chat_id = request.json.get('chat_id', 'chat_1')

# # #     if not user_input:
# # #         return jsonify({"error": "Missing 'message' in request body"}), 400

# # #     if not user_id:
# # #         return jsonify({"error": "Missing 'user_id' in request"}), 400

# # #     print("===== [/extract ROUTE HIT] =====")
# # #     print(f"💬 User message: {user_input}")

# # #     # --- Base prompt for memory + judgement extraction ---
# # #     base_prompt = f"""
# # # You are extracting personal facts **about the user** from their message.

# # # You must return a **single JSON object** that contains these keys:

# # # 1. "jino_memory" → factual memory only (like name, city, job, etc.)
# # # 2. "jino_judgement" → emotional memory (like moods, opinions, personality insight)

# # # If provided, summarize the conversation and include:
# # # 3. "jino_convo_summary" → Summary of last interactions + latest timestamp

# # # Format (MUST be one single valid JSON object):
# # # {{
# # #   "jino_memory": {{
# # #     "key1": "value1"
# # #   }},
# # #   "jino_judgement": {{
# # #     "judgement": "User seems frustrated but optimistic.",
# # #     "category": "emotional_state",
# # #     "confidence": "high"
# # #   }},
# # #   "jino_convo_summary": {{
# # #     "summary": "Brief but rich summary of last few interactions.",
# # #     "latest_timestamp": "2025-04-20T04:32:08Z"
# # #   }}
# # # }}

# # # DO NOT return multiple JSON blocks.
# # # DO NOT wrap with markdown or explanation. Just pure valid JSON.

# # # User message: "{user_input}"
# # # """.strip()

# # #     # --- If convo summary list is provided, append this to prompt ---
# # #     if convo_summary_list and isinstance(convo_summary_list, list):
# # #         convo_summary_prompt = "\n\nConversation history:\n"
# # #         for entry in convo_summary_list[-6:]:  # FIFO – just last 6 to keep it snappy
# # #             msg = entry.get("message", "")
# # #             ts = entry.get("timestamp", "")
# # #             sender = entry.get("sender", "user")
# # #             role = "User" if sender == "user" else "Jino"
# # #             convo_summary_prompt += f"{role} ({ts}): {msg}\n"

# # #         base_prompt += convo_summary_prompt

# # #     models = [
# # #         "mistralai/mixtral-8x7b-instruct"
# # #     ]

# # #     final_model = None
# # #     final_result = None
# # #     memory_updated = False
# # #     updated_memory = existing_memory
# # #     judgement_entry = {}
# # #     convo_summary_output = {}

# # #     for model in models:
# # #         try:
# # #             print(f"⚙️ Trying model: {model}")
# # #             result = call_openrouter(
# # #                 model=model,
# # #                 messages=[{"role": "user", "content": base_prompt}],
# # #                 temperature=0.3,
# # #                 max_tokens=500
# # #             )

# # #             raw_response = result.get("content", "").strip()
# # #             print(f"📦 Raw model response:\n{raw_response}")

# # #             # Fix common formatting junk
# # #             cleaned = raw_response.replace("\\_", "_")
# # #             cleaned = re.sub(r"```json|```", "", cleaned).strip()

# # #             if not cleaned:
# # #                 print("❌ Cleaned response is empty!")
# # #                 continue

# # #             try:
# # #                 parsed = json.loads(cleaned)
# # #             except json.JSONDecodeError as jde:
# # #                 print(f"❌ JSON decode failed after cleanup: {str(jde)}")
# # #                 print("🧽 Cleaned content that failed:\n", cleaned)
# # #                 continue

# # #             if not isinstance(parsed, dict):
# # #                 print("⚠️ Model returned non-dict JSON. Skipping.")
# # #                 continue

# # #             # ----- Memory -----
# # #             memory_data = parsed.get("jino_memory", {})
# # #             if isinstance(memory_data, dict) and memory_data:
# # #                 updated_memory = merge_memory(existing_memory, memory_data)
# # #                 memory_updated = updated_memory != existing_memory
# # #                 if memory_updated:
# # #                     save_memory(user_id, updated_memory)
# # #                     print("✅ jino_memory updated and saved.")
# # #                 else:
# # #                     print("ℹ️ No new factual memory changes.")
# # #             else:
# # #                 print("🫥 No valid jino_memory returned.")

# # #             # ----- Judgement -----
# # #             judgement_data = parsed.get("jino_judgement", {})
# # #             if isinstance(judgement_data, dict) and "judgement" in judgement_data:
# # #                 judgement_entry = {
# # #                     "timestamp": datetime.utcnow().isoformat(),
# # #                     "category": judgement_data.get("category", "emotional_state"),
# # #                     "judgement": judgement_data.get("judgement"),
# # #                     "confidence": judgement_data.get("confidence", "medium")
# # #                 }

# # #                 save_judgement(user_id, chat_id, judgement_entry)
# # #                 print("🧠 [JINO Judgement Saved]:")
# # #                 print(json.dumps(judgement_entry, indent=2))
# # #             else:
# # #                 print("🫥 No valid jino_judgement returned.")

# # #             # ----- Convo Summary (NEW STUFF) -----
# # #             convo_summary = parsed.get("jino_convo_summary", {})
# # #             if isinstance(convo_summary, dict) and "summary" in convo_summary:
# # #                 convo_summary_output = convo_summary
# # #                 print("🧾 [Convo Summary Extracted]:")
# # #                 print(json.dumps(convo_summary_output, indent=2))
# # #             else:
# # #                 print("⚠️ No valid convo summary found or malformed.")

# # #             final_result = result
# # #             final_model = model
# # #             break

# # #         except Exception as e:
# # #             print(f"💥 Unexpected error from {model}: {str(e)}")
# # #             continue

# # #     response = {
# # #         "extracted": updated_memory,
# # #         "judgement": judgement_entry,
# # #         "convo_summary": convo_summary_output,
# # #         "tokens_used": final_result.get("tokens", {}) if final_result else {},
# # #         "model_used": final_model or "none",
# # #         "memory_updated": memory_updated
# # #     }

# # #     return jsonify(response), 200


# # from flask import Blueprint, request, jsonify
# # from app.utils.openrouter_client import call_openrouter
# # from app.utils.memory import merge_memory, save_memory, save_judgement
# # from datetime import datetime
# # import json
# # import re

# # extract_bp = Blueprint('extract', __name__)

# # @extract_bp.route('/extract', methods=['POST'])
# # def extract():
# #     user_input = request.json.get('message', '')
# #     existing_memory = request.json.get('memory', {})
# #     convo_summary_list = request.json.get('convo_summary', [])  # 🧠 New input
# #     user_id = request.json.get('user_id', None)
# #     chat_id = request.json.get('chat_id', 'chat_1')

# #     if not user_input:
# #         return jsonify({"error": "Missing 'message' in request body"}), 400

# #     if not user_id:
# #         return jsonify({"error": "Missing 'user_id' in request"}), 400

# #     print("===== [/extract ROUTE HIT] =====")
# #     print(f"💬 User message: {user_input}")

# #     # --- Base prompt for memory + judgement extraction ---
# #     base_prompt = f"""
# # You are extracting personal facts **about the user** from their message.

# # You must return a **single JSON object** that contains these keys:

# # 1. "jino_memory" → factual memory only (like name, city, job, etc.)
# # 2. "jino_judgement" → emotional memory (like moods, opinions, personality insight)

# # If provided, summarize the conversation and include:
# # 3. "jino_convo_summary" → Summary of last interactions + latest timestamp

# # Format (MUST be one single valid JSON object):
# # {{
# #   "jino_memory": {{
# #     "key1": "value1"
# #   }},
# #   "jino_judgement": {{
# #     "judgement": "User seems frustrated but optimistic.",
# #     "category": "emotional_state",
# #     "confidence": "high"
# #   }},
# #   "jino_convo_summary": {{
# #     "summary": "Brief but rich summary of last few interactions.",
# #   }}
# # }}

# # DO NOT return multiple JSON blocks.
# # DO NOT wrap with markdown or explanation. Just pure valid JSON.

# # User message: "{user_input}"
# # """.strip()

# #     # --- Append convo history if provided ---
# #     if convo_summary_list and isinstance(convo_summary_list, list):
# #         convo_summary_prompt = "\n\nRecent Conversation History:\n"
# #         for entry in convo_summary_list[-6:]:  # last 6 messages max
# #             msg = entry.get("message", "")
# #             ts = entry.get("timestamp", "")
# #             sender = entry.get("sender", "user")
# #             role = "User" if sender == "user" else "Jino"
# #             convo_summary_prompt += f"{role} ({ts}): {msg}\n"

# #         base_prompt += convo_summary_prompt

# #     models = [
# #         "mistralai/mixtral-8x7b-instruct"
# #     ]

# #     final_model = None
# #     final_result = None
# #     memory_updated = False
# #     updated_memory = existing_memory
# #     judgement_entry = {}
# #     convo_summary_output = {}

# #     for model in models:
# #         try:
# #             print(f"⚙️ Trying model: {model}")
# #             result = call_openrouter(
# #                 model=model,
# #                 messages=[{"role": "user", "content": base_prompt}],
# #                 temperature=0.3,
# #                 max_tokens=500
# #             )

# #             raw_response = result.get("content", "").strip()
# #             print(f"📦 Raw model response:\n{raw_response}")

# #             # Fix common formatting junk
# #             cleaned = raw_response.replace("\\_", "_")
# #             cleaned = re.sub(r"```json|```", "", cleaned).strip()

# #             if not cleaned:
# #                 print("❌ Cleaned response is empty!")
# #                 continue

# #             try:
# #                 parsed = json.loads(cleaned)
# #             except json.JSONDecodeError as jde:
# #                 print(f"❌ JSON decode failed after cleanup: {str(jde)}")
# #                 print("🧽 Cleaned content that failed:\n", cleaned)
# #                 continue

# #             if not isinstance(parsed, dict):
# #                 print("⚠️ Model returned non-dict JSON. Skipping.")
# #                 continue

# #             # ----- Memory -----
# #             memory_data = parsed.get("jino_memory", {})
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

# #             # ----- Judgement -----
# #             judgement_data = parsed.get("jino_judgement", {})
# #             if isinstance(judgement_data, dict) and "judgement" in judgement_data:
# #                 judgement_entry = {
# #                     "category": judgement_data.get("category", "emotional_state"),
# #                     "judgement": judgement_data.get("judgement"),
# #                     "confidence": judgement_data.get("confidence", "medium")
# #                 }

# #                 save_judgement(user_id, chat_id, judgement_entry)
# #                 print("🧠 [JINO Judgement Saved]:")
# #                 print(json.dumps(judgement_entry, indent=2))
# #             else:
# #                 print("🫥 No valid jino_judgement returned.")

# #             # ----- Convo Summary (NEW STUFF) -----
# #             convo_summary = parsed.get("jino_convo_summary", {})
# #             if isinstance(convo_summary, dict) and "summary" in convo_summary:
# #                 convo_summary_output = convo_summary
# #                 print("🧾 [Convo Summary Extracted]:")
# #                 print(json.dumps(convo_summary_output, indent=2))
# #             else:
# #                 print("⚠️ No valid convo summary found or malformed.")

# #             final_result = result
# #             final_model = model
# #             break

# #         except Exception as e:
# #             print(f"💥 Unexpected error from {model}: {str(e)}")
# #             continue

# #     response = {
# #         "extracted": updated_memory,
# #         "judgement": judgement_entry,
# #         "convo_summary": convo_summary_output,
# #         "tokens_used": final_result.get("tokens", {}) if final_result else {},
# #         "model_used": final_model or "none",
# #         "memory_updated": memory_updated
# #     }

# #     return jsonify(response), 200

# from flask import Blueprint, request, jsonify
# from app.utils.openrouter_client import call_openrouter
# from app.utils.memory import merge_memory, save_memory, save_judgement
# from datetime import datetime
# import json
# import re

# extract_bp = Blueprint('extract', __name__)

# @extract_bp.route('/extract', methods=['POST'])
# def extract():
#     user_input = request.json.get('message', '')
#     existing_memory = request.json.get('memory', {})
#     convo_summary_list = request.json.get('convo_summary', [])  # 🧠 New input
#     user_id = request.json.get('user_id', None)
#     chat_id = request.json.get('chat_id', 'chat_1')

#     # Validate user input and user_id
#     if not user_input:
#         return jsonify({"error": "Missing 'message' in request body"}), 400

#     if not user_id:
#         return jsonify({"error": "Missing 'user_id' in request"}), 400

#     print("===== [/extract ROUTE HIT] =====")
#     print(f"💬 User message: {user_input}")

#     # --- Base prompt for memory + judgement extraction ---
#     base_prompt = f"""
# You are extracting personal facts **about the user** from their message.

# You must return a **single JSON object** that contains these keys:

# 1. "jino_memory" → factual memory only (like name, city, job, etc.)
# 2. "jino_judgement" → emotional memory (like moods, opinions, personality insight)

# If provided, summarize the conversation and include:
# 3. "jino_convo_summary" → Summary of last interactions + latest timestamp

# Format (MUST be one single valid JSON object):
# {{
#   "jino_memory": {{
#     "key1": "value1"
#   }},
#   "jino_judgement": {{
#     "judgement": "User seems frustrated but optimistic.",
#     "category": "emotional_state",
#     "confidence": "high"
#   }},
#   "jino_convo_summary": {{
#     "summary": "Brief but rich summary of last few interactions.",
#   }}
# }}

# DO NOT return multiple JSON blocks.
# DO NOT wrap with markdown or explanation. Just pure valid JSON.

# User message: "{user_input}"
# """.strip()

#     # --- Append convo history if provided ---
#     if convo_summary_list and isinstance(convo_summary_list, list):
#         convo_summary_prompt = "\n\nRecent Conversation History:\n"
#         for entry in convo_summary_list[-6:]:  # last 6 messages max
#             msg = entry.get("message", "")
#             ts = entry.get("timestamp", "")
#             sender = entry.get("sender", "user")
#             role = "User" if sender == "user" else "Jino"
#             convo_summary_prompt += f"{role} ({ts}): {msg}\n"

#         base_prompt += convo_summary_prompt

#     models = [
#         "mistralai/mixtral-8x7b-instruct"
#     ]

#     final_model = None
#     final_result = None
#     memory_updated = False
#     updated_memory = existing_memory
#     judgement_entry = {}
#     convo_summary_output = {}

#     for model in models:
#         try:
#             print(f"⚙️ Trying model: {model}")
#             result = call_openrouter(
#                 model=model,
#                 messages=[{"role": "user", "content": base_prompt}],
#                 temperature=0.3,
#                 max_tokens=500
#             )

#             raw_response = result.get("content", "").strip()
#             print(f"📦 Raw model response:\n{raw_response}")

#             # Fix common formatting junk
#             cleaned = raw_response.replace("\\_", "_")
#             cleaned = re.sub(r"```json|```", "", cleaned).strip()

#             # Ensure the response ends with a closing brace
#             if not raw_output.strip().endswith('}'):
#                 raw_response += '}'


#             if not cleaned:
#                 print("❌ Cleaned response is empty!")
#                 continue

#             try:
#                 parsed = json.loads(cleaned)
#             except json.JSONDecodeError as jde:
#                 print(f"❌ JSON decode failed after cleanup: {str(jde)}")
#                 print("🧽 Cleaned content that failed:\n", cleaned)
#                 continue

#             if not isinstance(parsed, dict):
#                 print("⚠️ Model returned non-dict JSON. Skipping.")
#                 continue

#             # ----- Memory -----
#             memory_data = parsed.get("jino_memory", {})
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

#             # ----- Judgement -----
#             judgement_data = parsed.get("jino_judgement", {})
#             if isinstance(judgement_data, dict) and "judgement" in judgement_data:
#                 judgement_entry = {
#                     "category": judgement_data.get("category", "emotional_state"),
#                     "judgement": judgement_data.get("judgement"),
#                     "confidence": judgement_data.get("confidence", "medium")
#                 }

#                 save_judgement(user_id, chat_id, judgement_entry)
#                 print("🧠 [JINO Judgement Saved]:")
#                 print(json.dumps(judgement_entry, indent=2))
#             else:
#                 print("🫥 No valid jino_judgement returned.")

#             # ----- Convo Summary (NEW STUFF) -----
#             convo_summary = parsed.get("jino_convo_summary", {})
#             if isinstance(convo_summary, dict) and "summary" in convo_summary:
#                 convo_summary_output = convo_summary
#                 print("🧾 [Convo Summary Extracted]:")
#                 print(json.dumps(convo_summary_output, indent=2))
#             else:
#                 print("⚠️ No valid convo summary found or malformed.")

#             final_result = result
#             final_model = model
#             break

#         except Exception as e:
#             print(f"💥 Unexpected error from {model}: {str(e)}")
#             continue

#     # Response structure to return
#     response = {
#         "extracted": updated_memory,
#         "judgement": judgement_entry,
#         "convo_summary": convo_summary_output,
#         "tokens_used": final_result.get("tokens", {}) if final_result else {},
#         "model_used": final_model or "none",
#         "memory_updated": memory_updated
#     }

#     return jsonify(response), 200
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
    existing_memory = request.json.get('memory', {}) or {}
    convo_summary_list = request.json.get('convo_summary', [])  # 🧠 New input
    user_id = request.json.get('user_id', None)
    chat_id = request.json.get('chat_id', 'chat_1')

    # Validate inputs
    if not user_input:
        return jsonify({"error": "Missing 'message' in request body"}), 400
    if not user_id:
        return jsonify({"error": "Missing 'user_id' in request"}), 400

    print("===== [/extract ROUTE HIT] =====")
    print(f"💬 User message: {user_input}")

    # --- Build prompt ---
    base_prompt = f"""
You are extracting personal facts **about the user** from their message.

You must return a **single JSON object** that contains these keys:

1. "jino_memory" → factual memory only (like name, city, job, etc.)
2. "jino_judgement" → emotional memory (like moods, opinions, personality insight)

If provided, summarize the conversation and include:
3. "jino_convo_summary" → Summary of last interactions + latest timestamp

Format (MUST be one single valid JSON object):
{{
  "jino_memory": {{
    "key1": "value1"
  }},
  "jino_judgement": {{
    "judgement": "User seems frustrated but optimistic.",
    "category": "emotional_state",
    "confidence": "high"
  }},
  "jino_convo_summary": {{
    "summary": "Brief but rich summary of last few interactions.",
    "latest_timestamp": "2025-04-20T04:32:08Z"
  }}
}}

DO NOT return multiple JSON blocks.
DO NOT wrap with markdown or explanation. Just pure valid JSON.

User message: "{user_input}"
""".strip()

    # Append recent convo history if available
    if isinstance(convo_summary_list, list) and convo_summary_list:
        base_prompt += "\n\nRecent Conversation History:\n"
        for entry in convo_summary_list[-6:]:
            ts = entry.get("timestamp", "")
            msg = entry.get("message", "")
            role = "User" if entry.get("sender", "user") == "user" else "Jino"
            base_prompt += f"{role} ({ts}): {msg}\n"

    models = ["mistralai/mixtral-8x7b-instruct"]

    final_model = None
    final_result = None
    memory_updated = False
    updated_memory = existing_memory.copy()
    judgement_entry = {}
    convo_summary_output = {}

    for model in models:
        try:
            print(f"⚙️ Trying model: {model}")
            result = call_openrouter(
                model=model,
                messages=[{"role": "user", "content": base_prompt}],
                temperature=0.3,
                max_tokens=500
            )

            raw = result.get("content", "").strip()
            print("📦 Raw model response:\n", raw)

            # Cleanup formatting
            cleaned = re.sub(r"```json|```", "", raw).replace("\\_", "_").strip()
            if not cleaned.endswith("}"):
                print("🔧 Appending missing '}'")
                cleaned += "}"
            print("🔍 Cleaned JSON:\n", cleaned)

            parsed = json.loads(cleaned)
            if not isinstance(parsed, dict):
                print("⚠️ Parsed JSON not an object, skipping.")
                continue

            # ----- Memory Handling -----
            memory_data = parsed.get("jino_memory", {}) or {}

            # Custom name logic:
            new_name = memory_data.get("name", "").strip()
            old_name = existing_memory.get("name", "").strip()
            if new_name and old_name:
                new_lower, old_lower = new_name.lower(), old_name.lower()
                # expansion case: old_name → "afnan", new_name → "afnan ahmed"
                if new_lower.startswith(old_lower) and new_lower != old_lower:
                    print("ℹ️ Detected name expansion; moving to full_name")
                    memory_data.pop("name", None)
                    memory_data["full_name"] = new_name
                # contraction case: old_name → "afnan ahmed", new_name → "afnan"
                elif old_lower.startswith(new_lower) and new_lower != old_lower:
                    print("ℹ️ Detected name contraction; dropping new_name")
                    memory_data.pop("name", None)
                # completely different: replace
                else:
                    print("ℹ️ Detected completely new name; replacing 'name'")
                    memory_data["name"] = new_name

            # Merge only if there’s at least one valid key
            if isinstance(memory_data, dict) and memory_data:
                merged = merge_memory(updated_memory, memory_data)
                if merged != updated_memory:
                    updated_memory = merged
                    memory_updated = True
                    save_memory(user_id, updated_memory)
                    print("✅ jino_memory merged & saved:", updated_memory)
                else:
                    print("ℹ️ Memory present but no actual changes after merge")
            else:
                print("🫥 No valid jino_memory to merge")

            # ----- Judgement -----
            j_data = parsed.get("jino_judgement", {}) or {}
            if isinstance(j_data, dict) and "judgement" in j_data:
                judgement_entry = {
                    "timestamp": datetime.utcnow().isoformat(),
                    "category": j_data.get("category", "emotional_state"),
                    "judgement": j_data["judgement"],
                    "confidence": j_data.get("confidence", "medium")
                }
                save_judgement(user_id, chat_id, judgement_entry)
                print("🧠 jino_judgement saved:", judgement_entry)
            else:
                print("🫥 No valid jino_judgement returned")

            # ----- Convo Summary -----
            cs = parsed.get("jino_convo_summary", {}) or {}
            if isinstance(cs, dict) and "summary" in cs:
                if "latest_timestamp" not in cs:
                    cs["latest_timestamp"] = datetime.utcnow().isoformat()
                convo_summary_output = cs
                print("🧾 jino_convo_summary extracted:", cs)
            else:
                print("⚠️ No valid jino_convo_summary found")

            final_model = model
            final_result = result
            break

        except Exception as e:
            print(f"💥 Unexpected error in {model}:", e)
            continue

    response = {
        "extracted": updated_memory,
        "judgement": judgement_entry,
        "convo_summary": convo_summary_output,
        "tokens_used": final_result.get("tokens", {}) if final_result else {},
        "model_used": final_model or "none",
        "memory_updated": memory_updated
    }

    print("📤 /extract response payload:", response)
    return jsonify(response), 200
