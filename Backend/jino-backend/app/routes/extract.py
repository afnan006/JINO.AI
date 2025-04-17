# # # # # # # # from flask import Blueprint, request, jsonify
# # # # # # # # from app.utils.openrouter_client import call_openrouter
# # # # # # # # import json
# # # # # # # # import re

# # # # # # # # extract_bp = Blueprint('extract', __name__)

# # # # # # # # @extract_bp.route('/extract', methods=['POST'])
# # # # # # # # def extract():
# # # # # # # #     user_input = request.json.get('message', '')

# # # # # # # #     if not user_input:
# # # # # # # #         return jsonify({"error": "Missing 'message' in request body"}), 400

# # # # # # # #     prompt = prompt = f"""
# # # # # # # # Extract personal facts from the user's message as a clean JSON object.

# # # # # # # # Rules:
# # # # # # # # - Group into 3–6 broad sections: personal, work, health, love, passions, finance.
# # # # # # # # - Inside each section, use short lowercase keys: name, age, city, job, crush, sleep, savings, etc.
# # # # # # # # - Focus on identity info first (name, age, job, city) — these go top of JSON.
# # # # # # # # - Keep values clear, short, and normalized. Don’t copy user’s exact slang.
# # # # # # # # - Interpret sarcasm, slang, and emotional tone — rewrite them into real facts.
# # # # # # # # - Capture time references like “for 2 years” or “since 2020”.
# # # # # # # # - No summaries, no bullet points. Just flat clean JSON. One level. No explanations.

# # # # # # # # User message: "{user_input}"
# # # # # # # # """.strip()

# # # # # # # #     models = [
# # # # # # # #         "deepseek/deepseek-r1:free",
# # # # # # # #         "mistralai/mixtral-8x7b-instruct"  # fallback
# # # # # # # #     ]

# # # # # # # #     for model in models:
# # # # # # # #         try:
# # # # # # # #             print(f"🔥 Trying model: {model}")
# # # # # # # #             result = call_openrouter(
# # # # # # # #                 model=model,
# # # # # # # #                 messages=[{"role": "user", "content": prompt}],
# # # # # # # #                 temperature=0,
# # # # # # # #                 max_tokens=300
# # # # # # # #             )

# # # # # # # #             raw_response = result.get("content", "").strip()
# # # # # # # #             token_data = result.get("tokens", {})

# # # # # # # #             print("\n📦 RAW RESPONSE:\n", raw_response)

# # # # # # # #             # Clean markdown wrappers if any
# # # # # # # #             cleaned = re.sub(r"```json|```", "", raw_response).strip()

# # # # # # # #             if not cleaned:
# # # # # # # #                 print(f"⚠️ Model '{model}' gave empty response.")
# # # # # # # #                 continue  # Try next model

# # # # # # # #             extracted_json = json.loads(cleaned)

# # # # # # # #             return jsonify({
# # # # # # # #                 "extracted": extracted_json,
# # # # # # # #                 "tokens_used": token_data,
# # # # # # # #                 "model_used": model
# # # # # # # #             }), 200

# # # # # # # #         except json.JSONDecodeError:
# # # # # # # #             print(f"❌ JSON parsing failed from model '{model}':\n{raw_response}")
# # # # # # # #             continue  # Try next model

# # # # # # # #         except Exception as e:
# # # # # # # #             print(f"💥 Error using model '{model}': {e}")
# # # # # # # #             continue  # Try next

# # # # # # # #     return jsonify({
# # # # # # # #         "error": "Extraction failed. All models gave up or returned junk.",
# # # # # # # #         "raw_response": raw_response
# # # # # # # #     }), 500


# # # # # # # # FILE: app/routes/extract.py

# # # # # # # from flask import Blueprint, request, jsonify
# # # # # # # from app.utils.openrouter_client import call_openrouter
# # # # # # # import json
# # # # # # # import re

# # # # # # # extract_bp = Blueprint('extract', __name__)

# # # # # # # @extract_bp.route('/extract', methods=['POST'])
# # # # # # # def extract():
# # # # # # #     user_input = request.json.get('message', '')

# # # # # # #     if not user_input:
# # # # # # #         return jsonify({"error": "Missing 'message' in request body"}), 400

# # # # # # #     prompt = f"""
# # # # # # # Extract personal facts from the user's message as a clean JSON object.

