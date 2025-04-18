// Description: Main component for the Jino AI application
// This file contains the API calls to the backend server for extracting facts, generating context, and getting replies from Jino AI.
// It also handles the local storage of user data and memory.
// This file is responsible for the interaction between the frontend and backend of the Jino AI application.
// It includes functions to extract facts from user messages, generate context prompts, and get replies from the AI model.
// It also manages the local storage of user data and memory, ensuring that the application can maintain context across sessions.
// Api.js
const BASE_URL = "http://localhost:5000";
import { getUUID, getMemory, updateMemory, getJudgement, saveJudgement } from "./localStorage";

// Extract facts from the message and store them in localStorage
export const extractFacts = async (message) => {
  const userId = getUUID(); // 🆔 Get the unique user ID
  const memory = getMemory(); // 🧠 Existing memory for that user

  const res = await fetch(`${BASE_URL}/extract`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message, user_id: userId, memory }),
  });

  const data = await res.json();

  const updatedMemory = data.extracted || {};
  const updatedJudgement = data.judgement || {};

  // 🧠 Store memory under unique key per user
  localStorage.setItem(`jino_memory_${userId}`, JSON.stringify(updatedMemory));
  localStorage.setItem("jino_judgement", JSON.stringify(updatedJudgement));

  console.log("📥 Extract API:", { updatedMemory, updatedJudgement });
  return data;
};

// Get context for the latest message
export const getContextPrompt = async (latest_message) => {
  const memory = getMemory();
  const judgement = getJudgement();

  const res = await fetch(`${BASE_URL}/context`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ latest_message, memory, judgement }),
  });

  const data = await res.json();
  console.log("📦 Context API Response:", data);
  return data.context_prompt || "";
};

// Get the final reply based on the context
export const getReply = async (context_prompt) => {
  const res = await fetch(`${BASE_URL}/reply`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ prompt: context_prompt }),
  });

  return await res.json();
};

// Complete function to extract facts, get context, and finally generate the AI reply
export const getJinoReply = async (userMessage) => {
  try {
    const extractData = await extractFacts(userMessage); // 🧠 Extract and save
    const context_prompt = await getContextPrompt(userMessage); // 🧠 Generate contextual prompt

    if (!context_prompt) throw new Error("Context prompt is empty 🥲");

    const reply = await getReply(context_prompt); // 🤖 Generate reply
    return reply;

  } catch (err) {
    console.error("[JINO ERROR]:", err);
    return {
      reply: "Ugh, I malfunctioned harder than your last situationship. Try again.",
      log: { error: err.message || "Unknown error" },
    };
  }
};
