from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def text_to_vector(text: str) -> list:
    """
    Convert text to vector embedding using OpenAI's embedding model.
    """
    try:
        response = client.embeddings.create(
            input=text,
            model="text-embedding-3-small"
        )
        return response.data[0].embedding
    except Exception as e:
        raise Exception(f"Error creating embedding: {str(e)}")