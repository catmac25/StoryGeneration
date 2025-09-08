from sqlalchemy import Column, Integer, String, Text, ForeignKey, Boolean, DateTime, JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from db.database import Base

class Story(Base):
    __tablename__ = "stories"
    # id = Column(Integer, primary_key = True, index = True) #we need primary key and id as integer 
    # title = Column (String, index=True)
    # # session_id = Column(String, index=True)
    # created_at = Column(DateTime(timezone=True), server_default = func.now())
    
    id = Column(Integer, primary_key=True, index=True)   # unique story ID
    prompt = Column(Text, nullable=False)                # user’s input prompt
    generated_story = Column(Text, nullable=False)       # AI generated story
    created_at = Column(DateTime(timezone=True), server_default=func.now())  # timestamp
    

