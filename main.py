from fastapi import FastAPI
from pydantic import BaseModel
import os
from openai import OpenAI

# Import mock responses
from mock_responses import get_mock_response

# Flag to determine if we should use mock responses
USE_MOCK = os.environ.get("USE_MOCK", "false").lower() == "true"

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"), 
)

app = FastAPI()

class IdeaRequest(BaseModel):
    idea_text: str
    # action: str  # "expand", "summarize", "improve"

@app.get("/")
async def root():
  return {"message": "Hello from Mindtaker!"}

@app.post("/expand-idea")
async def expand_idea(request: IdeaRequest):
    # Use mock response if configured
    if USE_MOCK:
        return {"result": get_mock_response("expand-idea", request.idea_text)}
    
    # Otherwise use the real OpenAI client
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[ 
            {"role": "developer", "content": "Expand and refine user ideas with creative suggestions."},
            {"role": "user", "content": f"My idea is: {request.idea_text}"}
          ]
    )
    if response.choices and len(response.choices) > 0:
        return {"result": response.choices[0].message.content}
    return {"error": "No response from the model"}