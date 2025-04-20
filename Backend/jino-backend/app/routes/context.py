# # # # # # # # context.py
# # # # # # # from flask import Blueprint, request, jsonify
# # # # # # # from app.utils.openrouter_client import call_openrouter

# # # # # # # context_bp = Blueprint('context', __name__)

# # # # # # # @context_bp.route('/context', methods=['POST'])
# # # # # # # def context():
# # # # # # #     memory = request.json.get('memory', {})
# # # # # # #     judgement = request.json.get('judgement', {})
# # # # # # #     last_input = request.json.get('latest_message', '')

# # # # # # #     print("===== [ /context ROUTE HIT ] =====")
# # # # # # #     print("🧠 Memory:", memory)
# # # # # # #     print("🧐 Judgement:", judgement)
# # # # # # #     print("💬 Last user message:", last_input)

# # # # # # #     if not last_input.strip():
# # # # # # #         print("❌ No message content. Skipping context gen.")
# # # # # # #         return jsonify({"error": "Empty message. Like, literally nothing.", "context_prompt": ""}), 400

# # # # # # #     prompt = f"""
# # # # # # # You are generating a compact and savage prompt for a sarcastic AI named Jino.

# # # # # # # Facts about the user: {memory}
# # # # # # # Jino’s emotional judgment of the user: {judgement}
# # # # # # # User’s latest message: "{last_input}"

# # # # # # # Construct a witty, info-rich prompt to give to Jino. Include relevant personal, emotional, and situational context so he can cook up a spicy, personalized reply.

# # # # # # # Just return the compact prompt. No extra words.
# # # # # # # """.strip()

# # # # # # #     print("🛠️ Final constructed prompt (to be sent to AI):\n", prompt)

# # # # # # #     try:
# # # # # # #         result = call_openrouter(
# # # # # # #             model="mistralai/mixtral-8x7b-instruct",
# # # # # # #             messages=[{"role": "user", "content": prompt}],
# # # # # # #             temperature=0.4
# # # # # # #         )

# # # # # # #         compact_prompt = result.get("content", "").strip()
# # # # # # #         print("✅ Context generated successfully.\n🧪 Output:", compact_prompt)

# # # # # # #         return jsonify({"context_prompt": compact_prompt})
    
# # # # # # #     except Exception as e:
# # # # # # #         print("❌ Error generating context:", e)
# # # # # # #         return jsonify({
# # # # # # #             "error": f"Uh oh, something broke while generating context: {e}",
# # # # # # #             "context_prompt": ""
# # # # # # #         }), 500







# # # # # # from flask import Blueprint, request, jsonify
# # # # # # from app.utils.openrouter_client import call_openrouter

# # # # # # context_bp = Blueprint('context', __name__)

# # # # # # @context_bp.route('/context', methods=['POST'])
# # # # # # def context():
# # # # # #     memory = request.json.get('memory', {})
# # # # # #     judgement = request.json.get('judgement', {})
# # # # # #     last_input = request.json.get('latest_message', '')

# # # # # #     print("===== [ /context ROUTE HIT ] =====")
# # # # # #     print("🧠 Memory:", memory)
# # # # # #     print("🧐 Judgement:", judgement)
# # # # # #     print("💬 Last user message:", last_input)

# # # # # #     if not last_input.strip():
# # # # # #         print("❌ No message content. Skipping context gen.")
# # # # # #         return jsonify({"error": "Empty message. Like, literally nothing.", "context_prompt": ""}), 400

# # # # # #     prompt = f"""
# # # # # # You are generating a compact and savage prompt for a sarcastic AI named Jino.

# # # # # # Facts about the user: {memory}
# # # # # # Jino’s emotional judgment of the user: {judgement}
# # # # # # User’s latest message: "{last_input}"

# # # # # # Construct a witty, info-rich prompt to give to Jino and use the users last message to answer accordingly dont reply bullshit. Include relevant personal, emotional, and situational context so he can cook up a spicy, personalized reply.

# # # # # # Just return the compact prompt. No extra words.
# # # # # # """.strip()

