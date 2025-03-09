"""
Configuration settings for the API.
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

USE_MOCK = os.getenv("USE_MOCK", "False").lower() == "true"