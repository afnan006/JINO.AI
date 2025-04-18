// App.jsx
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
