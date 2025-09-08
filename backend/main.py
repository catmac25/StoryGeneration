# import fast api first 
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# uv init => initializes a project structure in my folfer
from core.config import settings
from routers import story
from db.database import create_tables
# interpreter path = /Users/arpitaarora/Documents/python/interactiveStory/backend/.venv/bin/activate

app = FastAPI(
    title="Create your own adventure story API",
    description= "An API to create and manage interactive adventure stories",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.add_middleware(
    # we allow everything
    CORSMiddleware,
    allow_origins= settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(story.router, prefix = settings.API_PREFIX)
@app.on_event("startup")
def on_startup():
    create_tables()
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app= "main:app", host = "0.0.0.0", port = 8000, reload=True)