# # # # # #     print("🛠️ Final constructed prompt (to be sent to AI):\n", prompt)

# # # # # #     try:
# # # # # #         result = call_openrouter(
# # # # # #             model="mistralai/mixtral-8x7b-instruct",
# # # # # #             messages=[{"role": "user", "content": prompt}],
# # # # # #             temperature=0.4
# # # # # #         )

# # # # # #         compact_prompt = result.get("content", "").strip()
# # # # # #         print("✅ Context generated successfully.\n🧪 Output:", compact_prompt)

# # # # # #         return jsonify({"context_prompt": compact_prompt})
    
# # # # # #     except Exception as e:
# # # # # #         print("❌ Error generating context:", e)
# # # # # #         return jsonify({
# # # # # #             "error": f"Uh oh, something broke while generating context: {e}",
# # # # # #             "context_prompt": ""
# # # # # #         }), 500


# # # # # from flask import Blueprint, request, jsonify
# # # # # from app.utils.openrouter_client import call_openrouter
# # # # # from datetime import datetime

# # # # # context_bp = Blueprint('context', __name__)

# # # # # @context_bp.route('/context', methods=['POST'])
# # # # # def context():
# # # # #     memory = request.json.get('memory', {})
# # # # #     judgement = request.json.get('judgement', {})
# # # # #     last_input = request.json.get('latest_message', '')

# # # # #     print("===== [ /context ROUTE HIT ] =====")
# # # # #     print("🧠 Memory:", memory)
# # # # #     print("🧐 Judgement:", judgement)
# # # # #     print("💬 Last user message:", last_input)

# # # # #     if not last_input.strip():
# # # # #         print("❌ No message content. Skipping context gen.")
# # # # #         return jsonify({"error": "Empty message. Like, literally nothing.", "context_prompt": ""}), 400

# # # # #     # === Judgement Slimming: Keep only last 3 judgments per chat ===
# # # # #     slimmed_judgement = {}
# # # # #     for chat_id, entries in judgement.items():
# # # # #         if isinstance(entries, list):
# # # # #             sorted_entries = sorted(entries, key=lambda x: x.get('timestamp', ''), reverse=True)
# # # # #             slimmed_judgement[chat_id] = sorted_entries[:3]

# # # # #     # === Soft small-talk detection (for prompt enhancement only, not control) ===
# # # # #     small_talk_detected = False
# # # # #     small_talk_triggers = ["how are you", "what’s up", "what's up", "do you remember", "remember me", "miss me"]
# # # # #     lowered_input = last_input.lower()

# # # # #     for phrase in small_talk_triggers:
# # # # #         if phrase in lowered_input:
# # # # #             small_talk_detected = True
# # # # #             break

# # # # #     # === Prompt enhancement zone ===
# # # # #     enhancement = ""
# # # # #     if small_talk_detected:
# # # # #         enhancement = (
# # # # #             "The user seems to be casually checking in or trying to connect. "
# # # # #             "Start your reply by briefly acknowledging the greeting or recognition before going full roast mode."
# # # # #         )

# # # # #     prompt = f"""
# # # # # You are generating a compact and savage prompt for a sarcastic AI named Jino.

# # # # # Facts about the user: {memory}
# # # # # Jino’s emotional judgment of the user: {slimmed_judgement}
# # # # # User’s latest message: "{last_input}"

# # # # # {enhancement}

# # # # # Construct a witty, info-rich prompt to give to Jino. Use the user's latest message meaningfully.
# # # # # Incorporate emotional tone and relevant facts, but don't be generic. This AI has a personality – make it spicy and personal.

# # # # # Only return the final prompt for Jino. No headers, no fluff, just the compact spicy context.
# # # # # """.strip()

# # # # #     print("🛠️ Final constructed prompt (to be sent to AI):\n", prompt)

# # # # #     try:
# # # # #         result = call_openrouter(
# # # # #             model="mistralai/mixtral-8x7b-instruct",
# # # # #             messages=[{"role": "user", "content": prompt}],
# # # # #             temperature=0.4
# # # # #         )

