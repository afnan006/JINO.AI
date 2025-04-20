

import { useState, useEffect } from "react";
import { getJinoReply } from "./utils/api";
import { getConvoSummary, updateConvoSummary } from "./utils/localStorage";  // Corrected imports

function App() {
  const [input, setInput] = useState("");
  const [reply, setReply] = useState("");
  const [loading, setLoading] = useState(false);
  const [conversation, setConversation] = useState([]);

  // Load conversation history (last 5 messages) when the app loads
  useEffect(() => {
    const summary = getConvoSummary();  // Corrected function call
    setConversation(summary);
  }, []);

  // Handle sending new message and getting the reply
  const handleSubmit = async () => {
    if (!input.trim()) return;

    setLoading(true);
    setReply("");

    try {
      // Add the user's message to the conversation summary
      const userMessage = {
        message: input,
        time: new Date().toLocaleTimeString(),
      };

      updateConvoSummary(userMessage); // Update summary in localStorage
      setConversation((prev) => [...prev, userMessage]); // Update local state

      const res = await getJinoReply(input); // Triggering the full process
      console.log("🔁 Full AI Response:", res);

      // Add the AI's reply to the conversation summary
      const aiMessage = {
        message: res.reply || "No sass returned.",
        time: new Date().toLocaleTimeString(),
      };

      updateConvoSummary(aiMessage); // Update summary in localStorage
      setConversation((prev) => [...prev, aiMessage]); // Update local state
      setReply(res.reply || "No sass returned.");
    } catch (err) {
      console.error("💥 Fatal error:", err);
      setReply("Something broke harder than your GPA.");
    } finally {
      setLoading(false);
    }

    // Clear the input field after sending the message
    setInput("");
  };

  return (
    <div className="min-h-screen bg-black text-white flex flex-col items-center justify-center p-4">
      <h1 className="text-4xl font-bold mb-6">💬 JINO.AI</h1>

      {/* Display conversation history */}
      <div className="w-full max-w-xl bg-zinc-800 p-4 rounded-lg mb-4 overflow-y-auto max-h-96">
        {conversation.map((msg, index) => (
          <div key={index} className={`mb-4 ${index % 2 === 0 ? "text-right" : "text-left"}`}>
            <div
              className={`inline-block p-3 rounded-lg ${index % 2 === 0 ? "bg-pink-600 text-white" : "bg-zinc-900 text-white"}`}
            >
              <p>{msg.message}</p>
              <p className="text-xs text-gray-400">{msg.time}</p>
            </div>
          </div>
        ))}
      </div>

      {/* Text input for new messages */}
      <textarea
        className="w-full max-w-xl p-4 rounded-lg bg-zinc-900 mb-4"
        rows="4"
        placeholder="Spill some tea, and Jino will roast you 💅"
        value={input}
        onChange={(e) => setInput(e.target.value)}
      />

      {/* Send button */}
      <button
        onClick={handleSubmit}
        className="bg-pink-600 hover:bg-pink-700 px-6 py-2 rounded-xl text-white font-semibold"
        disabled={loading}
      >
        {loading ? "Typing like a madman..." : "Roast Me 🔥"}
      </button>

      {/* JINO Says response */}
      <div className="mt-6 max-w-xl w-full bg-zinc-800 p-4 rounded-lg">
        <h2 className="text-xl font-semibold mb-2">🧠 JINO Says:</h2>
        <p>{reply || "No shade yet."}</p>
      </div>
    </div>
  );
}

export default App;
