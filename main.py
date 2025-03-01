from fastapi import FastAPI
from pydantic import BaseModel
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)

app = FastAPI()

class IdeaRequest(BaseModel):
    idea_text: str
    # action: str  # "expand", "summarize", "improve"

@app.get("/")
async def root():
  return {"message": "Hello from Mindtaker!"}

@app.post("/expand-idea/")
async def expand_idea(request: IdeaRequest):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[ 
            {"role": "developer", "content": "You are a helpful assistant in expanding my ideas in positive ways."},
            {"role": "user", "content": f"My idea is as follows: {request.idea_text}"}
          ]
    )
    if response.choices and len(response.choices) > 0:
        return {"result": response.choices[0].message.content}
    return {"error": "No response from the model"}