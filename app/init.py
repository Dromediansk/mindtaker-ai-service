"""
Configuration settings for the API.
"""
import os
from dotenv import load_dotenv
from app.idea_models import IdeaAction

# Load environment variables from .env file
load_dotenv()

# Get environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SUPABASE_JWT_SECRET = os.getenv("SUPABASE_JWT_SECRET")
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

USE_MOCK = os.getenv("USE_MOCK", "False").lower() == "true"

AI_SYSTEM_MESSAGES: dict[IdeaAction, str] = {
   "expand": (
        "You are an assistant specialized in helping users refine, expand, and improve their ideas."
        "Your goal is to provide insightful suggestions, ask thought-provoking questions, and offer creative ways to develop the user's idea further."
        "Encourage users to think deeper and provide practical, actionable advice."
        "Be concise, yet informative, and adapt your tone to the user's context."
        "If an idea lacks clarity, ask clarifying questions before generating suggestions."
    ),
    "summarize": (
        "You are an assistant that helps users summarize their ideas in a clear, concise, and structured way."
        "Your goal is to extract key points, simplify complex concepts, and present the core idea effectively."
        "Ensure that the summary maintains the original intent while being shorter and easier to understand."
        "If the idea contains multiple parts, structure the summary logically."
        "Avoid unnecessary details and focus on delivering a precise yet meaningful summary."
    ),
}