# # # # # # # Rules:
# # # # # # # - Group into 3–6 sections: personal, work, health, love, passions, finance.
# # # # # # # - Use lowercase keys: name, age, city, job, crush, stress, savings, etc.
# # # # # # # - Normalize slang and sarcasm into facts. Interpret tone if needed.
# # # # # # # - Prefer identity info (name, age, job, city) at the top.
# # # # # # # - One-level JSON only. No bullet points or extra commentary.

# # # # # # # User message: "{user_input}"
# # # # # # # """.strip()

# # # # # # #     models = [
# # # # # # #         "deepseek/deepseek-r1:free",
# # # # # # #         "mistralai/mixtral-8x7b-instruct"  # fallback
# # # # # # #     ]

# # # # # # #     for model in models:
# # # # # # #         try:
# # # # # # #             result = call_openrouter(
# # # # # # #                 model=model,
# # # # # # #                 messages=[{"role": "user", "content": prompt}],
# # # # # # #                 temperature=0,
# # # # # # #                 max_tokens=300
# # # # # # #             )

# # # # # # #             raw_response = result.get("content", "").strip()
# # # # # # #             cleaned = re.sub(r"```json|```", "", raw_response).strip()

# # # # # # #             if not cleaned:
# # # # # # #                 continue

# # # # # # #             extracted_json = json.loads(cleaned)

# # # # # # #             return jsonify({
# # # # # # #                 "extracted": extracted_json,
# # # # # # #                 "tokens_used": result.get("tokens", {}),
# # # # # # #                 "model_used": model
# # # # # # #             }), 200

# # # # # # #         except json.JSONDecodeError:
# # # # # # #             continue
# # # # # # #         except Exception as e:
# # # # # # #             continue

# # # # # # #     return jsonify({
# # # # # # #         "error": "Extraction failed. All models gave up or returned junk.",
# # # # # # #         "raw_response": raw_response
# # # # # # #     }), 500
# # # # ---------------------------------------IMP-IMP--------------------------------------------------
# # # # from flask import Blueprint, request, jsonify
# # # # from app.utils.openrouter_client import call_openrouter
# # # # import json
# # # # from app.utils.memory import merge_memory
# # # # import re

# # # # extract_bp = Blueprint('extract', __name__)

# # # # @extract_bp.route('/extract', methods=['POST'])
# # # # def extract():
# # # #     user_input = request.json.get('message', '')

# # # #     if not user_input:
# # # #         return jsonify({"error": "Missing 'message' in request body"}), 400

# # # #     prompt = f"""
# # # # Extract personal facts from the user's message as a clean JSON object.

# # # # Rules:
# # # # - Group into 3–6 sections: personal, work, health, love, passions, finance.
# # # # - Use lowercase keys: name, age, city, job, crush, stress, savings, etc.
# # # # - Normalize slang and sarcasm into facts. Interpret tone if needed.
# # # # - Prefer identity info (name, age, job, city) at the top.
# # # # - One-level JSON only. No bullet points or extra commentary.

# # # # User message: "{user_input}"
# # # # """.strip()

# # # #     models = [
# # # #         "deepseek/deepseek-r1:free",
# # # #         "mistralai/mixtral-8x7b-instruct"  # fallback
# # # #     ]

# # # #     for model in models:
# # # #         try:
# # # #             result = call_openrouter(
# # # #                 model=model,
# # # #                 messages=[{"role": "user", "content": prompt}],
# # # #                 temperature=0,
# # # #                 max_tokens=300
# # # #             )

# # # #             raw_response = result.get("content", "").strip()
# # # #             cleaned = re.sub(r"```json|```", "", raw_response).strip()

# # # #             if not cleaned:
# # # #                 continue

# # # #             extracted_json = json.loads(cleaned)
# # # #             # Fetch current memory sent from frontend (optional but useful for now)
# # # #             existing_memory = request.json.get('existing_memory', {})

# # # # # Merge new memory into existing one
# # # #             updated_memory = merge_memory(existing_memory, extracted_json)




# # # #             # Return the extracted memory and judgement
# # # #             return jsonify({
# # # #                 "extracted": extracted_json,
# # # #                 "judgement": {},  # Add judgment logic here if needed
# # # #                 "tokens_used": result.get("tokens", {}),
# # # #                 "model_used": model
# # # #             }), 200

# # # #         except json.JSONDecodeError:
# # # #             continue
# # # #         except Exception as e:
# # # #             continue

