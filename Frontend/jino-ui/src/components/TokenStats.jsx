import { useEffect, useState } from 'react';
import { getTokensUsed } from '../utils/localStorage';
import { motion } from 'framer-motion';

const TokenStats = () => {
  const [tokens, setTokens] = useState(0);
  const [percentage, setPercentage] = useState(0);
  
  // Define token limits
  const tokenLimit = 100000; // Example limit
  
  useEffect(() => {
    // Initial load
    const currentTokens = getTokensUsed();
    setTokens(currentTokens);
    setPercentage(Math.min((currentTokens / tokenLimit) * 100, 100));
    
    // Set up interval to refresh
    const interval = setInterval(() => {
      const updatedTokens = getTokensUsed();
      setTokens(updatedTokens);
      setPercentage(Math.min((updatedTokens / tokenLimit) * 100, 100));
    }, 2000);
    
    return () => clearInterval(interval);
  }, []);
  
  // Determine color based on percentage
  const getBarColor = () => {
    if (percentage < 50) return 'bg-green-500';
    if (percentage < 80) return 'bg-yellow-500';
    return 'bg-red-500';
  };

  return (
    <div className="bg-charcoal/50 rounded-lg p-4">
      <div className="flex items-center justify-between mb-2">
        <h3 className="text-sm font-medium text-offwhite">Token Usage</h3>
        <span className="text-xs text-offwhite/70">
          {tokens.toLocaleString()} / {tokenLimit.toLocaleString()}
        </span>
      </div>
      
      <div className="h-2 bg-ink rounded-full overflow-hidden">
        <motion.div 
          className={`h-full ${getBarColor()}`}
          initial={{ width: 0 }}
          animate={{ width: `${percentage}%` }}
          transition={{ duration: 0.5 }}
        />
      </div>
      
      <div className="mt-4 text-xs grid grid-cols-2 gap-2">
        <div className="bg-ink/50 p-2 rounded">
          <span className="block text-offwhite/70">Model</span>
          <span className="font-medium">Mixtral-8x7B</span>
        </div>
        <div className="bg-ink/50 p-2 rounded">
          <span className="block text-offwhite/70">Cost Estimate</span>
          <span className="font-medium">${(tokens / 1000 * 0.0007).toFixed(4)}</span>
        </div>
      </div>
    </div>
  );
};

export default TokenStats;