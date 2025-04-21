import { motion } from 'framer-motion';

const Loader = () => {
  return (
    <div className="flex justify-center items-center py-2">
      <div className="typing-indicator">
        <motion.span
          initial={{ y: 0 }}
          animate={{ y: [0, -5, 0] }}
          transition={{ 
            repeat: Infinity, 
            duration: 0.6,
            delay: 0
          }}
        />
        <motion.span
          initial={{ y: 0 }}
          animate={{ y: [0, -5, 0] }}
          transition={{ 
            repeat: Infinity, 
            duration: 0.6,
            delay: 0.2
          }}
        />
        <motion.span
          initial={{ y: 0 }}
          animate={{ y: [0, -5, 0] }}
          transition={{ 
            repeat: Infinity, 
            duration: 0.6,
            delay: 0.4
          }}
        />
      </div>
      <motion.p 
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 1, duration: 0.3 }}
        className="ml-3 text-sm text-offwhite/60"
      >
        JINO is thinking...
      </motion.p>
    </div>
  );
};

export default Loader;