// // // // // const BASE_URL = "http://localhost:5000"; // Your backend URL

// // // // // // API 1: Extract memory facts
// // // // // export const extractFacts = async (message) => {
// // // // //   const res = await fetch(`${BASE_URL}/extract`, {
// // // // //     method: "POST",
// // // // //     headers: { "Content-Type": "application/json" },
// // // // //     body: JSON.stringify({ message }),
// // // // //   });
// // // // //   return await res.json();
// // // // // };

// // // // // // API 2: Get context prompt with filtered data
// // // // // export const getContextPrompt = async (latest_message, memory, judgement, convo_summary) => {
// // // // //   const relevantMemory = {
// // // // //     ...memory, // Only include the key-value pairs that are important
// // // // //     // You can further filter data here if needed
// // // // //   };

// // // // //   const res = await fetch(`${BASE_URL}/context`, {
// // // // //     method: "POST",
// // // // //     headers: { "Content-Type": "application/json" },
// // // // //     body: JSON.stringify({
// // // // //       latest_message,
// // // // //       memory: relevantMemory,
// // // // //       judgement, // Include judgment data
// // // // //       convo_summary, // Summary of previous conversations
// // // // //     }),
// // // // //   });
// // // // //   return await res.json();
// // // // // };

// // // // // // API 3: Get the final reply
// // // // // export const getReply = async (context_prompt) => {
// // // // //   const res = await fetch(`${BASE_URL}/reply`, {
// // // // //     method: "POST",
// // // // //     headers: { "Content-Type": "application/json" },
// // // // //     body: JSON.stringify({ prompt: context_prompt }),
// // // // //   });
// // // // //   return await res.json();
// // // // // };


// // // // const BASE_URL = "http://localhost:5000"; // Update to production URL if needed

// // // // // ✅ API 1: Extract memory facts and update localStorage
// // // // export const extractFacts = async (message) => {
// // // //   const res = await fetch(`${BASE_URL}/extract`, {
// // // //     method: "POST",
// // // //     headers: { "Content-Type": "application/json" },
// // // //     body: JSON.stringify({ message }),
// // // //   });

// // // //   const data = await res.json();

// // // //   // 🔁 Update localStorage
// // // //   if (data.memory) {
// // // //     localStorage.setItem("jino_memory", JSON.stringify(data.memory));
// // // //   }
// // // //   if (data.judgement) {
// // // //     localStorage.setItem("jino_judgement", JSON.stringify(data.judgement));
// // // //   }

// // // //   return data;
// // // // };

// // // // // ✅ API 2: Get context prompt with latest facts + convo summary
// // // // export const getContextPrompt = async (latest_message) => {
// // // //   const memory = JSON.parse(localStorage.getItem("jino_memory") || "{}");
// // // //   const judgement = JSON.parse(localStorage.getItem("jino_judgement") || "{}");
// // // //   const convo_summary = JSON.parse(localStorage.getItem("jino_convo_summary") || "[]");

// // // //   const res = await fetch(`${BASE_URL}/context`, {
// // // //     method: "POST",
// // // //     headers: { "Content-Type": "application/json" },
// // // //     body: JSON.stringify({
// // // //       latest_message,
// // // //       memory,
// // // //       judgement,
// // // //       convo_summary,
// // // //     }),
// // // //   });

// // // //   const data = await res.json();
// // // //   return data.context_prompt || ""; // Return the actual prompt string
// // // // };

// // // // // ✅ API 3: Get final spicy Jino reply
// // // // export const getReply = async (context_prompt) => {
// // // //   const res = await fetch(`${BASE_URL}/reply`, {
// // // //     method: "POST",
// // // //     headers: { "Content-Type": "application/json" },
// // // //     body: JSON.stringify({ prompt: context_prompt }),
// // // //   });

// // // //   const data = await res.json();
// // // //   return data;
// // // // };

// // // // // 🔁 Master function to chain the full JINO cycle
// // // // export const getJinoReply = async (userMessage) => {
// // // //   try {
// // // //     // STEP 1: Extract & update memory
// // // //     await extractFacts(userMessage);

// // // //     // STEP 2: Generate a prompt with savage context
// // // //     const context_prompt = await getContextPrompt(userMessage);

// // // //     if (!context_prompt) throw new Error("Context prompt is empty 🥲");

// // // //     // STEP 3: Let Jino spit bars
// // // //     const reply = await getReply(context_prompt);

// // // //     return reply;
// // // //   } catch (err) {
// // // //     console.error("[JINO ERROR]:", err);
// // // //     return {
// // // //       reply: "Ugh, I malfunctioned harder than your last situationship. Try again.",
// // // //       log: { error: err.message || "Unknown error" },
// // // //     };
// // // //   }
// // // // };

// // // const BASE_URL = "http://localhost:5000"; // change if needed

// // // export const extractFacts = async (message) => {
// // //   const res = await fetch(`${BASE_URL}/extract`, {
// // //     method: "POST",
// // //     headers: { "Content-Type": "application/json" },
// // //     body: JSON.stringify({ message }),
// // //   });

// // //   const data = await res.json();

// // //   if (data.memory) {
// // //     localStorage.setItem("jino_memory", JSON.stringify(data.memory));
// // //   }
// // //   if (data.judgement) {
// // //     localStorage.setItem("jino_judgement", JSON.stringify(data.judgement));
// // //   }

// // //   return data;
// // // };

// // // export const getContextPrompt = async (latest_message) => {
// // //   const memory = JSON.parse(localStorage.getItem("jino_memory") || "{}");
// // //   const judgement = JSON.parse(localStorage.getItem("jino_judgement") || "{}");

