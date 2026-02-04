def dividir_text(text: str, chunk_size: int = 500, overlap: int = 100):
    ''' dividim el text en trossos de 500 caracters '''
    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap

    return chunks
