// Format date to time string (e.g., "10:30 AM")
export const formatTime = (date) => {
    if (!date) return ''
    
    // If date is a string, convert to Date object
    const dateObj = typeof date === 'string' ? new Date(date) : date
    
    return dateObj.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
  }
  
  // Format date to full date string (e.g., "Jan 1, 2023")
  export const formatDate = (date) => {
    if (!date) return ''
    
    // If date is a string, convert to Date object
    const dateObj = typeof date === 'string' ? new Date(date) : date
    
    return dateObj.toLocaleDateString([], { 
      month: 'short', 
      day: 'numeric', 
      year: 'numeric' 
    })
  }
  
  // Truncate text to specified length
  export const truncateText = (text, maxLength = 100) => {
    if (!text || text.length <= maxLength) return text
    
    return text.substring(0, maxLength) + '...'
  }
  
  // Get random item from array
  export const getRandomItem = (array) => {
    if (!array || array.length === 0) return null
    
    return array[Math.floor(Math.random() * array.length)]
  }
  
  // Debounce function for performance optimization
  export const debounce = (func, wait = 300) => {
    let timeout
    
    return function executedFunction(...args) {
      const later = () => {
        clearTimeout(timeout)
        func(...args)
      }
      
      clearTimeout(timeout)
      timeout = setTimeout(later, wait)
    }
  }
  
  // Generate a unique ID (simple version, not for security purposes)
  export const generateId = () => {
    return Date.now().toString(36) + Math.random().toString(36).substring(2)
  }
  
  // Check if an object is empty
  export const isEmptyObject = (obj) => {
    return obj && Object.keys(obj).length === 0 && obj.constructor === Object
  }
  
  // Safely parse JSON with error handling
  export const safeJsonParse = (jsonString, fallback = {}) => {
    try {
      return JSON.parse(jsonString)
    } catch (error) {
      console.error('Error parsing JSON:', error)
      return fallback
    }
  }
  
  // Format number with commas
  export const formatNumber = (num) => {
    return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")
  }