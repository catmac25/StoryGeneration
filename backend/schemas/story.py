from typing import List, Optional, Dict
from datetime import datetime
from pydantic import BaseModel


# Request schema: what the user sends
class StoryRequest(BaseModel):
    prompt: str

# Response schema: what your API returns
class StoryResponse(BaseModel):
    id: int                # unique story ID from DB
    prompt: str            # user’s input
    generated_story: str   # AI’s output
    created_at: datetime   # timestamp when story was saved

    class Config:
        from_attributes = True   # lets Pydantic read directly from SQLAlchemy model

