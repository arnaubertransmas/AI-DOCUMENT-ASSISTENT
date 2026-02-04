from fastapi import FastAPI
from app.routes import upload
from app.services.vector_store_service import VectorStore
from app.routes import chat

VECTOR_DIMENSION = 1536  # embeddings OpenAI
vector_store = VectorStore(dim=VECTOR_DIMENSION)

app = FastAPI(title="AI Document Assistant API")

app.include_router(upload.router)
app.include_router(chat.router)
app.state.vector_store = vector_store

@app.get("/")
def root():
    return {"message": "API is running"}
