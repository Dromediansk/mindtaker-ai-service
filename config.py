"""
Configuration settings for the API.
"""
import os

# Flag to determine if we should use mock responses
USE_MOCK = os.environ.get("USE_MOCK", "false").lower() == "true"

# OpenAI API key
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# System messages for different idea actions
AI_SYSTEM_MESSAGES = {
    "expand": "Expand and refine user ideas with creative suggestions and more details.",
    "summarize": "Provide a clear, concise summary of the user's idea, highlighting the key points.",
    "improve": "Analyze the user's idea and suggest specific improvements and enhancements."
}
