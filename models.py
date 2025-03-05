"""
Data models used in the API.
"""
from pydantic import BaseModel
from enum import Enum

class IdeaAction(str, Enum):
    expand = "expand"
    summarize = "summarize"

class IdeaRequest(BaseModel):
    idea_text: str
    action: IdeaAction
