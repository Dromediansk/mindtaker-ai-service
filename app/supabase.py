from supabase import create_client
import os

SUPABASE_JWT_SECRET = os.getenv("SUPABASE_JWT_SECRET")
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Check all supabase environment variables
if not all([SUPABASE_JWT_SECRET, SUPABASE_URL, SUPABASE_KEY]):
    raise ValueError("One or more Supabase environment variables are not set")

supabase_client = create_client(SUPABASE_URL, SUPABASE_KEY)