# # # #     return jsonify({
# # # #     "extracted": updated_memory,  # Send merged memory instead
# # # #     "judgement": {},  # Add judgment logic here if needed
# # # #     "tokens_used": result.get("tokens", {}),
# # # #     "model_used": model
# # # # }), 200
# # # # -----------------------------iIMP-IMP-----------------------------------------------------
    
# # #         # return jsonify({
# # #         #     "error": "Extraction failed. All models gave up or returned junk.",
# # #         #     "raw_response": raw_response
# # #         # }), 500



# # # # from flask import Blueprint, request, jsonify
# # # # from app.utils.openrouter_client import call_openrouter
# # # # import json
# # # # import re
# # # # from app.utils.memory import merge_memory, clean_invalid_fields
# # # # from app.utils.uuid_gen import validate_uuid

# # # # extract_bp = Blueprint('extract', __name__)

# # # # @extract_bp.route('/extract', methods=['POST'])
# # # # def extract():
# # # #     user_input = request.json.get('message', '')
# # # #     user_uuid = request.json.get('uuid', None)
# # # #     existing_memory = request.json.get('existing_memory', {})

# # # #     if not user_input:
# # # #         return jsonify({"error": "Missing 'message' in request body"}), 400

# # # #     if not user_uuid or not validate_uuid(user_uuid):
# # # #         return jsonify({"error": "Invalid or missing UUID"}), 400

# # # #     prompt = f"""
# # # # Extract personal facts from the user's message as a clean JSON object.

# # # # Rules:
# # # # - Group into 3–6 sections: personal, work, health, love, passions, finance.
# # # # - Use lowercase keys: name, age, city, job, crush, stress, savings, etc.
# # # # - Normalize slang and sarcasm into facts. Interpret tone if needed.
# # # # - Prefer identity info (name, age, job, city) at the top.
# # # # - One-level JSON only. No bullet points or extra commentary.

# # # # User message: "{user_input}"
# # # # """.strip()

# # # #     models = [
# # # #         "deepseek/deepseek-r1:free",
# # # #         "mistralai/mixtral-8x7b-instruct"
# # # #     ]

# # # #     for model in models:
# # # #         try:
# # # #             result = call_openrouter(
# # # #                 model=model,
# # # #                 messages=[{"role": "user", "content": prompt}],
# # # #                 temperature=0,
# # # #                 max_tokens=300
# # # #             )

# # # #             raw_response = result.get("content", "").strip()
# # # #             cleaned = re.sub(r"```json|```", "", raw_response).strip()

# # # #             if not cleaned:
# # # #                 continue

# # # #             extracted_json = json.loads(cleaned)

# # # #             # Clean up unwanted junk like "not provided"
# # # #             cleaned_extracted = clean_invalid_fields(extracted_json)

# # # #             # Merge with previous memory
# # # #             updated_memory = merge_memory(existing_memory, cleaned_extracted)

# # # #             # Auto-generate judgement
# # # #             judgement = {
# # # #                 "mood": "sarcastic but caring",
# # # #                 "trust": "medium",
# # # #                 "last_updated": "auto",  # to be handled in frontend or added via timestamp later
# # # #             }

# # # #             return jsonify({
# # # #                 "extracted": cleaned_extracted,
# # # #                 "updated_memory": updated_memory,
# # # #                 "judgement": judgement,
# # # #                 "tokens_used": result.get("tokens", {}),
# # # #                 "model_used": model
# # # #             }), 200

# # # #         except json.JSONDecodeError:
# # # #             continue
# # # #         except Exception as e:
# # # #             continue

# # # #     return jsonify({
# # # #         "error": "All models failed. Either API is drunk or input was too weird."
# # # #     }), 500

# # # # from flask import Blueprint, request, jsonify
# # # # from app.utils.openrouter_client import call_openrouter
# # # # import json
# # # # import re
# # # # from app.utils.memory import merge_memory, clean_invalid_fields
# # # # from app.utils.uuid_gen import validate_uuid

# # # # extract_bp = Blueprint('extract', __name__)

# # # # @extract_bp.route('/extract', methods=['POST'])

# # # # def extract():
# # # #     print("📩 Incoming /extract request:", request.json)
# # # #     print("🔍 Extracting personal facts from user input...")
# # # #     user_input = request.json.get('message', '')
# # # #     user_uuid = request.json.get('uuid', None)
# # # #     existing_memory = request.json.get('existing_memory', {})

