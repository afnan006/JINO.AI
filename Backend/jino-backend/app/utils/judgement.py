# from datetime import datetime

# def add_judgement(user_input, existing_memory):
#     """
#     Determines whether the user message is judgement-worthy.
#     If it is, adds a judgement entry to the user's memory.
#     """
#     judgement = {}

#     # Simple logic to judge based on emotional context or significant input
#     if "stress" in user_input.lower():
#         judgement = {
#             "timestamp": datetime.utcnow().isoformat(),
#             "category": "emotional_state",
#             "judgement": "User seems stressed but is still grinding like a beast.",
#             "confidence": "high"
#         }

#     # You can expand with other emotional judgments, tone recognition, etc.
    
#     if judgement:
#         # Ensure the memory structure exists
#         existing_memory.setdefault("jino_judgement", {})
        
#         # Get the chat ID (or set a default if not present)
#         chat_id = existing_memory.get('chat_id', 'chat_1')  # Default chat_id if not set

#         # Ensure chat_id entry exists for judgments
#         existing_memory["jino_judgement"].setdefault(chat_id, [])
        
#         # Append the judgment to the respective chat's memory
#         existing_memory["jino_judgement"][chat_id].append(judgement)
#         print(f"🧠 Added judgement: {judgement}")

#     # Return updated memory for further use
#     return existing_memory
