from openai import OpenAI
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Check if the required environment variables are set
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable is not set")

openai_client = OpenAI(
    api_key=OPENAI_API_KEY, 
)