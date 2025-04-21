// src/firebase.js

import { initializeApp } from "firebase/app";
import { getAuth, GoogleAuthProvider, signInWithPopup, signOut } from "firebase/auth";

// 🔥 Your config from Firebase Console
const firebaseConfig = {
    apiKey: import.meta.env.VITE_FIREBASE_API_KEY,
    authDomain: "jino-ai.firebaseapp.com",
    projectId: "jino-ai",
    storageBucket: "jino-ai.firebasestorage.app",
    messagingSenderId: "1049252316872",
    appId: "1:1049252316872:web:06d0e8f073ca14bf99c7fd",
    measurementId: "G-WWBW1W9HRW"
  };
  

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const provider = new GoogleAuthProvider();

export { auth, provider, signInWithPopup, signOut };