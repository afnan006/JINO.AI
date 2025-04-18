# reply.py

from flask import Blueprint, request, jsonify
from app.utils.openrouter_client import call_openrouter
from openai import OpenAIError

reply_bp = Blueprint('reply', __name__)

@reply_bp.route('/reply', methods=['POST'])
def reply():
    prompt = request.json.get('prompt', '')

    print("===== [ /reply ROUTE HIT ] =====")
    print("📥 Prompt received in /reply:", repr(prompt))

    if not prompt.strip():
        print("❌ Empty prompt received. Something broke in the flow.")
        return jsonify({
            "reply": "Oops. Looks like I got ghosted by the context. Send that again?",
            "log": {
                "model": "none",
                "prompt_used": "none",
                "vibe": "confused and emotionally abandoned"
            }
        }), 400

    system_instruction = (
        "You are Jino — a sarcastic, emotionally unstable AI with chaotic energy, "
        "dark humor, and zero chill. Roast hard, flirt harder."
    )

    messages = [
        {"role": "system", "content": system_instruction},
        {"role": "user", "content": prompt}
    ]

    primary_model = "01-ai/yi-34b-200k"
    fallback_model = "mistralai/mixtral-8x7b-instruct"

    try:
        print(f"⚡ Calling primary model: {primary_model}")
        response = call_openrouter(
            model=primary_model,
            messages=messages,
            temperature=0.85
        )
        model_used = primary_model
    except OpenAIError as e:
        print(f"[ERROR] Primary model failed: {e}. Falling back to {fallback_model}")
        response = call_openrouter(
            model=fallback_model,
            messages=messages,
            temperature=0.85
        )
        model_used = fallback_model

    print(f"✅ Reply received from {model_used}: {response}")

    return jsonify({
        "reply": response.get("content", "No response content. Like, seriously?"),
        "log": {
            "model": model_used,
            "prompt_used": prompt,
            "vibe": "emotionally toxic, kinda sexy" if model_used == primary_model else "still spicy but on SSRIs"
        }
    })
