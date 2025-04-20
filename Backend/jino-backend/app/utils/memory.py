# # app/utils/memory.py

import json
import os
import copy


def clean_invalid_fields(memory):
    cleaned_memory = {}
    for key, value in memory.items():
        if value and value != "not provided":
            cleaned_memory[key] = value
    return cleaned_memory

# def merge_memory(old, new):
#     if not isinstance(old, dict):
#         old = {}
#     if not isinstance(new, dict):
#         new = {}
    
#     new = clean_invalid_fields(new)
#     old.update(new)
#     return old

def merge_memory(old, new):
    if not isinstance(old, dict):
        old = {}
    if not isinstance(new, dict):
        new = {}

    new = clean_invalid_fields(new)
    
    # Make a deep copy to prevent mutation of original
    merged = copy.deepcopy(old)
    merged.update(new)
    
    return merged


def deep_merge_memory(existing_memory, new_data):
    if not isinstance(existing_memory, dict):
        existing_memory = {}
    if not isinstance(new_data, dict):
        return existing_memory

    for key, value in new_data.items():
        if isinstance(value, dict) and isinstance(existing_memory.get(key), dict):
            existing_memory[key] = deep_merge_memory(existing_memory.get(key, {}), value)
        elif value is not None:
            existing_memory[key] = value
    return existing_memory

def save_memory(user_id, memory):
    memory_dir = os.path.join(os.getcwd(), "memory_store")
    os.makedirs(memory_dir, exist_ok=True)

    memory_file = os.path.join(memory_dir, f"{user_id}.json")
    with open(memory_file, "w") as f:
        json.dump(memory, f, indent=2)

    print(f"📝 jino_memory saved to {memory_file}")

def load_memory(user_id):
    memory_file = os.path.join(os.getcwd(), "memory_store", f"{user_id}.json")
    if os.path.exists(memory_file):
        with open(memory_file, "r") as f:
            return json.load(f)
    return {}

def save_judgement(user_id, chat_id, judgement_entry):
    """
    Saves judgement data in a separate file per user, under the respective chat ID.
    """
    memory_dir = os.path.join(os.getcwd(), "memory_store")
    os.makedirs(memory_dir, exist_ok=True)

    file_path = os.path.join(memory_dir, f"{user_id}_judgement.json")
    data = {}

    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            data = json.load(f)

    data.setdefault(chat_id, [])
    data[chat_id].append(judgement_entry)

    with open(file_path, "w") as f:
        json.dump(data, f, indent=2)

    print(f"🧠 jino_judgement saved to {file_path}")

def extract_summary(chat_history):
    max_messages = 5
    recent_messages = chat_history[-max_messages:]
    summary = ""
    for message in recent_messages:
        summary += f"{message['role']}: {message['content']}\n"
    return summary.strip() if summary else "No conversation history found."
