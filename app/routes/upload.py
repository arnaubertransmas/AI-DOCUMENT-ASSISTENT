from fastapi import APIRouter, UploadFile, File
import os
from uuid import uuid4
from app.services.pdf_service import extract_text_from_pdf

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        return {"error": "Only PDFs allowed"}

    file_id = f"{uuid4()}.pdf"
    file_path = os.path.join(UPLOAD_DIR, file_id)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    extracted_text = extract_text_from_pdf(file_path)

    return {
        "filename": file.filename,
        "stored_as": file_id,
        "text_preview": extracted_text[:500]  # només els primers caràcters
    }