# # # # #         compact_prompt = result.get("content", "").strip()
# # # # #         print("✅ Context generated successfully.\n🧪 Output:", compact_prompt)

# # # # #         return jsonify({"context_prompt": compact_prompt})

# # # # #     except Exception as e:
# # # # #         print("❌ Error generating context:", e)
# # # # #         return jsonify({
# # # # #             "error": f"Uh oh, something broke while generating context: {e}",
# # # # #             "context_prompt": ""
# # # # #         }), 500





# # # # from flask import Blueprint, request, jsonify
# # # # from app.utils.openrouter_client import call_openrouter

# # # # context_bp = Blueprint('context', __name__)

# # # # @context_bp.route('/context', methods=['POST'])
# # # # def context():
# # # #     try:
# # # #         data = request.json or {}
# # # #         memory = data.get('memory', {})
# # # #         judgement = data.get('judgement', {})
# # # #         last_input = data.get('latest_message', '').strip()
# # # #         chat_id = data.get('chat_id', None)

# # # #         print("\n===== [ /context ROUTE HIT ] =====")
# # # #         print("🧠 Memory:", memory)
# # # #         print("🧐 Judgement:", judgement)
# # # #         print("💬 Last user message:", last_input)

# # # #         if not last_input:
# # # #             print("❌ No message content. Skipping context gen.")
# # # #             return jsonify({
# # # #                 "error": "Empty message. Like, literally nothing.",
# # # #                 "context_prompt": ""
# # # #             }), 400

# # # #         # === JUDGEMENT SLIMMING ===
# # # #         slimmed_judgement = ""
# # # #         try:
# # # #             # Case 1: New format with chat_id -> list of judgements
# # # #             if chat_id and isinstance(judgement.get(chat_id), list):
# # # #                 sorted_entries = sorted(judgement[chat_id], key=lambda x: x.get('timestamp', ''), reverse=True)
# # # #                 latest = sorted_entries[0] if sorted_entries else {}
# # # #                 slimmed_judgement = f"{latest.get('judgement', 'Unknown')}, Confidence: {latest.get('confidence', 'N/A')}"

# # # #             # Case 2: Old flat format (single judgement dict)
# # # #             elif isinstance(judgement, dict) and "judgement" in judgement:
# # # #                 slimmed_judgement = f"{judgement.get('judgement', 'Unknown')}, Confidence: {judgement.get('confidence', 'N/A')}"

# # # #             else:
# # # #                 slimmed_judgement = "No emotional read available. Jino is confused."

# # # #         except Exception as e:
# # # #             print("⚠️ Error slimming judgement:", e)
# # # #             slimmed_judgement = "Judgement data was a hot mess."

# # # #         # === SMALL TALK ENHANCEMENT CHECK ===
# # # #         small_talk_triggers = [
# # # #             "how are you", "what’s up", "what's up", 
# # # #             "do you remember", "remember me", "miss me"
# # # #         ]
# # # #         small_talk_detected = any(phrase in last_input.lower() for phrase in small_talk_triggers)

# # # #         enhancement = ""
# # # #         if small_talk_detected:
# # # #             enhancement = (
# # # #                 "The user seems to be casually checking in or trying to connect. "
# # # #                 "Start your reply by briefly acknowledging the greeting or recognition before going full roast mode."
# # # #             )

# # # #         # === FINAL PROMPT BUILDING ===
# # # #         prompt = f"""
# # # # You are generating a compact and savage prompt for a sarcastic AI named Jino.

# # # # Facts about the user: {memory}
# # # # Jino’s emotional judgment of the user: {slimmed_judgement}
# # # # User’s latest message: "{last_input}"

# # # # {enhancement}

# # # # Construct a witty, info-rich prompt to give to Jino. Use the user's latest message meaningfully. Use only memory and facts to reply to the user and use the users last message to answer accordingly dont reply bullshit, use their words back to them and fun of them.
# # # # Incorporate emotional tone and relevant facts, but don't be generic. This AI has a personality – make it spicy and personal.

