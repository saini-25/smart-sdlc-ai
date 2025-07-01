from fastapi import APIRouter, Body
router = APIRouter(prefix="/chat")

@router.post("/chat")
def chat_route(message: str = Body(...)):
    return {"reply": f"You asked: {message}. Here's a helpful tip: Write unit tests!"}
