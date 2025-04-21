import { useState, useRef, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import MessageBubble from './MessageBubble';
import Loader from './Loader';
import { getJinoReply } from '../utils/api';
import { getTokensUsed } from '../utils/localStorage';
import DevPanel from './DevPanel';

const ChatWindow = ({ user }) => {
  const [input, setInput] = useState('');
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);
  const [showDevPanel, setShowDevPanel] = useState(false);
  const [tokenUsage, setTokenUsage] = useState(0);
  const messagesEndRef = useRef(null);
  const textareaRef = useRef(null);

  useEffect(() => {
    // Scroll to bottom whenever messages change
    scrollToBottom();
    
    // Update token usage stats
    setTokenUsage(getTokensUsed());
    
    // Load any saved messages from localStorage
    const savedMessages = localStorage.getItem('jino_messages');
    if (savedMessages) {
      try {
        setMessages(JSON.parse(savedMessages));
      } catch (e) {
        console.error('Failed to parse saved messages', e);
      }
    }
  }, []);

  // Save messages to localStorage whenever they change
  useEffect(() => {
    if (messages.length > 0) {
      localStorage.setItem('jino_messages', JSON.stringify(messages));
    }
  }, [messages]);

  // Auto-resize textarea as user types
  useEffect(() => {
    if (textareaRef.current) {
      textareaRef.current.style.height = 'auto';
      textareaRef.current.style.height = textareaRef.current.scrollHeight + 'px';
    }
  }, [input]);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  const handleSendMessage = async () => {
    if (!input.trim() || loading) return;
    
    const userMessage = {
      id: Date.now(),
      sender: 'user',
      text: input.trim(),
      timestamp: new Date().toISOString(),
    };
    
    setMessages(prev => [...prev, userMessage]);
    setInput('');
    setLoading(true);
    
    // Auto-focus and reset textarea height
    if (textareaRef.current) {
      textareaRef.current.style.height = 'auto';
      textareaRef.current.focus();
    }

    try {
      const response = await getJinoReply(userMessage.text);
      console.log('JINO Response:', response);
      
      // Update token usage
      setTokenUsage(getTokensUsed());
      
      const aiMessage = {
        id: Date.now() + 1,
        sender: 'jino',
        text: response.reply || "Sorry, I think I just had an existential crisis. Can we try again?",
        timestamp: new Date().toISOString(),
        mood: response.mood || 'sarcastic',
        log: response.log || {}
      };
      
      setMessages(prev => [...prev, aiMessage]);
    } catch (error) {
      console.error('Error getting JINO response:', error);
      
      const errorMessage = {
        id: Date.now() + 1,
        sender: 'jino',
        text: "My circuits are fried worse than your fashion sense. Try again later.",
        timestamp: new Date().toISOString(),
        mood: 'error'
      };
      
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setLoading(false);
      // Wait a tick for state to update before scrolling
      setTimeout(scrollToBottom, 100);
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSendMessage();
    }
  };

  const clearChat = () => {
    setMessages([]);
    localStorage.removeItem('jino_messages');
  };

  return (
    <div className="relative h-screen pt-20 pb-6 px-4 md:px-6">
      <div className="max-w-4xl mx-auto h-full flex flex-col">
        {/* Header */}
        <motion.div 
          initial={{ opacity: 0, y: -10 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.2 }}
          className="flex justify-between items-center mb-4"
        >
          <div>
            <h2 className="text-xl font-bold text-offwhite">
              Chat with <span className="text-violet-light">JINO.AI</span>
            </h2>
            <p className="text-sm text-offwhite/60">
              Be prepared for some emotional damage
            </p>
          </div>
          
          <div className="flex items-center gap-2">
            <button 
              onClick={clearChat} 
              className="text-sm text-offwhite/60 hover:text-red-400 transition-colors"
            >
              Clear Chat
            </button>
            <button 
              onClick={() => setShowDevPanel(!showDevPanel)}
              className="text-sm bg-charcoal hover:bg-violet-dark/30 px-3 py-1 rounded transition-colors"
            >
              {showDevPanel ? 'Hide' : 'Show'} Dev Panel
            </button>
          </div>
        </motion.div>
        
        {/* Messages Container */}
        <motion.div 
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          className="flex-1 overflow-y-auto mb-4 bg-charcoal/50 rounded-xl p-4"
        >
          {messages.length === 0 ? (
            <div className="h-full flex flex-col items-center justify-center text-center">
              <span className="text-4xl mb-4">💬</span>
              <h3 className="text-xl font-medium text-offwhite/80 mb-2">Start chatting with JINO</h3>
              <p className="text-sm text-offwhite/60 max-w-sm">
                Ask anything, share your thoughts, or just say hi. JINO has opinions about everything.
              </p>
            </div>
          ) : (
            <AnimatePresence>
              {messages.map((message) => (
                <MessageBubble 
                  key={message.id} 
                  message={message} 
                  isUser={message.sender === 'user'} 
                />
              ))}
            </AnimatePresence>
          )}
          
          {loading && (
            <div className="py-4">
              <Loader />
            </div>
          )}
          
          <div ref={messagesEndRef} />
        </motion.div>
        
        {/* Input Area */}
        <motion.div 
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.4 }}
          className="bg-charcoal rounded-xl p-4"
        >
          <div className="flex items-end gap-3">
            <div className="flex-1 relative">
              <textarea
                ref={textareaRef}
                value={input}
                onChange={(e) => setInput(e.target.value)}
                onKeyDown={handleKeyDown}
                placeholder="Say something to JINO..."
                className="w-full bg-ink border border-violet-deep/30 rounded-lg px-4 py-3 focus:outline-none focus:ring-2 focus:ring-violet-deep/50 text-offwhite resize-none min-h-[60px] max-h-[200px]"
                rows={1}
                disabled={loading}
              />
              <div className="absolute bottom-2 right-2 text-xs text-offwhite/40">
                {loading ? 'Thinking...' : 'Press Enter to send'}
              </div>
            </div>
            
            <motion.button
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.95 }}
              onClick={handleSendMessage}
              disabled={loading || !input.trim()}
              className={`px-5 py-3 rounded-lg font-medium flex items-center gap-2 ${
                loading || !input.trim() 
                  ? 'bg-violet-deep/30 text-offwhite/50 cursor-not-allowed' 
                  : 'bg-violet-deep hover:bg-violet-light text-offwhite'
              }`}
            >
              {loading ? (
                <span>Thinking...</span>
              ) : (
                <>
                  <span>Send</span>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M22 2L11 13" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                    <path d="M22 2L15 22L11 13L2 9L22 2Z" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                  </svg>
                </>
              )}
            </motion.button>
          </div>
          
          {/* Token usage indicator */}
          <div className="mt-3 flex items-center justify-between text-xs text-offwhite/50">
            <div>
              Tokens used: {tokenUsage}
            </div>
            <div>
              Model: Mixtral-8x7B
            </div>
          </div>
        </motion.div>
      </div>
      
      {/* Developer Panel */}
      {showDevPanel && (
        <DevPanel 
          onClose={() => setShowDevPanel(false)} 
          lastMessage={messages.length > 0 ? messages[messages.length - 1] : null}
        />
      )}
    </div>
  );
};

export default ChatWindow;