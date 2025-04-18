
// src/utils/localStorage.js
// 🗄️ Local Storage Utility Functions for Jino
// This file handles the storage and retrieval of user data, memory, and other relevant information in the browser's local storage.
// It includes functions to get or create a unique user ID, manage user memory, and handle chat summaries.
// It also provides functions to save and read files, clear memory, and track token usage.
// It is designed to be used in the Jino AI application, which is a web-based chat application that uses AI to generate responses.

import { v4 as uuidv4 } from 'uuid'; // ✅ USE THIS instead of crypto.randomUUID

// 🆔 Get or create UUID
export const getUUID = () => {
  let id = localStorage.getItem("jino_uid");
  if (!id) {
    id = uuidv4(); // ✅ use uuidv4
    localStorage.setItem("jino_uid", id);
  } else if (!validateUUID(id)) {
    id = uuidv4(); // ✅ regenerate if broken
    localStorage.setItem("jino_uid", id);
  }
  return id;
};

// 🧪 Check if UUID format is valid
const validateUUID = (uuidStr) => {
  const uuidRegex = /^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i;
  return uuidRegex.test(uuidStr);
};

// 🧠 Safe JSON parser
const safeParse = (json) => {
  try {
    return JSON.parse(json);
  } catch {
    return null;
  }
};

// 🧠 USER MEMORY (factual)
export const getMemory = () => {
  const userId = getUUID();
  const memory = localStorage.getItem(`jino_memory_${userId}`);
  return safeParse(memory) || {};
};

export const updateMemory = (newMem) => {
  const userId = getUUID();
  const oldMem = getMemory();
  const merged = { ...oldMem, ...cleanInvalidFields(newMem) };
  localStorage.setItem(`jino_memory_${userId}`, JSON.stringify(merged));
};

// 🚿 Clean garbage from memory
const cleanInvalidFields = (memory) => {
  let cleanedMemory = {};
  for (let key in memory) {
    if (memory[key] && memory[key] !== "not provided") {
      cleanedMemory[key] = memory[key];
    }
  }
  return cleanedMemory;
};

// 🧠 Emotional Judgement
export const getJudgement = () => {
  const j = localStorage.getItem("jino_judgement");
  return safeParse(j) || {};
};

export const saveJudgement = (data) => {
  localStorage.setItem("jino_judgement", JSON.stringify(data));
};

// 🧾 Chat Summary (last 5 messages)
export const getChatSummary = () => {
  const c = localStorage.getItem("jino_convo_summary");
  return safeParse(c) || [];
};

export const updateChatSummary = (message) => {
  let summary = getChatSummary();
  const entry = typeof message === "string"
    ? { message, time: new Date().toISOString() }
    : message;

  summary.push(entry);
  if (summary.length > 5) summary.shift();
  localStorage.setItem("jino_convo_summary", JSON.stringify(summary));
};

// 📁 File-style Storage
export const saveToFile = (filename, data) => {
  localStorage.setItem(filename, JSON.stringify(data));
};

export const readFile = (filename) => {
  const data = localStorage.getItem(filename);
  return safeParse(data) || {};
};

// 💣 Memory nuking
export const clearMemory = () => {
  const userId = getUUID();
  localStorage.removeItem(`jino_memory_${userId}`);
};

// 💣💣 Nuke everything Jino
export const clearAllJinoData = () => {
  const userId = getUUID();
  [
    "jino_uid",
    `jino_memory_${userId}`,
    "jino_judgement",
    "jino_convo_summary",
    "jino_tokens_used"
  ].forEach((key) => localStorage.removeItem(key));
};

// 🔢 Token usage tracker
export const saveTokensUsed = (count) => {
  localStorage.setItem("jino_tokens_used", count.toString());
};

export const getTokensUsed = () => {
  return parseInt(localStorage.getItem("jino_tokens_used") || "0", 10);
};

// 🧩 Debugger: List all Jino storage keys
export const listJinoStorageKeys = () => {
  return Object.keys(localStorage).filter((key) => key.startsWith("jino_"));
};