# # # #     if not user_input:
# # # #         return jsonify({"error": "Missing 'message' in request body"}), 400

# # # #     if not user_uuid or not validate_uuid(user_uuid):
# # # #         return jsonify({"error": "Invalid or missing UUID"}), 400

# # # #     prompt = f"""
# # # # Extract personal facts from the user's message as a clean JSON object.

# # # # Rules:
# # # # - Group into 3–6 sections: personal, work, health, love, passions, finance.
# # # # - Use lowercase keys: name, age, city, job, crush, stress, savings, etc.
# # # # - Normalize slang and sarcasm into facts. Interpret tone if needed.
# # # # - Prefer identity info (name, age, job, city) at the top.
# # # # - One-level JSON only. No bullet points or extra commentary.

# # # # User message: "{user_input}"
# # # # """.strip()

# # # #     models = [
# # # #         "deepseek/deepseek-r1:free",
# # # #         "mistralai/mixtral-8x7b-instruct"
# # # #     ]

# # # #     for model in models:
# # # #         try:
# # # #             result = call_openrouter(
# # # #                 model=model,
# # # #                 messages=[{"role": "user", "content": prompt}],
# # # #                 temperature=0,
# # # #                 max_tokens=300
# # # #             )

# # # #             raw_response = result.get("content", "").strip()
# # # #             cleaned = re.sub(r"```json|```", "", raw_response).strip()

# # # #             if not cleaned:
# # # #                 print(f"[{model}] Empty or invalid response.")
# # # #                 continue

# # # #             try:
# # # #                 extracted_json = json.loads(cleaned)
# # # #             except json.JSONDecodeError as je:
# # # #                 print(f"[{model}] JSON decode error: {je}")
# # # #                 print(f"[{model}] Raw output: {cleaned}")
# # # #                 continue

# # # #             cleaned_extracted = clean_invalid_fields(extracted_json)
# # # #             updated_memory = merge_memory(existing_memory, cleaned_extracted)

# # # #             judgement = {
# # # #                 "mood": "sarcastic but caring",
# # # #                 "trust": "medium",
# # # #                 "last_updated": "auto"
# # # #             }

# # # #             return jsonify({
# # # #                 "extracted": cleaned_extracted,
# # # #                 "updated_memory": updated_memory,
# # # #                 "judgement": judgement,
# # # #                 "tokens_used": result.get("tokens", {}),
# # # #                 "model_used": model
# # # #             }), 200

# # # #         except Exception as e:
# # # #             print(f"[{model}] Model failed with error: {e}")
# # # #             continue

# # # #     return jsonify({
# # # #         "error": "All models failed. API might be asleep or response was not JSON.",
# # # #         "suggestion": "Try simpler message or check server logs."
# # # #     }), 500
# # # #----------------------------------------------------------------------------------------------
# # # from flask import Blueprint, request, jsonify
# # # from app.utils.openrouter_client import call_openrouter
# # # import json
# # # from app.utils.memory import merge_memory
# # # import re

# # # extract_bp = Blueprint('extract', __name__)

# # # @extract_bp.route('/extract', methods=['POST'])
# # # def extract():
# # #     user_input = request.json.get('message', '')

# # #     if not user_input:
# # #         return jsonify({"error": "Missing 'message' in request body"}), 400

# # #     prompt = f"""
# # # Extract personal facts from the user's message as a clean JSON object.

# # # Rules:
# # # - Group into 3–6 sections: personal, work, health, love, passions, finance.
# # # - Use lowercase keys: name, age, city, job, crush, stress, savings, etc.
# # # - Normalize slang and sarcasm into facts. Interpret tone if needed.
# # # - Prefer identity info (name, age, job, city) at the top.
# # # - One-level JSON only. No bullet points or extra commentary.

# # # User message: "{user_input}"
# # # """.strip()

# # #     models = [
# # #         "deepseek/deepseek-r1:free",
# # #         "mistralai/mixtral-8x7b-instruct"  # fallback
# # #     ]

# # #     for model in models:
# # #         try:
# # #             result = call_openrouter(
# # #                 model=model,
# # #                 messages=[{"role": "user", "content": prompt}],
# # #                 temperature=0,
# # #                 max_tokens=300
# # #             )

# # #             raw_response = result.get("content", "").strip()
# # #             cleaned = re.sub(r"```json|```", "", raw_response).strip()

