# import uuid
from typing import Optional
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, Cookie, Response
from sqlalchemy.orm import Session
import json
from db.database import get_db, SessionLocal
from models.story import Story
from schemas.story import StoryRequest, StoryResponse

from core.story_generator import generate_story
router = APIRouter(
    # backend_url/api/stories
    prefix="/stories",
    tags=["stories"],
)

@router.post("/create", response_model=StoryResponse)
def create_story(
    request: StoryRequest,
    response: Response,
    db: Session= Depends(get_db)):
    prompt = request.prompt
    story_text = generate_story(prompt)
    
    new_story = Story(
        prompt=prompt,
        generated_story=story_text,
        created_at=datetime.now()
    )
    db.add(new_story)
    db.commit()
    db.refresh(new_story)

    return new_story

@router.get("/{story_id}/complete", response_model = StoryResponse)
def get_complete_story(story_id: int, db: Session = Depends(get_db)):
    story = db.query(Story).filter(Story.id == story_id).first()
    if not story:
        raise HTTPException(status_code=404, detail="Story not found")
    return story
