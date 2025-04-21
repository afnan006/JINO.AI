import { motion } from 'framer-motion';
import { useState, useEffect } from 'react';
import { 
  getMemory,
  getJudgement,
  getConvoSummary,
  getTokensUsed,
  listJinoStorageKeys
} from '../utils/localStorage';
import TokenStats from './TokenStats';

const DevPanel = ({ onClose, lastMessage }) => {
  const [memory, setMemory] = useState({});
  const [judgement, setJudgement] = useState({});
  const [convoSummary, setConvoSummary] = useState([]);
  const [storageKeys, setStorageKeys] = useState([]);
  const [activeTab, setActiveTab] = useState('memory');

  useEffect(() => {
    // Load data
    setMemory(getMemory());
    setJudgement(getJudgement());
    setConvoSummary(getConvoSummary());
    setStorageKeys(listJinoStorageKeys());

    // Refresh on interval
    const interval = setInterval(() => {
      setMemory(getMemory());
      setJudgement(getJudgement());
      setConvoSummary(getConvoSummary());
      setStorageKeys(listJinoStorageKeys());
    }, 2000);

    return () => clearInterval(interval);
  }, []);

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      exit={{ opacity: 0, y: 20 }}
      className="fixed bottom-0 left-0 right-0 bg-charcoal border-t border-violet-deep/30 shadow-lg shadow-violet-deep/10 z-10"
      style={{ height: '50vh' }}
    >
      <div className="flex justify-between items-center p-3 border-b border-violet-deep/20">
        <h3 className="font-semibold text-violet-light">JINO.AI Developer Panel</h3>
        <button 
          onClick={onClose}
          className="text-offwhite/60 hover:text-offwhite"
        >
          Close
        </button>
      </div>

      {/* Tabs */}
      <div className="flex border-b border-violet-deep/20">
        <button 
          onClick={() => setActiveTab('memory')}
          className={`px-4 py-2 ${activeTab === 'memory' ? 'bg-violet-deep/20 text-violet-light' : 'text-offwhite/60'}`}
        >
          Memory
        </button>
        <button 
          onClick={() => setActiveTab('judgement')}
          className={`px-4 py-2 ${activeTab === 'judgement' ? 'bg-violet-deep/20 text-violet-light' : 'text-offwhite/60'}`}
        >
          Judgement
        </button>
        <button 
          onClick={() => setActiveTab('conversation')}
          className={`px-4 py-2 ${activeTab === 'conversation' ? 'bg-violet-deep/20 text-violet-light' : 'text-offwhite/60'}`}
        >
          Conversation
        </button>
        <button 
          onClick={() => setActiveTab('api')}
          className={`px-4 py-2 ${activeTab === 'api' ? 'bg-violet-deep/20 text-violet-light' : 'text-offwhite/60'}`}
        >
          API & Tokens
        </button>
        <button 
          onClick={() => setActiveTab('storage')}
          className={`px-4 py-2 ${activeTab === 'storage' ? 'bg-violet-deep/20 text-violet-light' : 'text-offwhite/60'}`}
        >
          Storage
        </button>
      </div>

      {/* Content */}
      <div className="p-4 overflow-y-auto" style={{ height: 'calc(50vh - 80px)' }}>
        {activeTab === 'memory' && (
          <div>
            <h4 className="text-violet-light mb-3 text-sm font-semibold">User Memory (Facts)</h4>
            {Object.keys(memory).length > 0 ? (
              <pre className="bg-ink rounded p-3 text-xs overflow-x-auto">
                {JSON.stringify(memory, null, 2)}
              </pre>
            ) : (
              <p className="text-offwhite/50 text-sm">No memory stored yet</p>
            )}
          </div>
        )}

        {activeTab === 'judgement' && (
          <div>
            <h4 className="text-violet-light mb-3 text-sm font-semibold">JINO's Judgement (Emotional)</h4>
            {Object.keys(judgement).length > 0 ? (
              <pre className="bg-ink rounded p-3 text-xs overflow-x-auto">
                {JSON.stringify(judgement, null, 2)}
              </pre>
            ) : (
              <p className="text-offwhite/50 text-sm">No judgements stored yet</p>
            )}
          </div>
        )}

        {activeTab === 'conversation' && (
          <div>
            <h4 className="text-violet-light mb-3 text-sm font-semibold">Conversation Summary</h4>
            {convoSummary.length > 0 ? (
              <pre className="bg-ink rounded p-3 text-xs overflow-x-auto">
                {JSON.stringify(convoSummary, null, 2)}
              </pre>
            ) : (
              <p className="text-offwhite/50 text-sm">No conversation summary yet</p>
            )}
          </div>
        )}

        {activeTab === 'api' && (
          <div>
            <TokenStats />
            
            <h4 className="text-violet-light mb-3 mt-6 text-sm font-semibold">Last Response</h4>
            {lastMessage?.log ? (
              <pre className="bg-ink rounded p-3 text-xs overflow-x-auto">
                {JSON.stringify(lastMessage.log, null, 2)}
              </pre>
            ) : (
              <p className="text-offwhite/50 text-sm">No API response data available</p>
            )}
            
            <div className="mt-4 bg-violet-deep/10 p-3 rounded text-xs">
              <p className="font-medium text-violet-light mb-1">API Endpoints</p>
              <ul className="list-disc list-inside space-y-1 text-offwhite/70">
                <li>/extract - Extracts facts and judgement</li>
                <li>/context - Builds context for the AI</li>
                <li>/reply - Generates JINO's response</li>
              </ul>
            </div>
          </div>
        )}
        
        {activeTab === 'storage' && (
          <div>
            <h4 className="text-violet-light mb-3 text-sm font-semibold">LocalStorage Keys</h4>
            {storageKeys.length > 0 ? (
              <ul className="bg-ink rounded p-3 text-xs">
                {storageKeys.map(key => (
                  <li key={key} className="mb-1 flex items-center">
                    <span className="text-violet-light mr-2">→</span> {key}
                  </li>
                ))}
              </ul>
            ) : (
              <p className="text-offwhite/50 text-sm">No JINO storage keys found</p>
            )}
          </div>
        )}
      </div>
    </motion.div>
  );
};

export default DevPanel;