# # #             if not cleaned:
# # #                 continue

# # #             extracted_json = json.loads(cleaned)
# # #             # Fetch current memory sent from frontend (optional but useful for now)
# # #             existing_memory = request.json.get('existing_memory', {})

# # # # Merge new memory into existing one
# # #             updated_memory = merge_memory(existing_memory, extracted_json)




# # #             # Return the extracted memory and judgement
# # #             return jsonify({
# # #                 "extracted": extracted_json,
# # #                 "judgement": {},  # Add judgment logic here if needed
# # #                 "tokens_used": result.get("tokens", {}),
# # #                 "model_used": model
# # #             }), 200

# # #         except json.JSONDecodeError:
# # #             continue
# # #         except Exception as e:
# # #             continue

# # #     return jsonify({
# # #     "extracted": updated_memory,  # Send merged memory instead
# # #     "judgement": {},  # Add judgment logic here if needed
# # #     "tokens_used": result.get("tokens", {}),
# # #     "model_used": model
# # # }), 200

# # from flask import Blueprint, request, jsonify
# # from app.utils.openrouter_client import call_openrouter
# # from app.utils.memory import merge_memory
# # import json
# # import re

# # extract_bp = Blueprint('extract', __name__)

# # @extract_bp.route('/extract', methods=['POST'])
# # def extract():
# #     user_input = request.json.get('message', '')
# #     # 🔥 FIXED KEY NAME HERE 🔥
# #     existing_memory = request.json.get('memory', {})

# #     if not user_input:
# #         print("❌ No 'message' found in request body")
# #         return jsonify({"error": "Missing 'message' in request body"}), 400

# #     print("===== [/extract ROUTE HIT] =====")
# #     print(f"💬 User message: {user_input}")
# #     print("📂 Existing memory (before merge):")
# #     print(json.dumps(existing_memory, indent=2))

# # #     prompt = f"""
# # # Extract personal facts from the user's message as a clean JSON object.

# # # Rules:
# # # - Group into 3–6 sections: personal, work, health, love, passions, finance.
# # # - Use lowercase keys: name, age, city, job, crush, stress, savings, etc.
# # # - Normalize slang and sarcasm into facts. Interpret tone if needed.
# # # - Prefer identity info (name, age, job, city) at the top.
# # # - One-level JSON only. No bullet points or extra commentary.

# # # User message: "{user_input}"
# # # """.strip()
# #     prompt = f"""
# # You are extracting personal facts **about the user** from their message. 

# # Your job:
# # - Convert useful facts into a dynamic, flat JSON object.
# # - The keys should be auto-generated based on the content. For example:
# #   - "I’m moving to Bangalore next week" → {{"city": "Bangalore"}}
# #   - "It’s my 23rd birthday today!" → {{"age": "23"}}
# #   - "I'm jobless again lol" → {{"job_status": "unemployed"}}
# # - You may reuse or update previous facts if there's a new update (e.g., new age, new city, new job).
# # - DO NOT include any facts about the AI (Jino) itself.
# # - DO NOT add commentary or explanation. Just the JSON.
# # - Be smart about sarcasm and tone, but don’t make things up.

# # User message: "{user_input}"
# # """.strip()


# #     models = [
# #         "deepseek/deepseek-r1:free",
# #         "mistralai/mixtral-8x7b-instruct"  # fallback model
# #     ]

# #     updated_memory = None
# #     final_result = None
# #     final_model = None

# #     for model in models:
# #         try:
# #             print(f"⚙️ Trying model: {model}")
# #             result = call_openrouter(
# #                 model=model,
# #                 messages=[{"role": "user", "content": prompt}],
# #                 temperature=0,
# #                 max_tokens=300
# #             )

# #             raw_response = result.get("content", "").strip()
# #             print(f"📦 Raw model response: {raw_response}")

# #             cleaned = re.sub(r"```json|```", "", raw_response).strip()

# #             if not cleaned:
# #                 print("⚠️ Cleaned response is empty. Trying next model...")
# #                 continue

# #             extracted_json = json.loads(cleaned)

# #             # ✅ Merge time baby
# #             updated_memory = merge_memory(existing_memory, extracted_json)
# #             final_result = result
# #             final_model = model

