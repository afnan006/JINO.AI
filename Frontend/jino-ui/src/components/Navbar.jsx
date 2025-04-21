import { motion } from 'framer-motion';
import { Link } from 'react-router-dom';
import LoginModal from './LoginModal';
import { useState } from 'react';

const Navbar = ({ user, onLogout }) => {
  const [showLoginModal, setShowLoginModal] = useState(false);

  return (
    <motion.nav 
      initial={{ y: -20, opacity: 0 }}
      animate={{ y: 0, opacity: 1 }}
      transition={{ duration: 0.5 }}
      className="fixed top-0 left-0 right-0 z-50 bg-ink/80 backdrop-blur-md border-b border-violet-deep/20 py-4 px-6"
    >
      <div className="container mx-auto flex justify-between items-center">
        <Link to="/" className="flex items-center">
          <motion.div
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
            className="flex items-center"
          >
            <span className="text-3xl mr-2">💬</span>
            <span className="font-poppins font-bold text-2xl bg-gradient-to-r from-violet-light to-violet-deep bg-clip-text text-transparent">
              JINO.AI
            </span>
          </motion.div>
        </Link>

        <div className="flex items-center space-x-4">
          {user ? (
            <div className="flex items-center gap-4">
              <motion.div 
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                className="hidden md:flex items-center gap-2"
              >
                <img 
                  src={user.photoURL || `https://ui-avatars.com/api/?name=${user.name}&background=7E22CE&color=fff`} 
                  alt={user.name} 
                  className="w-8 h-8 rounded-full border-2 border-violet-deep"
                />
                <span className="text-sm font-medium">{user.name}</span>
              </motion.div>
              
              <motion.button
                whileHover={{ scale: 1.05, backgroundColor: '#7E22CE' }}
                whileTap={{ scale: 0.95 }}
                onClick={onLogout}
                className="bg-violet-dark hover:bg-violet-deep text-white px-4 py-2 rounded-lg text-sm font-medium transition-colors"
              >
                Logout
              </motion.button>
            </div>
          ) : (
            <motion.button
              whileHover={{ scale: 1.05, backgroundColor: '#A855F7' }}
              whileTap={{ scale: 0.95 }}
              onClick={() => setShowLoginModal(true)}
              className="bg-violet-deep hover:bg-violet-light text-white px-6 py-2 rounded-lg font-medium transition-colors"
            >
              Get Started
            </motion.button>
          )}
        </div>
      </div>

      {showLoginModal && !user && (
        <LoginModal onClose={() => setShowLoginModal(false)} />
      )}
    </motion.nav>
  );
};

export default Navbar;