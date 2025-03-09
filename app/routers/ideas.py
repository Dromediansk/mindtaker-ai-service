from fastapi import APIRouter, HTTPException, Depends

from app.init import USE_MOCK
from app.utils import AI_SYSTEM_MESSAGES, IdeaRequest, get_mock_response
from app.auth import get_current_user
from app.openai import openai_client

ideas_router = APIRouter(prefix="/ideas")

@ideas_router.post("/action")
async def process_idea(request: IdeaRequest, user=Depends(get_current_user)):
    # Use mock response if configured
    if USE_MOCK:
        return {"result": get_mock_response(request.action)}
    
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
