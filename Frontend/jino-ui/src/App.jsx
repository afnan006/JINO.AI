// import { useState, useEffect } from "react";
// import { getJinoReply } from "./utils/api";
// import { getConvoSummary, updateConvoSummary } from "./utils/localStorage";
// import { auth, provider, signInWithPopup, signOut } from "./firebase";

// function App() {
//   const [input, setInput] = useState("");
//   const [reply, setReply] = useState("");
//   const [loading, setLoading] = useState(false);
//   const [conversation, setConversation] = useState([]);
//   const [user, setUser] = useState(null);

//   // On mount: check if user is logged in
//   useEffect(() => {
//     try {
//       const saved = JSON.parse(localStorage.getItem("jino_user"));
//       if (saved?.firebase_uid) {
//         setUser(saved);
//         const summary = getConvoSummary();
//         setConversation(summary);
//       }
//     } catch (err) {
//       console.error("🧨 Failed to load saved user:", err);
//     }
//   }, []);

//   const handleLogin = async () => {
//     try {
//       const result = await signInWithPopup(auth, provider);
//       const firebaseUser = result.user;
//       const uid = firebaseUser.uid;
//       const name = firebaseUser.displayName;
//       const email = firebaseUser.email;

//       const uuid = crypto.randomUUID();

//       const userData = {
//         firebase_uid: uid,
//         jino_user_id: uuid,
//         name,
//         email,
//       };

//       localStorage.setItem("jino_user", JSON.stringify(userData));
//       setUser(userData);
//       console.log("✅ Logged in:", userData);
//     } catch (err) {
//       console.error("❌ Login failed:", err);
//     }
//   };

//   const handleLogout = () => {
//     signOut(auth)
//       .then(() => {
//         localStorage.removeItem("jino_user");
//         setUser(null);
//         setConversation([]);
//         console.log("👋 Logged out");
//       })
//       .catch((err) => {
//         console.error("⚠️ Logout failed:", err);
//       });
//   };

//   const handleSubmit = async () => {
//     if (!input.trim() || !user) return;

//     setLoading(true);
//     setReply("");

//     try {
//       const userMessage = {
//         message: input,
//         time: new Date().toLocaleTimeString(),
//       };

//       updateConvoSummary(userMessage);
//       setConversation((prev) => [...prev, userMessage]);

//       const res = await getJinoReply(input);
//       console.log("🔁 Full AI Response:", res);

//       const aiMessage = {
//         message: res.reply || "No sass returned.",
//         time: new Date().toLocaleTimeString(),
//       };

//       updateConvoSummary(aiMessage);
//       setConversation((prev) => [...prev, aiMessage]);
//       setReply(res.reply || "No sass returned.");
//     } catch (err) {
//       console.error("💥 Fatal error:", err);
//       setReply("Something broke harder than your GPA.");
//     } finally {
//       setLoading(false);
//       setInput("");
//     }
//   };

//   return (
//     <div className="min-h-screen bg-black text-white flex flex-col items-center justify-center p-4">
//       <h1 className="text-4xl font-bold mb-6">💬 JINO.AI</h1>

//       {!user ? (
//         <>
//           <p className="mb-4 text-red-500">You must sign in with Google to chat with JINO 😎</p>
//           <button
//             onClick={handleLogin}
//             className="bg-blue-600 hover:bg-blue-700 px-6 py-2 rounded-xl text-white font-semibold mb-6"
//           >
//             Sign In with Google
//           </button>
//         </>
//       ) : (
//         <>
//           <div className="flex items-center justify-between w-full max-w-xl mb-4">
//             <p className="text-sm text-gray-400">
//               Logged in as <span className="text-pink-400">{user.name}</span>
//             </p>
//             <button
//               onClick={handleLogout}
//               className="text-sm text-red-500 underline hover:text-red-400"
//             >
//               Logout
//             </button>
//           </div>

//           {/* Conversation History */}
//           <div className="w-full max-w-xl bg-zinc-800 p-4 rounded-lg mb-4 overflow-y-auto max-h-96">
//             {conversation.map((msg, index) => (
//               <div key={index} className={`mb-4 ${index % 2 === 0 ? "text-right" : "text-left"}`}>
//                 <div
//                   className={`inline-block p-3 rounded-lg ${
//                     index % 2 === 0 ? "bg-pink-600 text-white" : "bg-zinc-900 text-white"
//                   }`}
//                 >
//                   <p>{msg.message}</p>
//                   <p className="text-xs text-gray-400">{msg.time}</p>
//                 </div>
//               </div>
//             ))}
//           </div>

//           {/* Message Input */}
//           <textarea
//             className="w-full max-w-xl p-4 rounded-lg bg-zinc-900 mb-4"
//             rows="4"
//             placeholder="Spill some tea, and Jino will roast you 💅"
//             value={input}
//             onChange={(e) => setInput(e.target.value)}
//             disabled={loading}
//           />

//           {/* Send Button */}
//           <button
//             onClick={handleSubmit}
//             className="bg-pink-600 hover:bg-pink-700 px-6 py-2 rounded-xl text-white font-semibold"
//             disabled={loading}
//           >
//             {loading ? "Typing like a madman..." : "Roast Me 🔥"}
//           </button>

//           {/* JINO's Reply */}
//           <div className="mt-6 max-w-xl w-full bg-zinc-800 p-4 rounded-lg">
//             <h2 className="text-xl font-semibold mb-2">🧠 JINO Says:</h2>
//             <p>{reply || "No shade yet."}</p>
//           </div>
//         </>
//       )}
//     </div>
//   );
// }

// export default App;

import { useState, useEffect } from 'react'
import { Routes, Route, Navigate } from 'react-router-dom'
import Navbar from './components/Navbar'
import Home from './components/Home'
import ChatWindow from './components/ChatWindow'
import { motion } from 'framer-motion'

function App() {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  // Check if user is logged in
  useEffect(() => {
    const checkAuth = () => {
      try {
        const savedUser = JSON.parse(localStorage.getItem('jino_user'));
        if (savedUser?.firebase_uid) {
          setUser(savedUser);
        }
      } catch (err) {
        console.error("Failed to load user data:", err);
      } finally {
        setLoading(false);
      }
    };

    checkAuth();
    
    // Listen for auth changes from other tabs/windows
    window.addEventListener('storage', (event) => {
      if (event.key === 'jino_user') {
        checkAuth();
      }
    });
  }, []);

  const handleLogout = () => {
    localStorage.removeItem('jino_user');
    setUser(null);
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-screen bg-ink">
        <div className="flex flex-col items-center">
          <motion.span 
            initial={{ scale: 0.8, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            transition={{ duration: 0.5 }}
            className="text-6xl mb-4"
          >
            💬
          </motion.span>
          <motion.p
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 0.3 }}
            className="text-violet-light"
          >
            Loading JINO.AI...
          </motion.p>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-ink">
      <Navbar user={user} onLogout={handleLogout} />
      
      <Routes>
        <Route path="/" element={<Home user={user} />} />
        <Route 
          path="/chat" 
          element={
            user ? <ChatWindow user={user} /> : <Navigate to="/" replace />
          } 
        />
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </div>
  );
}

export default App;