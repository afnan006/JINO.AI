from flask import Blueprint, request, jsonify
from app.utils.openrouter_client import call_openrouter

context_bp = Blueprint('context', __name__)

@context_bp.route('/context', methods=['POST'])
def context():
    memory = request.json.get('memory', {})
    last_input = request.json.get('latest_message', '')

    prompt = f"""
You are generating a context-aware prompt for a sarcastic chatbot.

User's memory (factual and emotional): {memory}
User's latest message: "{last_input}"

Construct a compact prompt to give to a sarcastic AI so it can reply appropriately, considering all memory and tone.
Just return the prompt.
    """

    result = call_openrouter(
        model="mistralai/mixtral-8x7b-instruct",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )

    return jsonify({"context_prompt": result})