# # # # Only return the final prompt for Jino. No headers, no fluff, just the compact spicy context.
# # # # """.strip()

# # # #         print("🛠️ Final constructed prompt:\n", prompt)

# # # #         # === CALL AI ===
# # # #         result = call_openrouter(
# # # #             model="mistralai/mixtral-8x7b-instruct",
# # # #             messages=[{"role": "user", "content": prompt}],
# # # #             temperature=0.4
# # # #         )

# # # #         compact_prompt = result.get("content", "").strip()

# # # #         print("✅ Context generated successfully.")
# # # #         print("🧪 Output:\n", compact_prompt)

# # # #         return jsonify({"context_prompt": compact_prompt})

# # # #     except Exception as e:
# # # #         print("🔥 UNHANDLED ERROR in /context:", e)
# # # #         return jsonify({
# # # #             "error": f"Something broke while generating context: {str(e)}",
# # # #             "context_prompt": ""
# # # #         }), 500


# # # from flask import Blueprint, request, jsonify
# # # from app.utils.openrouter_client import call_openrouter

# # # context_bp = Blueprint('context', __name__)

# # # @context_bp.route('/context', methods=['POST'])
# # # def context():
# # #     try:
# # #         data = request.json or {}
# # #         memory = data.get('memory', {})
# # #         judgement = data.get('judgement', {})
# # #         last_input = data.get('latest_message', '').strip()
# # #         chat_id = data.get('chat_id', None)

# # #         print("\n===== [ /context ROUTE HIT ] =====")
# # #         print("🧠 Memory:", memory)
# # #         print("🧐 Judgement:", judgement)
# # #         print("💬 Last user message:", last_input)

# # #         if not last_input:
# # #             print("❌ No message content. Skipping context gen.")
# # #             return jsonify({
# # #                 "error": "Empty message. Like, literally nothing.",
# # #                 "context_prompt": ""
# # #             }), 400

# # #         # === JUDGEMENT SLIMMING ===
# # #         slimmed_judgement = ""
# # #         try:
# # #             if chat_id and isinstance(judgement.get(chat_id), list):
# # #                 sorted_entries = sorted(judgement[chat_id], key=lambda x: x.get('timestamp', ''), reverse=True)
# # #                 latest = sorted_entries[0] if sorted_entries else {}
# # #                 slimmed_judgement = f"{latest.get('judgement', 'Unknown')}, Confidence: {latest.get('confidence', 'N/A')}"
# # #             elif isinstance(judgement, dict) and "judgement" in judgement:
# # #                 slimmed_judgement = f"{judgement.get('judgement', 'Unknown')}, Confidence: {judgement.get('confidence', 'N/A')}"
# # #             else:
# # #                 slimmed_judgement = "No emotional read available. Jino is confused."
# # #         except Exception as e:
# # #             print("⚠️ Error slimming judgement:", e)
# # #             slimmed_judgement = "Judgement data was a hot mess."

# # #         # === SMALL TALK ENHANCEMENT CHECK ===
# # #         small_talk_triggers = [
# # #             "how are you", "what’s up", "what's up", 
# # #             "do you remember", "remember me", "miss me"
# # #         ]
# # #         small_talk_detected = any(phrase in last_input.lower() for phrase in small_talk_triggers)

# # #         enhancement = ""
# # #         if small_talk_detected:
# # #             enhancement = (
# # #                 "Looks like the user is casually trying to reconnect or bait Jino. "
# # #                 "Make sure the message acknowledges this before clapping back sarcastically."
# # #             )

# # #         # === NEW STYLE PROMPT: ACT LIKE THE USER ===
# # #         prompt = f"""
# # # You are generating a message AS THE USER — not describing them — based on their memory, emotional judgment, and their most recent message. The output should feel like the user is chatting directly with Jino, with sass and emotion.

# # # Details you have:
# # # - Memory (factual details about user): {memory}
# # # - Judgement (Jino's emotional view of user): {slimmed_judgement}
# # # - Latest user message: "{last_input}"

