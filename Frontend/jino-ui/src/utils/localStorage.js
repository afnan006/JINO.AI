// // // export const getUUID = () => {
// // //     let id = localStorage.getItem("jino_uid");
// // //     if (!id) {
// // //       id = crypto.randomUUID();
// // //       localStorage.setItem("jino_uid", id);
// // //     }
// // //     return id;
// // //   };
  
// // //   export const getMemory = () => {
// // //     const memory = localStorage.getItem("jino_memory");
// // //     return memory ? JSON.parse(memory) : {};
// // //   };
  
// // //   export const updateMemory = (newMem) => {
// // //     const oldMem = getMemory();
// // //     const merged = { ...oldMem, ...newMem };
// // //     localStorage.setItem("jino_memory", JSON.stringify(merged));
// // //   };
  
// // //   export const getJudgement = () => {
// // //     const j = localStorage.getItem("jino_judgement");
// // //     return j ? JSON.parse(j) : {};
// // //   };
  
// // //   export const saveJudgement = (data) => {
// // //     localStorage.setItem("jino_judgement", JSON.stringify(data));
// // //   };
  
// // //   export const getChatSummary = () => {
// // //     const c = localStorage.getItem("jino_convo_summary");
// // //     return c ? JSON.parse(c) : [];
// // //   };
  
// // //   export const updateChatSummary = (message) => {
// // //     let summary = getChatSummary();
// // //     summary.push(message);
// // //     if (summary.length > 5) summary.shift(); // Keep the latest 5 messages
// // //     localStorage.setItem("jino_convo_summary", JSON.stringify(summary));
// // //   };
  
// // //   // Simulate text file saving in the browser for data separation
// // //   export const saveToFile = (filename, data) => {
// // //     localStorage.setItem(filename, JSON.stringify(data));
// // //   };
  
// // //   export const readFile = (filename) => {
// // //     const data = localStorage.getItem(filename);
// // //     return data ? JSON.parse(data) : {};
// // //   };
  

// // // localStorage.js

// // // 🔐 Unique user ID (persistent)
// // export const getUUID = () => {
// //     let id = localStorage.getItem("jino_uid");
// //     if (!id) {
// //       id = crypto.randomUUID();
// //       localStorage.setItem("jino_uid", id);
// //     }
// //     return id;
// //   };
  
// //   // 🧠 Safe JSON parsing helper
// //   const safeParse = (json) => {
// //     try {
// //       return JSON.parse(json);
// //     } catch {
// //       return null;
// //     }
// //   };
  
// //   // 🧠 User factual memory
// //   export const getMemory = () => {
// //     const memory = localStorage.getItem("jino_memory");
// //     return safeParse(memory) || {};
// //   };
  
// //   export const updateMemory = (newMem) => {
// //     const oldMem = getMemory();
// //     const merged = { ...oldMem, ...newMem };
// //     localStorage.setItem("jino_memory", JSON.stringify(merged));
// //   };
  
// //   // 🧠 Emotional judgement
// //   export const getJudgement = () => {
// //     const j = localStorage.getItem("jino_judgement");
// //     return safeParse(j) || {};
// //   };
  
// //   export const saveJudgement = (data) => {
// //     localStorage.setItem("jino_judgement", JSON.stringify(data));
// //   };
  
// //   // 🧾 Conversation summary (last 5 messages)
// //   export const getChatSummary = () => {
// //     const c = localStorage.getItem("jino_convo_summary");
// //     return safeParse(c) || [];
// //   };
  
// //   export const updateChatSummary = (message) => {
// //     let summary = getChatSummary();
  
// //     // Optional timestamp included without breaking old code
// //     const entry = typeof message === "string"
// //       ? { message, time: new Date().toISOString() }
// //       : message;
  
// //     summary.push(entry);
// //     if (summary.length > 5) summary.shift();
// //     localStorage.setItem("jino_convo_summary", JSON.stringify(summary));
// //   };
  
// //   // 📁 Simulated file system for modular storage
// //   export const saveToFile = (filename, data) => {
// //     localStorage.setItem(filename, JSON.stringify(data));
// //   };
  
// //   export const readFile = (filename) => {
// //     const data = localStorage.getItem(filename);
// //     return safeParse(data) || {};
// //   };
  
// //   // 💣 Utility: Clear memory
// //   export const clearMemory = () => {
// //     localStorage.removeItem("jino_memory");
// //   };
  
// //   // 💣💣 Utility: Nuke all Jino data
// //   export const clearAllJinoData = () => {
// //     [
// //       "jino_uid",
// //       "jino_memory",
// //       "jino_judgement",
// //       "jino_convo_summary",
// //       "jino_tokens_used"
// //     ].forEach((key) => localStorage.removeItem(key));
// //   };
  
// //   // 🔢 Token usage tracking (for limits / warnings)
// //   export const saveTokensUsed = (count) => {
// //     localStorage.setItem("jino_tokens_used", count.toString());
// //   };
  