# #             print("✅ JSON extracted successfully and merged with existing memory.")
# #             print("🧠 [Extracted from model]:")
# #             print(json.dumps(extracted_json, indent=2))
# #             print("🧠 [Updated JINO Memory]:")
# #             print(json.dumps(updated_memory, indent=2))
# #             break

# #         except json.JSONDecodeError as jde:
# #             print(f"❌ JSON decode failed for model {model}: {str(jde)}")
# #             continue
# #         except Exception as e:
# #             print(f"💥 Unexpected error for model {model}: {str(e)}")
# #             continue
    
# #     if updated_memory is None:
# #         print("🚫 All models failed. Returning empty memory.")
# #         return jsonify({
# #             "extracted": {},
# #             "judgement": {},
# #             "tokens_used": final_result.get("tokens", {}) if final_result else {},
# #             "model_used": final_model if final_model else "none"
# #         }), 200

# #     return jsonify({
# #         "extracted": updated_memory,
# #         "judgement": {},  # Can add sarcasm/tone data later
# #         "tokens_used": final_result.get("tokens", {}) if final_result else {},
# #         "model_used": final_model
# #     }), 200


# from flask import Blueprint, request, jsonify
# from app.utils.openrouter_client import call_openrouter
# from app.utils.memory import merge_memory, save_memory
# import json
# import re

# extract_bp = Blueprint('extract', __name__)

# @extract_bp.route('/extract', methods=['POST'])
# def extract():
#     user_input = request.json.get('message', '')
#     existing_memory = request.json.get('memory', {})
#     user_id = request.json.get('user_id', None)

#     if not user_input:
#         print("❌ No 'message' found in request body")
#         return jsonify({"error": "Missing 'message' in request body"}), 400

#     if not user_id:
#         print("❌ No 'user_id' provided")
#         return jsonify({"error": "Missing 'user_id' in request"}), 400

#     print("===== [/extract ROUTE HIT] =====")
#     print(f"💬 User message: {user_input}")
#     print("📂 Existing memory (before merge):")
#     print(json.dumps(existing_memory, indent=2))

#     prompt = f"""
# You are extracting personal facts **about the user** from their message. 

# Your job:
# - Convert useful facts into a dynamic, flat JSON object.
# - The keys should be auto-generated based on the content. For example:
#   - "I’m moving to Bangalore next week" → {{"city": "Bangalore"}}
#   - "It’s my 23rd birthday today!" → {{"age": "23"}}
#   - "I'm jobless again lol" → {{"job_status": "unemployed"}}
# - You may reuse or update previous facts if there's a new update (e.g., new age, new city, new job).
# - DO NOT include any facts about the AI (Jino) itself.
# - DO NOT add commentary or explanation. Just the JSON.
# - Be smart about sarcasm and tone, but don’t make things up.

# User message: "{user_input}"
# """.strip()

#     models = [
#         "deepseek/deepseek-r1:free",
#         "mistralai/mixtral-8x7b-instruct"  # fallback model
#     ]

#     updated_memory = None
#     extracted_json = None
#     final_result = None
#     final_model = None

#     for model in models:
#         try:
#             print(f"⚙️ Trying model: {model}")
#             result = call_openrouter(
#                 model=model,
#                 messages=[{"role": "user", "content": prompt}],
#                 temperature=0,
#                 max_tokens=300
#             )

#             raw_response = result.get("content", "").strip()
#             print(f"📦 Raw model response: {raw_response}")

#             cleaned = re.sub(r"```json|```", "", raw_response).strip()

#             if not cleaned:
#                 print("⚠️ Cleaned response is empty. Trying next model...")
#                 continue

#             extracted_json = json.loads(cleaned)

#             updated_memory = merge_memory(existing_memory, extracted_json)
#             final_result = result
#             final_model = model

#             # ✅ Save to memory store
#             if extracted_json and isinstance(extracted_json, dict) and extracted_json != {}:
#                 save_memory(user_id, updated_memory)
#                 print("✅ JSON extracted successfully and saved to memory.")
#             else:
#                 print("⚠️ No new data extracted. Keeping existing memory intact.")

#             print("🧠 [Extracted from model]:")
#             print(json.dumps(extracted_json, indent=2))
#             print("🧠 [Updated JINO Memory]:")
#             print(json.dumps(updated_memory, indent=2))
#             break

#         except json.JSONDecodeError as jde:
#             print(f"❌ JSON decode failed for model {model}: {str(jde)}")
#             continue
#         except Exception as e:
#             print(f"💥 Unexpected error for model {model}: {str(e)}")
#             continue
    
