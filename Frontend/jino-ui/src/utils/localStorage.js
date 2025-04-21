

// import { v4 as uuidv4 } from 'uuid'; 

// // 🆔 Generate or retrieve a stable UUID for this user
// export const getUUID = () => {
//   let id = localStorage.getItem("jino_uid");
//   if (!id) {
//     id = uuidv4();
//     localStorage.setItem("jino_uid", id);
//   } else if (!validateUUID(id)) {
//     id = uuidv4();
//     localStorage.setItem("jino_uid", id);
//   }
//   console.log("[UUID] Current userId:", id);
//   return id;
// };

// // 🧪 Validate that string is a proper UUID
// const validateUUID = (uuidStr) => {
//   const uuidRegex = /^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i;
//   return uuidRegex.test(uuidStr);
// };

// // 🧠 Safely parse JSON, returns null on error
// const safeParse = (json) => {
//   try {
//     return JSON.parse(json);
//   } catch (e) {
//     console.warn("[safeParse] JSON parse error:", e);
//     return null;
//   }
// };

// // 🚿 Clean out empty or "not provided" fields
// const cleanInvalidFields = (obj) => {
//   const cleaned = {};
//   for (const key in obj) {
//     const val = obj[key];
//     if (val !== undefined && val !== null && val !== "" && val !== "not provided") {
//       cleaned[key] = val;
//     }
//   }
//   console.log("[cleanInvalidFields] cleaned:", cleaned);
//   return cleaned;
// };

// // 🧠 Retrieve stored user memory (factual)
// export const getMemory = () => {
//   const userId = getUUID();
//   const raw = localStorage.getItem(`jino_memory_${userId}`);
//   const memory = safeParse(raw) || {};
//   console.log("[getMemory] loaded:", memory);
//   return memory;
// };

// // 🧠 Merge and save new memory, but skip if newMem is empty
// export const updateMemory = (newMem) => {
//   if (!newMem || Object.keys(newMem).length === 0) {
//     console.log("[updateMemory] newMem is empty, skipping update");
//     return;
//   }

//   const userId = getUUID();
//   console.log("[updateMemory] newMem incoming:", newMem);

//   const oldMem = getMemory();
//   const cleanedNew = cleanInvalidFields(newMem);
//   const merged = { ...oldMem, ...cleanedNew };
//   console.log("[updateMemory] merged memory:", merged);

//   try {
//     localStorage.setItem(`jino_memory_${userId}`, JSON.stringify(merged));
//     console.log("[updateMemory] saved successfully");
//   } catch (e) {
//     console.error("[updateMemory] error saving memory:", e);
//   }
// };

// // 🧠 Retrieve stored emotional judgement
// export const getJudgement = () => {
//   const userId = getUUID();
//   const raw = localStorage.getItem(`jino_judgement_${userId}`);
//   const judgement = safeParse(raw) || {};
//   console.log("[getJudgement] loaded:", judgement);
//   return judgement;
// };

// // 🧠 Save new judgement, but skip if data is empty
// export const saveJudgement = (data) => {
//   if (!data || Object.keys(data).length === 0) {
//     console.log("[saveJudgement] data empty, skipping save");
//     return;
//   }

//   const userId = getUUID();
//   console.log("[saveJudgement] data incoming:", data);

//   try {
//     localStorage.setItem(`jino_judgement_${userId}`, JSON.stringify(data));
//     console.log("[saveJudgement] saved successfully");
//   } catch (e) {
//     console.error("[saveJudgement] error saving judgement:", e);
//   }
// };

// // 🧾 Conversation summary (sessionStorage, last 5)
// export const getConvoSummary = () => {
//   const raw = sessionStorage.getItem("jino_convo_summary");
//   const summary = safeParse(raw) || [];
//   console.log("[getConvoSummary] loaded:", summary);
//   return summary;
// };

// export const saveConvoSummary = (message) => {
//   const summary = getConvoSummary();
//   const entry = typeof message === "string"
//     ? { message, time: new Date().toISOString() }
//     : message;

//   summary.push(entry);
//   if (summary.length > 5) summary.shift();
//   console.log("[saveConvoSummary] updated summary:", summary);

