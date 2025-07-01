from fastapi import APIRouter, Body
from app.services.ai_story_generator import analyze_requirements
from app.services.code_generator import generate_code
from app.services.bug_resolver import fix_bugs

router = APIRouter(prefix="/ai")

@router.post("/upload-pdf")
def upload_pdf(text: str = Body(...)):
    return analyze_requirements(text)

@router.post("/generate-code")
def generate_code_route(prompt: str = Body(...)):
    return {"code": generate_code(prompt)}

@router.post("/fix-bugs")
def fix_bugs_route(code: str = Body(...)):
    return {"fixed_code": fix_bugs(code)}
