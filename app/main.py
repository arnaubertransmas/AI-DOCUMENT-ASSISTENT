from fastapi import FastAPI
from app.routes import upload

app = FastAPI(title="AI Document Assistant API")

app.include_router(upload.router)

@app.get("/")
def root():
    return {"message": "API is running"}
