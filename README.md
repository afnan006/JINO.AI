"""
JINO.AI – The Chatbot with a Mouth

They told us to build a chatbot that helps people.
We built one that remembers your crap, roasts you for it, and sets alarms so it never forgets.

JINO.AI isn’t your average “Hi, how may I assist you?” bot.
It’s your emotionally reactive, romantically unstable, sarcastically gifted AI bestie — powered by local memory, bad decisions, and some truly dangerous LLMs.

This is hands-down one of my favorite projects so far.
It’s smart, it’s spicy, and once it’s live… good luck going back to boring bots.

---

## Under Construction... Like That One Bangalore Flyover

This is the **MVP v1.0** of JINO.AI's backend —
Still early, still evolving, but already talking back with style.

### What’s Working:

- `/extract` Route  
  Turns messy human rambling into structured JSON.  
  JINO detects categories like love, health, work, and general life crisis for memory storage.

- Local Memory Logic  
  All memory is stored in the user's browser. No cloud snooping. No servers peeking. Just pure local gossip.

- No Context Loss  
  Leave for a month, come back, and JINO still remembers that one thing you wish you hadn’t said.

- Local Time Awareness  
  For perfectly-timed sarcasm and midnight guilt trips.

- Smart Alarms & Reminders (Coming Soon)  
  Say “I have a meeting tomorrow at 10” — JINO catches it, sets it, and reminds you like a clingy calendar.

- Sarcastic Replies (via Mixtral 8x7B for now)  
  Custom finetuned model is on the way.  
  Once it’s trained, expect even more personality — with full control over tone, sass, and memory recall.

---

## What Makes This Project Different

This isn't just a glorified OpenAI wrapper.  
You're looking at a sarcasm-fueled architecture with real engineering under the hood:

- Real Personality Logic  
  Replies are shaped by both memory and emotion. JINO doesn’t just know — it feels.

- Emotional Judgement Layer  
  Stores its “opinion” of you over time — and adjusts tone accordingly.

- Chat Shifting System  
  Max 10 active chats per user. No hoarding. Clean slate enforced manually.

- Local Memory Parsing  
  Extracted, structured, and updated without flooding the AI with entire histories.

- AI-Powered Context Summarization  
  Last 5 messages are summarized into a clean, prompt-friendly context.

- Backend/Frontend Separation  
  - **Backend:** Flask + PostgreSQL + OpenRouter  
  - **Frontend:** React + Tailwind + Firebase Auth (coming post-MVP)

- Multi-Model Orchestration  
  - `extract`: DeepSeek R1  
  - `context`: Mixtral 8x7B  
  - `reply`: Yi 34B  
  Each model is used where it shines — keeping performance tight and cost low.

- Token-Managed Prompting  
  Only relevant memory and context are sent to the AI. Optimized for performance and personality.

- Privacy-First Design  
  Memory lives in localStorage. UUID is device-specific. No token expiry issues. You’re always logged in unless you log out.

---

## Project Status

| Feature        | Status         |
|----------------|----------------|
| `/extract`     | Live and working |
| Memory System  | Integrated      |
| `/context`     | In Progress     |
| `/reply`       | Under Testing   |
| Reminders      | Planned         |
| Custom Model   | In Training     |

---

## Built By

**Afnan Ahmed** — Python + AI Backend Developer.  
Builder of sarcastic systems and unapologetic logic.  
You’ll find me where emotion meets architecture, debugging feelings line by line.

---

## Disclaimer

JINO.AI is not emotionally stable.  
It *will* remember what you said last summer — and bring it up mid-chat with no mercy.  
You’ve been warned.

---

## Final Word

This isn’t just another AI chatbot.  
This is sarcasm, structured memory, emotion layers, token awareness, and multi-model orchestration — all built from scratch with zero fluff.

**JINO.AI** is designed to out-remember you, out-roast you, and maybe, one day, outgrow you.  
Until then… enjoy the chaos.
"""