# # # {enhancement}

# # # Now, using all of this, write a message **from the user’s point of view**, as if they’re replying to Jino. Include all the petty details from memory and judgment, make it sarcastic, casual, unfiltered, and spicy.

# # # Be dramatic about tiny things like spelling mistakes, timestamps, cringe life choices, whatever. This should feel like the user is dragging their own life through the mud while yelling at Jino for being judgmental.

# # # Make it personal and chaotic but informative. You are NOT replying as Jino — you are setting up Jino with the ultimate context to roast back.

# # # Only return the final message as if written by the user. No explanation. No framing. No narration.
# # # """.strip()

# # #         print("🛠️ Final constructed prompt:\n", prompt)

# # #         # === CALL AI ===
# # #         result = call_openrouter(
# # #             model="mistralai/mixtral-8x7b-instruct",
# # #             messages=[{"role": "user", "content": prompt}],
# # #             temperature=0.4
# # #         )

# # #         compact_prompt = result.get("content", "").strip()

# # #         print("✅ Context generated successfully.")
# # #         print("🧪 Output:\n", compact_prompt)

# # #         return jsonify({"context_prompt": compact_prompt})

# # #     except Exception as e:
# # #         print("🔥 UNHANDLED ERROR in /context:", e)
# # #         return jsonify({
# # #             "error": f"Something broke while generating context: {str(e)}",
# # #             "context_prompt": ""
# # #         }), 500



# # from flask import Blueprint, request, jsonify
# # from app.utils.openrouter_client import call_openrouter

# # context_bp = Blueprint('context', __name__)

# # @context_bp.route('/context', methods=['POST'])
# # def context():
# #     try:
# #         data = request.json or {}
# #         memory = data.get('memory', {})
# #         judgement = data.get('judgement', {})
# #         last_input = data.get('latest_message', '').strip()
# #         convo_summary = data.get('convo_summary', {})  # 🧠 NEW STUFF
# #         chat_id = data.get('chat_id', None)

# #         print("\n===== [ /context ROUTE HIT ] =====")
# #         print("🧠 Memory:", memory)
# #         print("🧐 Judgement:", judgement)
# #         print("💬 Last user message:", last_input)
# #         print("🧾 Convo Summary:", convo_summary)  # Log the new input

# #         if not last_input:
# #             print("❌ No message content. Skipping context gen.")
# #             return jsonify({
# #                 "error": "Empty message. Like, literally nothing.",
# #                 "context_prompt": ""
# #             }), 400

# #         # === JUDGEMENT SLIMMING ===
# #         slimmed_judgement = ""
# #         try:
# #             if chat_id and isinstance(judgement.get(chat_id), list):
# #                 sorted_entries = sorted(judgement[chat_id], key=lambda x: x.get('timestamp', ''), reverse=True)
# #                 latest = sorted_entries[0] if sorted_entries else {}
# #                 slimmed_judgement = f"{latest.get('judgement', 'Unknown')}, Confidence: {latest.get('confidence', 'N/A')}"
# #             elif isinstance(judgement, dict) and "judgement" in judgement:
# #                 slimmed_judgement = f"{judgement.get('judgement', 'Unknown')}, Confidence: {judgement.get('confidence', 'N/A')}"
# #             else:
# #                 slimmed_judgement = "No emotional read available. Jino is confused."
# #         except Exception as e:
# #             print("⚠️ Error slimming judgement:", e)
# #             slimmed_judgement = "Judgement data was a hot mess."

# #         # === SMALL TALK ENHANCEMENT CHECK ===
# #         small_talk_triggers = [
# #             "how are you", "what’s up", "what's up", 
# #             "do you remember", "remember me", "miss me"
# #         ]
# #         small_talk_detected = any(phrase in last_input.lower() for phrase in small_talk_triggers)

# #         enhancement = ""
# #         if small_talk_detected:
# #             enhancement = (
# #                 "Looks like the user is casually trying to reconnect or bait Jino. "
# #                 "Make sure the message acknowledges this before clapping back sarcastically."
# #             )