// // //   const res = await fetch(`${BASE_URL}/context`, {
// // //     method: "POST",
// // //     headers: { "Content-Type": "application/json" },
// // //     body: JSON.stringify({
// // //       latest_message,
// // //       memory,
// // //       judgement,
// // //     }),
// // //   });

// // //   const data = await res.json();
// // //   return data.context_prompt || "";
// // // };

// // // export const getReply = async (context_prompt) => {
// // //   const res = await fetch(`${BASE_URL}/reply`, {
// // //     method: "POST",
// // //     headers: { "Content-Type": "application/json" },
// // //     body: JSON.stringify({ prompt: context_prompt }),
// // //   });

// // //   return await res.json();
// // // };

// // // export const getJinoReply = async (userMessage) => {
// // //   try {
// // //     await extractFacts(userMessage);
// // //     const context_prompt = await getContextPrompt(userMessage);

// // //     if (!context_prompt) throw new Error("Context prompt is empty 🥲");

// // //     const reply = await getReply(context_prompt);
// // //     return reply;

// // //   } catch (err) {
// // //     console.error("[JINO ERROR]:", err);
// // //     return {
// // //       reply: "Ugh, I malfunctioned harder than your last situationship. Try again.",
// // //       log: { error: err.message || "Unknown error" },
// // //     };
// // //   }
// // // };


// // const BASE_URL = "http://localhost:5000";

// // export const extractFacts = async (message) => {
// //   const res = await fetch(`${BASE_URL}/extract`, {
// //     method: "POST",
// //     headers: { "Content-Type": "application/json" },
// //     body: JSON.stringify({ message }),
// //   });

// //   const data = await res.json();
// //   localStorage.setItem("jino_memory", JSON.stringify(data.memory || {}));
// //   localStorage.setItem("jino_judgement", JSON.stringify(data.judgement || {}));
// //   return data;
// // };

// // export const getContextPrompt = async (latest_message) => {
// //   const memory = JSON.parse(localStorage.getItem("jino_memory") || "{}");
// //   const judgement = JSON.parse(localStorage.getItem("jino_judgement") || "{}");

// //   const res = await fetch(`${BASE_URL}/context`, {
// //     method: "POST",
// //     headers: { "Content-Type": "application/json" },
// //     body: JSON.stringify({ latest_message, memory, judgement }),
// //   });

// //   const data = await res.json();
// //   console.log("📦 Context API Response:", data);
// //   return data.context_prompt || "";
// // };

// // export const getReply = async (context_prompt) => {
// //   const res = await fetch(`${BASE_URL}/reply`, {
// //     method: "POST",
// //     headers: { "Content-Type": "application/json" },
// //     body: JSON.stringify({ prompt: context_prompt }),
// //   });

// //   return await res.json();
// // };

// // export const getJinoReply = async (userMessage) => {
// //   try {
// //     await extractFacts(userMessage);
// //     const context_prompt = await getContextPrompt(userMessage);

// //     if (!context_prompt) throw new Error("Context prompt is empty 🥲");

// //     const reply = await getReply(context_prompt);
// //     return reply;

// //   } catch (err) {
// //     console.error("[JINO ERROR]:", err);
// //     return {
// //       reply: "Ugh, I malfunctioned harder than your last situationship. Try again.",
// //       log: { error: err.message || "Unknown error" },
// //     };
// //   }
// // };

// const BASE_URL = "http://localhost:5000";

// // Extract facts from the message and store them in localStorage
// export const extractFacts = async (message) => {
//   const res = await fetch(`${BASE_URL}/extract`, {
//     method: "POST",
//     headers: { "Content-Type": "application/json" },
//     body: JSON.stringify({ message }),
//   });

//   const data = await res.json();

//   // Make sure memory and judgement are correctly saved even if they are empty
//   localStorage.setItem("jino_memory", JSON.stringify(data.extracted || {}));  // Saving the extracted facts
//   localStorage.setItem("jino_judgement", JSON.stringify(data.judgement || {}));  // Saving the judgement

//   return data;  // Return data for further use
// };

// // Get context for the latest message
// export const getContextPrompt = async (latest_message) => {
//   const memory = JSON.parse(localStorage.getItem("jino_memory") || "{}");
//   const judgement = JSON.parse(localStorage.getItem("jino_judgement") || "{}");

//   const res = await fetch(`${BASE_URL}/context`, {
//     method: "POST",
//     headers: { "Content-Type": "application/json" },
//     body: JSON.stringify({ latest_message, memory, judgement }),
//   });

//   const data = await res.json();
//   console.log("📦 Context API Response:", data);
//   return data.context_prompt || "";
// };

// // Get the final reply based on the context
// export const getReply = async (context_prompt) => {
//   const res = await fetch(`${BASE_URL}/reply`, {
//     method: "POST",
//     headers: { "Content-Type": "application/json" },
//     body: JSON.stringify({ prompt: context_prompt }),
//   });

//   return await res.json();
// };

// // Complete function to extract facts, get context, and finally generate the AI reply
// export const getJinoReply = async (userMessage) => {
//   try {
//     const extractData = await extractFacts(userMessage);  // Extract facts and save them
//     const context_prompt = await getContextPrompt(userMessage);  // Get context

//     if (!context_prompt) throw new Error("Context prompt is empty 🥲");

//     const reply = await getReply(context_prompt);  // Get reply
//     return reply;

//   } catch (err) {
//     console.error("[JINO ERROR]:", err);
//     return {
//       reply: "Ugh, I malfunctioned harder than your last situationship. Try again.",
//       log: { error: err.message || "Unknown error" },
//     };
//   }
// };




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
