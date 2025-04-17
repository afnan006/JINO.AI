// // import { useState, useEffect } from "react";
// // import {
// //   getUUID,
// //   getMemory,
// //   updateMemory,
// //   updateChatSummary,
// //   getChatSummary,
// //   getJudgement,
// // } from "./utils/localStorage";
// // import {
// //   extractFacts,
// //   getContextPrompt,
// //   getReply,
// // } from "./utils/api";

// // function App() {
// //   const [input, setInput] = useState("");
// //   const [reply, setReply] = useState("");
// //   const [loading, setLoading] = useState(false);

// //   useEffect(() => {
// //     getUUID(); // generate and save UUID if not exists
// //   }, []);

// //   const handleSubmit = async () => {
// //     if (!input.trim()) return;

// //     setLoading(true);
// //     setReply("");

// //     try {
// //       // 1. Extract memory facts from the message
// //       const extractRes = await extractFacts(input);
// //       updateMemory(extractRes.extracted); // Update memory with the extracted facts

// //       // 2. Update the chat summary (store the latest 5 messages)
// //       updateChatSummary(input);

// //       // 3. Build context for the prompt using the relevant memory, judgement, and summary
// //       const contextRes = await getContextPrompt(
// //         input,
// //         getMemory(),
// //         getJudgement(),
// //         getChatSummary()
// //       );

// //       // 4. Get the final AI reply based on context
// //       const replyRes = await getReply(contextRes.context_prompt);
// //       setReply(replyRes.reply?.content || "Your API reply broke my brain.");
// //     } catch (err) {
// //       console.error("Something exploded 💥:", err);
// //       setReply("Oops, I malfunctioned harder than your ex's logic.");
// //     } finally {
// //       setLoading(false);
// //     }
// //   };

// //   return (
// //     <div className="min-h-screen bg-gray-900 text-white flex flex-col items-center justify-center p-4">
// //       <h1 className="text-3xl font-bold mb-6">💬 JINO.AI</h1>
// //       <textarea
// //         className="w-full max-w-xl p-4 rounded-lg bg-gray-800 mb-4"
// //         rows="4"
// //         placeholder="Tell me something juicy..."
// //         value={input}
// //         onChange={(e) => setInput(e.target.value)}
// //       />
// //       <button
// //         onClick={handleSubmit}
// //         className="bg-purple-600 hover:bg-purple-700 px-6 py-2 rounded-xl text-white font-semibold"
// //         disabled={loading}
// //       >
// //         {loading ? "Thinking..." : "Roast Me 🧠"}
// //       </button>
// //       <div className="mt-6 max-w-xl w-full bg-gray-800 p-4 rounded-lg">
// //         <h2 className="text-lg font-semibold mb-2">🧠 JINO Says:</h2>
// //         <p>{reply || "No roasts yet."}</p>
// //       </div>
// //     </div>
// //   );
// // }

// // export default App;


// import { useState, useEffect } from "react";
// import { getJinoReply } from "./utils/api";

// function App() {
//   const [input, setInput] = useState("");
//   const [reply, setReply] = useState("");
//   const [loading, setLoading] = useState(false);

//   const handleSubmit = async () => {
//     if (!input.trim()) return;

//     setLoading(true);
//     setReply("");

//     try {
//       const res = await getJinoReply(input);
//       console.log("🔁 Full AI Response:", res);
//       setReply(res.reply || "No sass returned.");
//     } catch (err) {
//       console.error("💥 Fatal error:", err);
//       setReply("Something broke harder than your GPA.");
//     } finally {
//       setLoading(false);
//     }
//   };

//   return (
//     <div className="min-h-screen bg-black text-white flex flex-col items-center justify-center p-4">
//       <h1 className="text-4xl font-bold mb-6">💬 JINO.AI</h1>
//       <textarea
//         className="w-full max-w-xl p-4 rounded-lg bg-zinc-900 mb-4"
//         rows="4"
//         placeholder="Spill some tea, and Jino will roast you 💅"
//         value={input}
//         onChange={(e) => setInput(e.target.value)}
//       />
//       <button
//         onClick={handleSubmit}
//         className="bg-pink-600 hover:bg-pink-700 px-6 py-2 rounded-xl text-white font-semibold"
//         disabled={loading}
//       >
//         {loading ? "Typing like a madman..." : "Roast Me 🔥"}
//       </button>
//       <div className="mt-6 max-w-xl w-full bg-zinc-800 p-4 rounded-lg">
//         <h2 className="text-xl font-semibold mb-2">🧠 JINO Says:</h2>
//         <p>{reply || "No shade yet."}</p>
//       </div>
//     </div>
//   );
// }

// export default App;


import { useState, useEffect } from "react";
import { getJinoReply } from "./utils/api";

function App() {
  const [input, setInput] = useState("");
  const [reply, setReply] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    if (!input.trim()) return;

    setLoading(true);
    setReply("");

    try {
      const res = await getJinoReply(input);  // Triggering the full process
      console.log("🔁 Full AI Response:", res);
      setReply(res.reply || "No sass returned.");
    } catch (err) {
      console.error("💥 Fatal error:", err);
      setReply("Something broke harder than your GPA.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-black text-white flex flex-col items-center justify-center p-4">
      <h1 className="text-4xl font-bold mb-6">💬 JINO.AI</h1>
      <textarea
        className="w-full max-w-xl p-4 rounded-lg bg-zinc-900 mb-4"
        rows="4"
        placeholder="Spill some tea, and Jino will roast you 💅"
        value={input}
        onChange={(e) => setInput(e.target.value)}
      />
      <button
        onClick={handleSubmit}
        className="bg-pink-600 hover:bg-pink-700 px-6 py-2 rounded-xl text-white font-semibold"
        disabled={loading}
      >
        {loading ? "Typing like a madman..." : "Roast Me 🔥"}
      </button>
      <div className="mt-6 max-w-xl w-full bg-zinc-800 p-4 rounded-lg">
        <h2 className="text-xl font-semibold mb-2">🧠 JINO Says:</h2>
        <p>{reply || "No shade yet."}</p>
      </div>
    </div>
  );
}

export default App;