# #         # === CONVO SUMMARY ADDITION ===
# #         convo_summary_text = ""
# #         if isinstance(convo_summary, dict) and convo_summary.get("summary"):
# #             convo_summary_text = f"\n- Convo Summary (last few messages): {convo_summary['summary']}"
# #             if convo_summary.get("latest_timestamp"):
# #                 convo_summary_text += f" [Last seen at: {convo_summary['latest_timestamp']}]"

# #         # === FINAL PROMPT ===
# #         prompt = f"""
# # You are generating a message AS THE USER — not describing them — based on their memory, emotional judgment, and their most recent message. The output should feel like the user is chatting directly with Jino, with sass and emotion.

# # Details you have:
# # - Memory (factual details about user): {memory}
# # - Judgement (Jino's emotional view of user): {slimmed_judgement}
# # - Latest user message: "{last_input}"
# # {convo_summary_text}
# # {enhancement}

# # Now, using all of this, write a message **from the user’s point of view**, as if they’re replying to Jino. Include all the petty details from memory and judgment, make it sarcastic, casual, unfiltered, and spicy.

# # Be dramatic about tiny things like spelling mistakes, timestamps, cringe life choices, whatever. This should feel like the user is dragging their own life through the mud while yelling at Jino for being judgmental.

# # Make it personal and chaotic but informative. You are NOT replying as Jino — you are setting up Jino with the ultimate context to roast back.

# # Only return the final message as if written by the user. No explanation. No framing. No narration.
# # """.strip()

# #         print("🛠️ Final constructed prompt:\n", prompt)

# #         # === CALL AI ===
# #         result = call_openrouter(
# #             model="mistralai/mixtral-8x7b-instruct",
# #             messages=[{"role": "user", "content": prompt}],
# #             temperature=0.4
# #         )

# #         compact_prompt = result.get("content", "").strip()

# #         print("✅ Context generated successfully.")
# #         print("🧪 Output:\n", compact_prompt)

# #         return jsonify({"context_prompt": compact_prompt})

# #     except Exception as e:
# #         print("🔥 UNHANDLED ERROR in /context:", e)
# #         return jsonify({
# #             "error": f"Something broke while generating context: {str(e)}",
# #             "context_prompt": ""
# #         }), 500

# from flask import Blueprint, request, jsonify
# from app.utils.openrouter_client import call_openrouter

# context_bp = Blueprint('context', __name__)

# @context_bp.route('/context', methods=['POST'])
# def context():
#     try:
#         # Step 1: Retrieve data from the request
#         data = request.json or {}
#         memory = data.get('memory', {})
#         judgement = data.get('judgement', {})
#         last_input = data.get('latest_message', '').strip()
#         convo_summary = data.get('convo_summary', {})  # 🧠 NEW STUFF
#         chat_id = data.get('chat_id', None)

#         print("\n===== [ /context ROUTE HIT ] =====")
#         print("🧠 Memory:", memory)
#         print("🧐 Judgement:", judgement)
#         print("💬 Last user message:", last_input)
#         print("🧾 Convo Summary:", convo_summary)  # Log the new input

#         # Check if the last input exists
#         if not last_input:
#             print("❌ No message content. Skipping context gen.")
#             return jsonify({
#                 "error": "Empty message. Like, literally nothing.",
#                 "context_prompt": ""
#             }), 400

#         # Step 2: Handle Judgement data (Improve error handling here)
#         slimmed_judgement = ""
#         try:
#             if chat_id and isinstance(judgement.get(chat_id), list):
#                 sorted_entries = sorted(judgement[chat_id], key=lambda x: x.get('timestamp', ''), reverse=True)
#                 latest = sorted_entries[0] if sorted_entries else {}
#                 slimmed_judgement = f"{latest.get('judgement', 'Unknown')}, Confidence: {latest.get('confidence', 'N/A')}"
#             elif isinstance(judgement, dict) and "judgement" in judgement:
#                 slimmed_judgement = f"{judgement.get('judgement', 'Unknown')}, Confidence: {judgement.get('confidence', 'N/A')}"
#             else:
#                 slimmed_judgement = "No emotional read available. Jino is confused."
#         except Exception as e:
#             print("⚠️ Error slimming judgement:", e)
#             slimmed_judgement = "Judgement data was a hot mess."