//   sessionStorage.setItem("jino_convo_summary", JSON.stringify(summary));
// };

// export const updateConvoSummary = saveConvoSummary;

// // 📁 Generic save/read to localStorage
// export const saveToFile = (filename, data) => {
//   try {
//     localStorage.setItem(filename, JSON.stringify(data));
//     console.log(`[saveToFile] ${filename} saved`);
//   } catch (e) {
//     console.error(`[saveToFile] error saving ${filename}:`, e);
//   }
// };

// export const readFile = (filename) => {
//   const raw = localStorage.getItem(filename);
//   const parsed = safeParse(raw) || {};
//   console.log(`[readFile] ${filename}:`, parsed);
//   return parsed;
// };

// // 💣 Clear only user memory
// export const clearMemory = () => {
//   const userId = getUUID();
//   localStorage.removeItem(`jino_memory_${userId}`);
//   console.log(`[clearMemory] removed jino_memory_${userId}`);
// };

// // 💣💣 Nukes all Jino data for this user
// export const clearAllJinoData = () => {
//   const userId = getUUID();
//   [
//     "jino_uid",
//     `jino_memory_${userId}`,
//     `jino_judgement_${userId}`,
//     "jino_convo_summary",
//     "jino_tokens_used"
//   ].forEach(key => {
//     localStorage.removeItem(key);
//     console.log(`[clearAllJinoData] removed ${key}`);
//   });
// };

// // 🔢 Token usage tracker
// export const saveTokensUsed = (count) => {
//   try {
//     localStorage.setItem("jino_tokens_used", count.toString());
//     console.log("[saveTokensUsed] saved:", count);
//   } catch (e) {
//     console.error("[saveTokensUsed] error:", e);
//   }
// };

// export const getTokensUsed = () => {
//   const raw = localStorage.getItem("jino_tokens_used") || "0";
//   const num = parseInt(raw, 10);
//   console.log("[getTokensUsed] loaded:", num);
//   return num;
// };

// // 🧩 Utility to list all Jino keys in localStorage
// export const listJinoStorageKeys = () => {
//   const keys = Object.keys(localStorage).filter(key => key.startsWith("jino_"));
//   console.log("[listJinoStorageKeys]", keys);
//   return keys;
// };









import { v4 as uuidv4 } from 'uuid'; 

// 🆔 Generate or retrieve a stable UUID for this user
export const getUUID = () => {
  let id = localStorage.getItem("jino_uid");
  if (!id) {
    id = uuidv4();
    localStorage.setItem("jino_uid", id);
  } else if (!validateUUID(id)) {
    id = uuidv4();
    localStorage.setItem("jino_uid", id);
  }
  console.log("[UUID] Current userId:", id);
  return id;
};

// 🧪 Validate that string is a proper UUID
const validateUUID = (uuidStr) => {
  const uuidRegex = /^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i;
  return uuidRegex.test(uuidStr);
};

// 🧠 Safely parse JSON, returns null on error
const safeParse = (json) => {
  try {
    return JSON.parse(json);
  } catch (e) {
    console.warn("[safeParse] JSON parse error:", e);
    return null;
  }
};

// 🚿 Clean out empty or "not provided" fields
const cleanInvalidFields = (obj) => {
  const cleaned = {};
  for (const key in obj) {
    const val = obj[key];
    if (val !== undefined && val !== null && val !== "" && val !== "not provided") {
      cleaned[key] = val;
    }
  }
  console.log("[cleanInvalidFields] cleaned:", cleaned);
  return cleaned;
};

// 🧠 Retrieve stored user memory (factual)
export const getMemory = () => {
  const userId = getUUID();
  const raw = localStorage.getItem(`jino_memory_${userId}`);
  const memory = safeParse(raw) || {};
  console.log("[getMemory] loaded:", memory);
  return memory;
};

