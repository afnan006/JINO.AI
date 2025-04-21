import { motion } from 'framer-motion';
import { useState } from 'react';

const MessageBubble = ({ message, isUser }) => {
  const [showDetails, setShowDetails] = useState(false);
  
  // Format timestamp to readable time
  const formatTime = (timestamp) => {
    try {
      const date = new Date(timestamp);
      return date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    } catch (e) {
      return 'Just now';
    }
  };
  
  // Determine mood emoji
  const getMoodEmoji = (mood) => {
    switch(mood) {
      case 'sarcastic': return '😏';
      case 'angry': return '😡';
      case 'excited': return '🤩';
      case 'confused': return '🤨';
      case 'unimpressed': return '😒';
      case 'empathetic': return '🧠';
      case 'error': return '💥';
      default: return '🤖';
    }
  };
  
  const bubbleVariants = {
    initial: { 
      opacity: 0, 
      y: 10,
      x: isUser ? 20 : -20 
    },
    animate: { 
      opacity: 1, 
      y: 0,
      x: 0,
      transition: { 
        type: "spring", 
        stiffness: 500, 
        damping: 30 
      } 
    },
    exit: { 
      opacity: 0,
      transition: { duration: 0.2 } 
    }
  };

  return (
    <motion.div
      variants={bubbleVariants}
      initial="initial"
      animate="animate"
      exit="exit"
      className={`mb-4 ${isUser ? 'ml-auto' : 'mr-auto'} max-w-[85%]`}
    >
      <div 
        className={`
          flex flex-col 
          ${isUser ? 'items-end' : 'items-start'}
        `}
      >
        {/* Message bubble */}
        <div 
          className={`
            rounded-2xl px-4 py-3
            ${isUser 
              ? 'bg-violet-dark text-white rounded-tr-none' 
              : 'bg-gradient-to-br from-charcoal to-charcoal/80 text-offwhite border border-violet-deep/20 rounded-tl-none'
            }
          `}
        >
          {/* Message content */}
          <p className="whitespace-pre-wrap break-words">{message.text}</p>
          
          {/* Show mood indicator for JINO messages */}
          {!isUser && message.mood && (
            <div 
              onClick={() => setShowDetails(!showDetails)}
              className="mt-2 text-xs flex items-center gap-1 text-offwhite/70 cursor-pointer hover:text-violet-light transition-colors"
            >
              {getMoodEmoji(message.mood)} <span>{message.mood}</span>
            </div>
          )}
          
          {/* Advanced message details (for debugging) */}
          {!isUser && showDetails && message.log && (
            <div className="mt-2 text-xs border-t border-violet-deep/20 pt-2 text-offwhite/60">
              <div className="font-mono overflow-x-auto max-h-32 scrollbar-thin">
                <pre>{JSON.stringify(message.log, null, 2)}</pre>
              </div>
            </div>
          )}
        </div>
        
        {/* Message timestamp */}
        <div 
          className={`
            text-xs mt-1 text-offwhite/50
            ${isUser ? 'text-right' : 'text-left'}
          `}
        >
          {formatTime(message.timestamp)}
        </div>
      </div>
    </motion.div>
  );
};

export default MessageBubble;