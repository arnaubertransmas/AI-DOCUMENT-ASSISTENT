import faiss
import numpy as np

class VectorStore:
    def __init__(self, dim: int):
        self.dim = dim
        self.index = faiss.IndexFlatL2(dim)  # cerca per distància L2
        self.text_chunks = []  # aquí guardem els textos reals

    def add_vector(self, embedding: list, text: str):
        vector = np.array([embedding]).astype("float32")
        self.index.add(vector)
        self.text_chunks.append(text)

    def search(self, query_embedding: list, k: int = 3):
        vector = np.array([query_embedding]).astype("float32")
        distances, indices = self.index.search(vector, k)

        results = []
        for idx in indices[0]:
            if idx < len(self.text_chunks):
                results.append(self.text_chunks[idx])

        return results
