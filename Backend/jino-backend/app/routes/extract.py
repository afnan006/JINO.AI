from flask import Blueprint, request, jsonify
from app.utils.openrouter_client import call_openrouter
import json
import re

extract_bp = Blueprint('extract', __name__)

@extract_bp.route('/extract', methods=['POST'])
def extract():
    user_input = request.json.get('message', '')

    if not user_input:
        return jsonify({"error": "Missing 'message' in request body"}), 400

    prompt = prompt = f"""
Extract personal facts from the user's message as a clean JSON object.

Rules:
- Group into 3–6 broad sections: personal, work, health, love, passions, finance.
- Inside each section, use short lowercase keys: name, age, city, job, crush, sleep, savings, etc.
- Focus on identity info first (name, age, job, city) — these go top of JSON.
- Keep values clear, short, and normalized. Don’t copy user’s exact slang.
- Interpret sarcasm, slang, and emotional tone — rewrite them into real facts.
- Capture time references like “for 2 years” or “since 2020”.
- No summaries, no bullet points. Just flat clean JSON. One level. No explanations.

User message: "{user_input}"
""".strip()

    models = [
        "deepseek/deepseek-r1:free",
        "mistralai/mixtral-8x7b-instruct"  # fallback
    ]

    for model in models:
        try:
            print(f"🔥 Trying model: {model}")
            result = call_openrouter(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0,
                max_tokens=300
            )

            raw_response = result.get("content", "").strip()
            token_data = result.get("tokens", {})

            print("\n📦 RAW RESPONSE:\n", raw_response)

            # Clean markdown wrappers if any
            cleaned = re.sub(r"```json|```", "", raw_response).strip()

            if not cleaned:
                print(f"⚠️ Model '{model}' gave empty response.")
                continue  # Try next model

            extracted_json = json.loads(cleaned)

            return jsonify({
                "extracted": extracted_json,
                "tokens_used": token_data,
                "model_used": model
            }), 200

        except json.JSONDecodeError:
            print(f"❌ JSON parsing failed from model '{model}':\n{raw_response}")
            continue  # Try next model

        except Exception as e:
            print(f"💥 Error using model '{model}': {e}")
            continue  # Try next

    return jsonify({
        "error": "Extraction failed. All models gave up or returned junk.",
        "raw_response": raw_response
    }), 500
