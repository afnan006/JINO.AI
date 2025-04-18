# extract.py
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
