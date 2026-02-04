from fastapi import APIRouter, UploadFile, File, Request
import os
from app.services.pdf_service import extract_text_from_pdf
from app.services.dividir_text import dividir_text
from app.services.embedding_service import text_to_vector

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload")
async def upload_pdf(request: Request, file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        return {"error": "Only PDFs allowed"}
    
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    
    with open(file_path, "wb") as f:
        f.write(await file.read())
    
    extracted_text = extract_text_from_pdf(file_path)
    chunks = dividir_text(extracted_text)

    vector_store = request.app.state.vector_store

    for chunk in chunks:
        embedding = text_to_vector(chunk)
        vector_store.add_vector(embedding, chunk)


    return {
        "filename": file.filename,
        "text_preview": extracted_text,
        "num_chunks": len(chunks),
        "first_chunk_preview": chunks[0][:300] if chunks else ""
    }