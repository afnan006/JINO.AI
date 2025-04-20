
const BASE_URL = "http://localhost:5000";
import {
  getUUID,
  getMemory,
  updateMemory,
  getJudgement,
  saveJudgement,
  getConvoSummary,
  saveConvoSummary,
} from "./localStorage";

// ✅ Safe handler for convo_summary updates
const handleConvoSummaryUpdate = (updatedConvoSummary) => {
  const summaries = Array.isArray(updatedConvoSummary)
    ? updatedConvoSummary
    : [updatedConvoSummary];

  summaries.forEach((msg) => saveConvoSummary(msg));
};

// 🧠 Extract facts from the message and store them in localStorage
export const extractFacts = async (message) => {
  const userId = getUUID();
  const memory = getMemory();
  const convoSummary = getConvoSummary();

  const res = await fetch(`${BASE_URL}/extract`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      message,
      user_id: userId,
      memory,
      convo_summary: convoSummary,
    }),
  });

  const data = await res.json();

  const updatedMemory = data.extracted || {};
  const updatedJudgement = data.judgement || {};
  const updatedConvoSummary = data.convo_summary || [];

  updateMemory(updatedMemory);
  saveJudgement(updatedJudgement);
  handleConvoSummaryUpdate(updatedConvoSummary);

  console.log("📥 Extract API:", {
    updatedMemory,
    updatedJudgement,
    updatedConvoSummary,
  });

  return data;
};

// 🧠 Get context for the latest message
export const getContextPrompt = async (latest_message) => {
  const memory = getMemory();
  const judgement = getJudgement();
  const convoSummary = getConvoSummary();

  const res = await fetch(`${BASE_URL}/context`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      latest_message,
      memory,
      judgement,
      convo_summary: convoSummary,
    }),
  });

  const data = await res.json();
  console.log("📦 Context API Response:", data);
  return data.context_prompt || "";
};

// 🤖 Get the final reply based on the context
export const getReply = async (context_prompt) => {
  const res = await fetch(`${BASE_URL}/reply`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ prompt: context_prompt }),
  });

  return await res.json();
};

// 💬 Complete function to extract facts, get context, and generate JINO's spicy reply
export const getJinoReply = async (userMessage) => {
  try {
    const extractData = await extractFacts(userMessage);
    const context_prompt = await getContextPrompt(userMessage);

    if (!context_prompt) throw new Error("Context prompt is empty 🥲");

    const reply = await getReply(context_prompt);
    return reply;
  } catch (err) {
    console.error("[JINO ERROR]:", err);
    return {
      reply: "Ugh, I malfunctioned harder than your last situationship. Try again.",
      log: { error: err.message || "Unknown error" },
    };
  }
};
