from fastapi import FastAPI, HTTPException, Depends
from openai import OpenAI

# Import from separated modules
from models import IdeaRequest
from config import USE_MOCK, OPENAI_API_KEY, AI_SYSTEM_MESSAGES
from mock_responses import get_mock_response
from auth import get_current_user

openai_client = OpenAI(
    api_key=OPENAI_API_KEY, 
)

app = FastAPI()

@app.get("/")
async def root():
  return {"message": "Hello from Mindtaker!"}

@app.post("/idea-action")
async def process_idea(request: IdeaRequest, user=Depends(get_current_user)):
    # Use mock response if configured
    if USE_MOCK:
        return {"result": get_mock_response(request.action, request.idea_text)}
    
    # Get the appropriate system message
    system_message = AI_SYSTEM_MESSAGES.get(request.action)
    if not system_message:
        raise HTTPException(status_code=400, detail="Invalid action specified")
    
    # Use the real OpenAI client with the appropriate system message
    response = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[ 
            {"role": "developer", "content": system_message},
            {"role": "user", "content": f"My idea is: {request.idea_text}"}
          ]
    )
    if response.choices and len(response.choices) > 0:
        return {"result": response.choices[0].message.content}
    return {"error": "No response from the model"}