#         # Step 3: Check for small talk triggers in last_input (if any)
#         small_talk_triggers = [
#             "how are you", "what’s up", "what's up", 
#             "do you remember", "remember me", "miss me"
#         ]
#         small_talk_detected = any(phrase in last_input.lower() for phrase in small_talk_triggers)

#         enhancement = ""
#         if small_talk_detected:
#             enhancement = (
#                 "Looks like the user is casually trying to reconnect or bait Jino. "
#                 "Make sure the message acknowledges this before clapping back sarcastically."
#             )

#         # Step 4: Handle Convo Summary (Log this part carefully)
#         convo_summary_text = ""
#         if isinstance(convo_summary, dict) and convo_summary.get("summary"):
#             convo_summary_text = f"\n- Convo Summary (last few messages): {convo_summary['summary']}"
#             if convo_summary.get("latest_timestamp"):
#                 convo_summary_text += f" [Last seen at: {convo_summary['latest_timestamp']}]"

#         # Step 5: Construct the final prompt for AI generation
#         prompt = f"""
# You are generating a message AS THE USER — not describing them — based on their memory, emotional judgment, and their most recent message. The output should feel like the user is chatting directly with Jino, with sass and emotion.

# Details you have:
# - Memory (factual details about user): {memory}
# - Judgement (Jino's emotional view of user): {slimmed_judgement}
# - Latest user message: "{last_input}"
# {convo_summary_text}
# {enhancement}

# Now, using all of this, write a message **from the user’s point of view**, as if they’re replying to Jino. Include all the petty details from memory and judgment, make it sarcastic, casual, unfiltered, and spicy.

# Be dramatic about tiny things like spelling mistakes, timestamps, cringe life choices, whatever. This should feel like the user is dragging their own life through the mud while yelling at Jino for being judgmental.

# Make it personal and chaotic but informative. You are NOT replying as Jino — you are setting up Jino with the ultimate context to roast back.

# Only return the final message as if written by the user. No explanation. No framing. No narration.
# """.strip()

#         print("🛠️ Final constructed prompt:\n", prompt)

#         # Step 6: Call the AI to generate the response
#         try:
#             result = call_openrouter(
#                 model="mistralai/mixtral-8x7b-instruct",
#                 messages=[{"role": "user", "content": prompt}],
#                 temperature=0.4
#             )
#             compact_prompt = result.get("content", "").strip()

#             print("✅ Context generated successfully.")
#             print("🧪 Output:\n", compact_prompt)

#             # Step 7: Return the final response
#             return jsonify({"context_prompt": compact_prompt})
        
#         except Exception as ai_error:
#             print("⚠️ AI Model Call Error:", ai_error)
#             return jsonify({
#                 "error": f"Failed to generate context with the model: {str(ai_error)}",
#                 "context_prompt": ""
#             }), 500

#     except Exception as e:
#         print("🔥 UNHANDLED ERROR in /context:", e)
#         return jsonify({
#             "error": f"Something broke while generating context: {str(e)}",
#             "context_prompt": ""
#         }), 500


from flask import Blueprint, request, jsonify
from app.utils.openrouter_client import call_openrouter

context_bp = Blueprint('context', __name__)

