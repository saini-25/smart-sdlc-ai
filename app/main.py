from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import ai_routes, chat_routes

app = FastAPI(
    title="SmartSDLC API",
    version="1.0",
    description="AI-powered SDLC automation backend"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(ai_routes.router)
app.include_router(chat_routes.router)

@app.get("/")
def root():
    return {"message": "SmartSDLC Backend is running!"}
