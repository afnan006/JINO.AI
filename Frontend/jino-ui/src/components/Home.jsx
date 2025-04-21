import { motion } from 'framer-motion';
import { useNavigate } from 'react-router-dom';
import { useEffect } from 'react';
import LoginModal from './LoginModal';
import { useState } from 'react';

const Home = ({ user }) => {
  const navigate = useNavigate();
  const [showLoginModal, setShowLoginModal] = useState(false);

  // If user is logged in, redirect to chat
  useEffect(() => {
    if (user) {
      navigate('/chat');
    }
  }, [user, navigate]);

  const containerVariants = {
    hidden: { opacity: 0 },
    visible: {
      opacity: 1,
      transition: {
        staggerChildren: 0.2
      }
    }
  };

  const itemVariants = {
    hidden: { y: 20, opacity: 0 },
    visible: {
      y: 0,
      opacity: 1,
      transition: { duration: 0.5 }
    }
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center p-6 bg-gradient-to-b from-ink to-charcoal">
      <motion.div 
        className="max-w-3xl mx-auto text-center"
        variants={containerVariants}
        initial="hidden"
        animate="visible"
      >
        <motion.div 
          variants={itemVariants}
          className="mb-4 flex justify-center"
        >
          <span className="text-6xl">💬</span>
        </motion.div>
        
        <motion.h1 
          variants={itemVariants}
          className="text-5xl md:text-6xl font-bold font-poppins mb-6 text-transparent bg-clip-text bg-gradient-to-r from-violet-light to-violet-deep"
        >
          Meet JINO.AI
        </motion.h1>
        
        <motion.p 
          variants={itemVariants}
          className="text-xl md:text-2xl mb-8 max-w-2xl mx-auto text-offwhite/90"
        >
          The sarcastic AI assistant with attitude, memory, and emotions. It's like talking to that friend who never holds back.
        </motion.p>

        <motion.div variants={itemVariants} className="mb-12 flex flex-wrap justify-center gap-4">
          <div className="bg-charcoal p-4 rounded-lg flex items-center gap-3 text-left">
            <span className="text-2xl">🧠</span>
            <span>Remembers your conversations</span>
          </div>
          <div className="bg-charcoal p-4 rounded-lg flex items-center gap-3 text-left">
            <span className="text-2xl">😏</span>
            <span>Sassy responses guaranteed</span>
          </div>
          <div className="bg-charcoal p-4 rounded-lg flex items-center gap-3 text-left">
            <span className="text-2xl">🔥</span>
            <span>Brutally honest feedback</span>
          </div>
        </motion.div>
        
        <motion.div variants={itemVariants}>
          <motion.button
            whileHover={{ scale: 1.05, backgroundColor: '#A855F7' }}
            whileTap={{ scale: 0.95 }}
            onClick={() => setShowLoginModal(true)}
            className="bg-violet-deep hover:bg-violet-light text-white px-8 py-3 rounded-xl font-bold text-lg transition-colors shadow-lg shadow-violet-deep/20"
          >
            Get Started
          </motion.button>
        </motion.div>

        <motion.p
          variants={itemVariants}
          className="mt-8 text-offwhite/60 text-sm"
        >
          Be ready for some tough love. JINO doesn't sugar-coat anything.
        </motion.p>
      </motion.div>

      {showLoginModal && !user && (
        <LoginModal onClose={() => setShowLoginModal(false)} />
      )}
    </div>
  );
};

export default Home;