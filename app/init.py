"""
Configuration settings for the API.
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SUPABASE_JWT_SECRET = os.getenv("SUPABASE_JWT_SECRET")
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

USE_MOCK = os.getenv("USE_MOCK", "False").lower() == "true"

# Other configuration variables
AI_SYSTEM_MESSAGES = {
    "expand": "Expand and refine user ideas with creative suggestions and more details.",
    "summarize": "Provide a clear, concise summary of the user's idea, highlighting the key points.",
    "improve": "Analyze the user's idea and suggest specific improvements and enhancements."
}