@context_bp.route('/context', methods=['POST'])
def context():
    try:
        # Step 1: Retrieve data from the request
        data = request.json or {}
        memory = data.get('memory', {})
        judgement = data.get('judgement', {})
        last_input = data.get('latest_message', '').strip()
        convo_summary = data.get('convo_summary', {})  # 🧠 NEW STUFF
        chat_id = data.get('chat_id', None)

        print("\n===== [ /context ROUTE HIT ] =====")
        print("🧠 Memory:", memory)
        print("🧐 Judgement:", judgement)
        print("💬 Last user message:", last_input)
        print("🧾 Convo Summary:", convo_summary)  # Log the new input

        # Check if the last input exists
        if not last_input:
            print("❌ No message content. Skipping context gen.")
            return jsonify({
                "error": "Empty message. Like, literally nothing.",
                "context_prompt": ""
            }), 400

        # Step 2: Handle Judgement data (Improve error handling here)
        slimmed_judgement = ""
        try:
            if chat_id and isinstance(judgement.get(chat_id), list):
                sorted_entries = sorted(judgement[chat_id], key=lambda x: x.get('timestamp', ''), reverse=True)
                latest = sorted_entries[0] if sorted_entries else {}
                slimmed_judgement = f"{latest.get('judgement', 'Unknown')}, Confidence: {latest.get('confidence', 'N/A')}"
            elif isinstance(judgement, dict) and "judgement" in judgement:
                slimmed_judgement = f"{judgement.get('judgement', 'Unknown')}, Confidence: {judgement.get('confidence', 'N/A')}"
            else:
                slimmed_judgement = "No emotional read available. Jino is confused."
        except Exception as e:
            print("⚠️ Error slimming judgement:", e)
            slimmed_judgement = "Judgement data was a hot mess."

        # Step 3: Check for small talk triggers in last_input (if any)
        small_talk_triggers = [
            "how are you", "what’s up", "what's up", 
            "do you remember", "remember me", "miss me"
        ]
        small_talk_detected = any(phrase in last_input.lower() for phrase in small_talk_triggers)

        enhancement = ""
        if small_talk_detected:
            enhancement = (
                "Looks like the user is casually trying to reconnect or bait Jino. "
                "Make sure the message acknowledges this before clapping back sarcastically."
            )

        # Step 4: Handle Convo Summary (Log this part carefully)
        convo_summary_text = ""
        if isinstance(convo_summary, dict) and convo_summary.get("summary"):
            convo_summary_text = f"\n- Convo Summary (last few messages): {convo_summary['summary']}"
            if convo_summary.get("latest_timestamp"):
                convo_summary_text += f" [Last seen at: {convo_summary['latest_timestamp']}]"

        # Step 5: Construct the final prompt for AI generation
        prompt = f"""
You are generating a message AS THE USER — not describing them — based on their memory, emotional judgment, and their most recent message. The output should feel like the user is chatting directly with Jino, with sass and emotion.

Details you have:
- Memory (factual details about user): {memory}
- Judgement (Jino's emotional view of user): {slimmed_judgement}
- Latest user message: "{last_input}"
{convo_summary_text}
{enhancement}

Now, using all of this, write a message **from the user’s point of view**, as if they’re replying to Jino. Include all the petty details from memory and judgment, make it sarcastic, casual, unfiltered, and spicy.

Be dramatic about tiny things like spelling mistakes, timestamps, cringe life choices, whatever. This should feel like the user is dragging their own life through the mud while yelling at Jino for being judgmental.

Make it personal and chaotic but informative. You are NOT replying as Jino — you are setting up Jino with the ultimate context to roast back.

Only return the final message as if written by the user. No explanation. No framing. No narration.
""".strip()

        print("🛠️ Final constructed prompt:\n", prompt)

        # Step 6: Call the AI to generate the response
        try:
            result = call_openrouter(
                model="mistralai/mixtral-8x7b-instruct",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.4
            )
            compact_prompt = result.get("content", "").strip()

            print("✅ Context generated successfully.")
            print("🧪 Output:\n", compact_prompt)

            # Step 7: Return the final response
            return jsonify({"context_prompt": compact_prompt})
        
        except Exception as ai_error:
            print("⚠️ AI Model Call Error:", ai_error)
            return jsonify({
                "error": f"Failed to generate context with the model: {str(ai_error)}",
                "context_prompt": ""
            }), 500

    except Exception as e:
        print("🔥 UNHANDLED ERROR in /context:", e)
        return jsonify({
            "error": f"Something broke while generating context: {str(e)}",
            "context_prompt": ""
        }), 500
