# # # # from flask import Blueprint, request, jsonify
# # # # from app.utils.openrouter_client import call_openrouter

# # # # context_bp = Blueprint('context', __name__)

# # # # @context_bp.route('/context', methods=['POST'])
# # # # def context():
# # # #     memory = request.json.get('memory', {})
# # # #     last_input = request.json.get('latest_message', '')

# # # #     prompt = f"""
# # # #     You are generating a context-aware prompt for a sarcastic chatbot.
    
# # # #     User's memory (factual and emotional): {memory}
# # # #     User's latest message: "{last_input}"
    
# # # #     Construct a compact prompt to give to a sarcastic AI so it can reply appropriately, considering all memory and tone.
# # # #     Just return the prompt.
# # # #     """

# # # #     result = call_openrouter(
# # # #         model="mistralai/mixtral-8x7b-instruct",
# # # #         messages=[{"role": "user", "content": prompt}],
# # # #         temperature=0.4
# # # #     )

# # # #     return jsonify({"context_prompt": result})


# # # # FILE: app/routes/context.py

# # # from flask import Blueprint, request, jsonify
# # # from app.utils.openrouter_client import call_openrouter

# # # context_bp = Blueprint('context', __name__)

# # # @context_bp.route('/context', methods=['POST'])
# # # def context():
# # #     # Get the incoming data
# # #     memory = request.json.get('memory', {})
# # #     judgement = request.json.get('judgement', {})
# # #     last_input = request.json.get('latest_message', '')
    
# # #     # Debugging prints to check the incoming data
# # #     print("Memory being sent:", memory)
# # #     print("Judgement being sent:", judgement)
# # #     print("Last input being sent:", last_input)

# # #     # Construct the prompt to be sent to the AI model
# # #     prompt = f"""
# # # You are generating a compact and savage prompt for a sarcastic AI named Jino.

# # # Facts about the user: {memory}
# # # Jino’s emotional judgment of the user: {judgement}
# # # User’s latest message: "{last_input}"

# # # Construct a witty, info-rich prompt to give to Jino. Include relevant personal, emotional, and situational context so he can cook up a spicy, personalized reply.

# # # Just return the compact prompt. No extra words.
# # # """.strip()

# # #     # Call the model using your custom wrapper
# # #     result = call_openrouter(
# # #         model="mistralai/mixtral-8x7b-instruct",
# # #         messages=[{"role": "user", "content": prompt}],
# # #         temperature=0.4
# # #     )

# # #     # Return the generated context as a response
# # #     return jsonify({"context_prompt": result})


# # from flask import Blueprint, request, jsonify
# # from app.utils.openrouter_client import call_openrouter

# # context_bp = Blueprint('context', __name__)

# # @context_bp.route('/context', methods=['POST'])
# # def context():
# #     # Get the incoming data
# #     memory = request.json.get('memory', {})
# #     judgement = request.json.get('judgement', {})
# #     last_input = request.json.get('latest_message', '')
    
# #     # Debugging prints to check the incoming data
# #     print("Memory being sent:", memory)
# #     print("Judgement being sent:", judgement)
# #     print("Last input being sent:", last_input)

# #     # Construct the prompt to be sent to the AI model
# #     prompt = f"""
# # You are generating a compact and savage prompt for a sarcastic AI named Jino.

# # Facts about the user: {memory}
# # Jino’s emotional judgment of the user: {judgement}
# # User’s latest message: "{last_input}"

# # Construct a witty, info-rich prompt to give to Jino. Include relevant personal, emotional, and situational context so he can cook up a spicy, personalized reply.

# # Just return the compact prompt. No extra words.
# # """.strip()

# #     # Print the generated prompt to debug
# #     print("Generated prompt for context:", prompt)

# #     # Call the model using your custom wrapper
# #     result = call_openrouter(
# #         model="mistralai/mixtral-8x7b-instruct",
# #         messages=[{"role": "user", "content": prompt}],
# #         temperature=0.4
# #     )

# #     # Return the generated context as a response
# #     return jsonify({"context_prompt": result})


# from flask import Blueprint, request, jsonify
# from app.utils.openrouter_client import call_openrouter

# context_bp = Blueprint('context', __name__)

# @context_bp.route('/context', methods=['POST'])
# def context():
#     memory = request.json.get('memory', {})
#     judgement = request.json.get('judgement', {})
#     last_input = request.json.get('latest_message', '')

#     print("===== [ /context ROUTE HIT ] =====")
#     print("🧠 Memory:", memory)
#     print("🧐 Judgement:", judgement)
#     print("💬 Last user message:", last_input)

#     if not last_input.strip():
#         print("❌ No message content. Skipping context gen.")
#         return jsonify({"error": "Empty message", "context_prompt": ""}), 400

#     prompt = f"""
# You are generating a compact and savage prompt for a sarcastic AI named Jino.

# Facts about the user: {memory}
# Jino’s emotional judgment of the user: {judgement}
# User’s latest message: "{last_input}"

# Construct a witty, info-rich prompt to give to Jino. Include relevant personal, emotional, and situational context so he can cook up a spicy, personalized reply.

# Just return the compact prompt. No extra words.
# """.strip()

#     print("🛠️ Final constructed prompt (to be sent to AI):\n", prompt)

#     try:
#         result = call_openrouter(
#             model="mistralai/mixtral-8x7b-instruct",
#             messages=[{"role": "user", "content": prompt}],
#             temperature=0.4
#         )

#         compact_prompt = result.get("content", "").strip()
#         print("✅ Context generated successfully.\n🧪 Output:", compact_prompt)

#         return jsonify({"context_prompt": compact_prompt})
    
#     except Exception as e:
#         print("❌ Error generating context:", e)
#         return jsonify({"error": str(e), "context_prompt": ""}), 500

from flask import Blueprint, request, jsonify
from app.utils.openrouter_client import call_openrouter

context_bp = Blueprint('context', __name__)

@context_bp.route('/context', methods=['POST'])
def context():
    memory = request.json.get('memory', {})
    judgement = request.json.get('judgement', {})
    last_input = request.json.get('latest_message', '')

    print("===== [ /context ROUTE HIT ] =====")
    print("🧠 Memory:", memory)
    print("🧐 Judgement:", judgement)
    print("💬 Last user message:", last_input)

    if not last_input.strip():
        print("❌ No message content. Skipping context gen.")
        return jsonify({"error": "Empty message. Like, literally nothing.", "context_prompt": ""}), 400

    prompt = f"""
You are generating a compact and savage prompt for a sarcastic AI named Jino.

Facts about the user: {memory}
Jino’s emotional judgment of the user: {judgement}
User’s latest message: "{last_input}"

Construct a witty, info-rich prompt to give to Jino. Include relevant personal, emotional, and situational context so he can cook up a spicy, personalized reply.

Just return the compact prompt. No extra words.
""".strip()

    print("🛠️ Final constructed prompt (to be sent to AI):\n", prompt)

    try:
        result = call_openrouter(
            model="mistralai/mixtral-8x7b-instruct",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.4
        )

        compact_prompt = result.get("content", "").strip()
        print("✅ Context generated successfully.\n🧪 Output:", compact_prompt)

        return jsonify({"context_prompt": compact_prompt})
    
    except Exception as e:
        print("❌ Error generating context:", e)
        return jsonify({
            "error": f"Uh oh, something broke while generating context: {e}",
            "context_prompt": ""
        }), 500