// //   export const getTokensUsed = () => {
// //     return parseInt(localStorage.getItem("jino_tokens_used") || "0", 10);
// //   };
  
// //   // 🧩 Debug: List all Jino keys
// //   export const listJinoStorageKeys = () => {
// //     return Object.keys(localStorage).filter((key) => key.startsWith("jino_"));
// //   };
  

// // 🔐 Unique user ID (persistent) with validation
// import { v4 as uuidv4 } from 'uuid'; // Import the UUID library
// export const getUUID = () => {
//   let id = localStorage.getItem("jino_uid");
//   if (!id) {
//     id = crypto.randomUUID();
//     localStorage.setItem("jino_uid", id);
//   } else if (!validateUUID(id)) {
//     // If UUID is invalid, regenerate and store it
//     id = crypto.randomUUID();
//     localStorage.setItem("jino_uid", id);
//   }
//   return id;
// };

// // Function to validate if UUID is properly formatted
// // Function to validate if UUID is properly formatted
// const validateUUID = (uuidStr) => {
//   const uuidRegex = /^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i;
//   return uuidRegex.test(uuidStr);
// };

// // 🧠 Safe JSON parsing helper
// const safeParse = (json) => {
//   try {
//     return JSON.parse(json);
//   } catch {
//     return null;
//   }
// };

// // 🧠 User factual memory
// // export const getMemory = () => {
// //   const memory = localStorage.getItem("jino_memory");
// //   return safeParse(memory) || {};
// // };

// // // Merge memory and ensure we are not overwriting good data
// // export const updateMemory = (newMem) => {
// //   const oldMem = getMemory();
// //   const merged = { ...oldMem, ...cleanInvalidFields(newMem) }; // Ensure invalid fields like "not provided" are ignored
// //   localStorage.setItem("jino_memory", JSON.stringify(merged));
// // };
// export const getMemory = () => {
//   const userId = getUUID();
//   const memory = localStorage.getItem(`jino_memory_${userId}`);
//   return safeParse(memory) || {};
// };

// export const updateMemory = (newMem) => {
//   const userId = getUUID();
//   const oldMem = getMemory();
//   const merged = { ...oldMem, ...cleanInvalidFields(newMem) };
//   localStorage.setItem(`jino_memory_${userId}`, JSON.stringify(merged));
// };


// // Clean "not provided" and empty values from the memory
// const cleanInvalidFields = (memory) => {
//   let cleanedMemory = {};
//   for (let key in memory) {
//     if (memory[key] && memory[key] !== "not provided") {  // Clean up "not provided" and empty values
//       cleanedMemory[key] = memory[key];
//     }
//   }
//   return cleanedMemory;
// };

// // 🧠 Emotional judgement saving
// export const getJudgement = () => {
//   const j = localStorage.getItem("jino_judgement");
//   return safeParse(j) || {};
// };

// export const saveJudgement = (data) => {
//   localStorage.setItem("jino_judgement", JSON.stringify(data));  // Persist judgement
// };

// // 🧾 Conversation summary (last 5 messages)
// export const getChatSummary = () => {
//   const c = localStorage.getItem("jino_convo_summary");
//   return safeParse(c) || [];
// };

// export const updateChatSummary = (message) => {
//   let summary = getChatSummary();

//   // Optional timestamp included without breaking old code
//   const entry = typeof message === "string"
//     ? { message, time: new Date().toISOString() }
//     : message;

//   summary.push(entry);
//   if (summary.length > 5) summary.shift();
//   localStorage.setItem("jino_convo_summary", JSON.stringify(summary));
// };

// // 📁 Simulated file system for modular storage
// export const saveToFile = (filename, data) => {
//   localStorage.setItem(filename, JSON.stringify(data));
// };

// export const readFile = (filename) => {
//   const data = localStorage.getItem(filename);
//   return safeParse(data) || {};
// };

// // 💣 Utility: Clear memory
// export const clearMemory = () => {
//   localStorage.removeItem("jino_memory");
// };


// // 💣💣 Utility: Nuke all Jino data
// export const clearAllJinoData = () => {
//   [
//     "jino_uid",
//     "jino_memory",
//     "jino_judgement",
//     "jino_convo_summary",
//     "jino_tokens_used"
//   ].forEach((key) => localStorage.removeItem(key));
// };

// // 🔢 Token usage tracking (for limits / warnings)
// export const saveTokensUsed = (count) => {
//   localStorage.setItem("jino_tokens_used", count.toString());
// };

// export const getTokensUsed = () => {
//   return parseInt(localStorage.getItem("jino_tokens_used") || "0", 10);
// };

// // 🧩 Debug: List all Jino keys
// export const listJinoStorageKeys = () => {
//   return Object.keys(localStorage).filter((key) => key.startsWith("jino_"));
// };


// src/utils/localStorage.js

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