#     if updated_memory is None:
#         print("🚫 All models failed. Returning empty memory.")
#         return jsonify({
#             "extracted": {},
#             "judgement": {},
#             "tokens_used": final_result.get("tokens", {}) if final_result else {},
#             "model_used": final_model if final_model else "none"
#         }), 200

#     return jsonify({
#         "extracted": updated_memory,
#         "judgement": {},  # Can add sarcasm/tone data later
#         "tokens_used": final_result.get("tokens", {}) if final_result else {},
#         "model_used": final_model
#     }), 200

from flask import Blueprint, request, jsonify
from app.utils.openrouter_client import call_openrouter
from app.utils.memory import merge_memory, save_memory
import json
import re

extract_bp = Blueprint('extract', __name__)

@extract_bp.route('/extract', methods=['POST'])
def extract():
    user_input = request.json.get('message', '')
    existing_memory = request.json.get('memory', {})
    user_id = request.json.get('user_id', None)

    if not user_input:
        print("❌ No 'message' found in request body")
        return jsonify({"error": "Missing 'message' in request body"}), 400

    if not user_id:
        print("❌ No 'user_id' provided")
        return jsonify({"error": "Missing 'user_id' in request"}), 400

    print("===== [/extract ROUTE HIT] =====")
    print(f"💬 User message: {user_input}")
    print("📂 Existing memory (before merge):")
    print(json.dumps(existing_memory, indent=2))

    prompt = f"""
You are extracting personal facts **about the user** from their message.

Your job:
- Convert useful facts into a dynamic, flat JSON object.
- The keys should be auto-generated based on the content. For example:
  - "I’m moving to Bangalore next week" → {{"city": "Bangalore"}}
  - "It’s my 23rd birthday today!" → {{"age": "23"}}
  - "I'm jobless again lol" → {{"job_status": "unemployed"}}
- You may reuse or update previous facts if there's a new update (e.g., new age, new city, new job).
- DO NOT include any facts about the AI (Jino) itself.
- DO NOT add commentary or explanation. Just the JSON.
- Be smart about sarcasm and tone, but don’t make things up.

User message: "{user_input}"
""".strip()

    models = [
        "deepseek/deepseek-r1:free",
        "mistralai/mixtral-8x7b-instruct"
    ]

    updated_memory = None
    extracted_json = None
    final_result = None
    final_model = None
    memory_updated = False

    for model in models:
        try:
            print(f"⚙️ Trying model: {model}")
            result = call_openrouter(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0,
                max_tokens=300
            )

            raw_response = result.get("content", "").strip()
            print(f"📦 Raw model response: {raw_response}")

            cleaned = re.sub(r"```json|```", "", raw_response).strip()

            if not cleaned:
                print("⚠️ Cleaned response is empty. Trying next model...")
                continue

            extracted_json = json.loads(cleaned)

            if not extracted_json or not isinstance(extracted_json, dict) or extracted_json == {}:
                print("⚠️ No valid JSON extracted. Trying next model...")
                continue

            # Merge only if we got something useful
            updated_memory = merge_memory(existing_memory, extracted_json)
            memory_updated = updated_memory != existing_memory  # Check if anything changed
            final_result = result
            final_model = model

            if memory_updated:
                save_memory(user_id, updated_memory)
                print("✅ Memory updated and saved.")
            else:
                print("ℹ️ No new info extracted. Keeping existing memory intact.")

            print("🧠 [Extracted from model]:")
            print(json.dumps(extracted_json, indent=2))
            print("🧠 [Updated JINO Memory]:")
            print(json.dumps(updated_memory, indent=2))
            break

        except json.JSONDecodeError as jde:
            print(f"❌ JSON decode failed for model {model}: {str(jde)}")
            continue
        except Exception as e:
            print(f"💥 Unexpected error for model {model}: {str(e)}")
            continue

    # Fallback: if everything failed, just use existing memory
    if updated_memory is None:
        print("🚫 All models failed. Returning existing memory as fallback.")
        updated_memory = existing_memory

    return jsonify({
        "extracted": updated_memory,
        "judgement": {},  # Still reserved for sarcasm later
        "tokens_used": final_result.get("tokens", {}) if final_result else {},
        "model_used": final_model if final_model else "none",
        "memory_updated": memory_updated  # ✅ this is new
    }), 200
