from fastapi import APIRouter, Request
from pydantic import BaseModel
from app.services.embedding_service import text_to_vector

router = APIRouter()

class Question(BaseModel):
    question: str

@router.post("/search")
async def search_docs(request: Request, q: Question):
    vector_store = request.app.state.vector_store

    query_embedding = text_to_vector(q.question)
    results = vector_store.search(query_embedding, k=3)

    return {
        "question": q.question,
        "relevant_chunks": results
    }