// 🧠 Merge and save new memory, but skip if newMem is empty
export const updateMemory = (newMem) => {
  if (!newMem || Object.keys(newMem).length === 0) {
    console.log("[updateMemory] newMem is empty, skipping update");
    return;
  }

  const userId = getUUID();
  console.log("[updateMemory] newMem incoming:", newMem);

  const oldMem = getMemory();
  const cleanedNew = cleanInvalidFields(newMem);
  const merged = { ...oldMem, ...cleanedNew };
  console.log("[updateMemory] merged memory:", merged);

  try {
    localStorage.setItem(`jino_memory_${userId}`, JSON.stringify(merged));
    console.log("[updateMemory] saved successfully");
  } catch (e) {
    console.error("[updateMemory] error saving memory:", e);
  }
};

// 🧠 Retrieve stored emotional judgement
export const getJudgement = () => {
  const userId = getUUID();
  const raw = localStorage.getItem(`jino_judgement_${userId}`);
  const judgement = safeParse(raw) || {};
  console.log("[getJudgement] loaded:", judgement);
  return judgement;
};

// 🧠 Save new judgement, but skip if data is empty
export const saveJudgement = (data) => {
  if (!data || Object.keys(data).length === 0) {
    console.log("[saveJudgement] data empty, skipping save");
    return;
  }

  const userId = getUUID();
  console.log("[saveJudgement] data incoming:", data);

  try {
    localStorage.setItem(`jino_judgement_${userId}`, JSON.stringify(data));
    console.log("[saveJudgement] saved successfully");
  } catch (e) {
    console.error("[saveJudgement] error saving judgement:", e);
  }
};

// 🧾 Conversation summary (sessionStorage, last 5)
export const getConvoSummary = () => {
  const raw = sessionStorage.getItem("jino_convo_summary");
  const summary = safeParse(raw) || [];
  console.log("[getConvoSummary] loaded:", summary);
  return summary;
};

export const saveConvoSummary = (message) => {
  const summary = getConvoSummary();
  const entry = typeof message === "string"
    ? { message, time: new Date().toISOString() }
    : message;

  summary.push(entry);
  if (summary.length > 5) summary.shift();
  console.log("[saveConvoSummary] updated summary:", summary);

  sessionStorage.setItem("jino_convo_summary", JSON.stringify(summary));
};

export const updateConvoSummary = saveConvoSummary;

// 📁 Generic save/read to localStorage
export const saveToFile = (filename, data) => {
  try {
    localStorage.setItem(filename, JSON.stringify(data));
    console.log(`[saveToFile] ${filename} saved`);
  } catch (e) {
    console.error(`[saveToFile] error saving ${filename}:`, e);
  }
};

export const readFile = (filename) => {
  const raw = localStorage.getItem(filename);
  const parsed = safeParse(raw) || {};
  console.log(`[readFile] ${filename}:`, parsed);
  return parsed;
};

// 💣 Clear only user memory
export const clearMemory = () => {
  const userId = getUUID();
  localStorage.removeItem(`jino_memory_${userId}`);
  console.log(`[clearMemory] removed jino_memory_${userId}`);
};

// 💣💣 Nukes all Jino data for this user
export const clearAllJinoData = () => {
  const userId = getUUID();
  [
    "jino_uid",
    `jino_memory_${userId}`,
    `jino_judgement_${userId}`,
    "jino_convo_summary",
    "jino_tokens_used"
  ].forEach(key => {
    localStorage.removeItem(key);
    console.log(`[clearAllJinoData] removed ${key}`);
  });
};

// 🔢 Token usage tracker
export const saveTokensUsed = (count) => {
  try {
    localStorage.setItem("jino_tokens_used", count.toString());
    console.log("[saveTokensUsed] saved:", count);
  } catch (e) {
    console.error("[saveTokensUsed] error:", e);
  }
};

export const getTokensUsed = () => {
  const raw = localStorage.getItem("jino_tokens_used") || "0";
  const num = parseInt(raw, 10);
  console.log("[getTokensUsed] loaded:", num);
  return num;
};

// 🧩 Utility to list all Jino keys in localStorage
export const listJinoStorageKeys = () => {
  const keys = Object.keys(localStorage).filter(key => key.startsWith("jino_"));
  console.log("[listJinoStorageKeys]", keys);
  return keys;
};



