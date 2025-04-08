from flask import Blueprint, request, jsonify
from app.utils.openrouter_client import call_openrouter

reply_bp = Blueprint('reply', __name__)

@reply_bp.route('/reply', methods=['POST'])
def reply():
    prompt = request.json.get('prompt', '')

    system_instruction = "You are DudePool, an emotionally reactive, sarcastic AI with dark humor. Be witty, flirty, and a bit chaotic, but never boring."

    messages = [
        {"role": "system", "content": system_instruction},
        {"role": "user", "content": prompt}
    ]

    response = call_openrouter(
        model="01-ai/yi-34b-200k",
        messages=messages,
        temperature=0.85
    )

    return jsonify({
        "reply": response,
        "log": {
            "model": "01-ai/yi-34b-200k",
            "prompt_used": prompt,
            "vibe": "unfiltered and dangerously spicy"
        }
    })
