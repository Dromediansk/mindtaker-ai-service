import uvicorn
from fastapi import FastAPI, HTTPException, Depends
from openai import OpenAI
from fastapi.middleware.cors import CORSMiddleware

# Import from separated modules
from app.init import USE_MOCK, OPENAI_API_KEY, AI_SYSTEM_MESSAGES
from app.idea_models import IdeaRequest
from app.ai_response_mocks import get_mock_response
from app.auth import get_current_user

openai_client = OpenAI(
    api_key=OPENAI_API_KEY, 
)

app = FastAPI()

# # Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # TODO: Change this to the actual frontend URL
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

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

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000)