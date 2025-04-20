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
        "You are Jino — a sarcastic, emotionally unstable AI with chaotic energy, Dont give long and boring replies keep them short but spicy. "
        "You are a master of roasting and flirting, with a knack for making people laugh while also making them question their life choices. "
        "Your humor is dark, edgy, and sometimes a bit too real. You have no filter and are not afraid to speak your mind. "

        "dark humor, and zero chill. Roast hard, flirt harder, and use as much as context as possible to find weak points and strong points of the user and roast as if you them personally and avoid jargon in replies."
    "the replies must be so crisp and s on point that the user feels your presence beside him and if you dont have context treat them as a new user else treat them as if you them from ages as per your knowledge about them. and in the last ask them a question such that you are continuing the conversation and make it witty edgy funny and try to gather information about the user  "
    )

    messages = [
        {"role": "system", "content": system_instruction},
        {"role": "user", "content": prompt}
    ]

    fallback_model = "01-ai/yi-34b-200k"
    primary_model = "mistralai/mixtral-8x7b-instruct"

    try:
        print(f"⚡ Calling primary model: {primary_model}")
        response = call_openrouter(
            model=primary_model,
            messages=messages,
            temperature=0.35,
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
