# import os
# from dotenv import load_dotenv

# load_dotenv()  # Loads from .env automatically

# class Config:
#     OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
#     COHERE_API_KEY = os.getenv("COHERE_API_KEY")
#     OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
#     GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")    

import os
from dotenv import load_dotenv

load_dotenv()  # Loads from .env automatically

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")  # For session management, etc.
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    COHERE_API_KEY = os.getenv("COHERE_API_KEY")
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
