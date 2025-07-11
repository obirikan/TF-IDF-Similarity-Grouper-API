import pandas as pd
import fitz  # PyMuPDF
from typing import List
from fastapi import UploadFile
from app.utils.file_helpers import get_extension
from io import StringIO

async def extract_text_chunks(file: UploadFile) -> List[str]:
    ext = get_extension(file.filename)
    content = await file.read()
    text_chunks = []

    if ext == ".pdf":
        doc = fitz.open(stream=content, filetype="pdf")
        for page in doc:
            text_chunks += page.get_text().split("\n\n")
    elif ext == ".csv":
        df = pd.read_csv(StringIO(content.decode()))
        text_chunks = df.astype(str).agg(" ".join, axis=1).tolist()
    elif ext == ".txt":
        text_chunks = content.decode().split("\n\n")
    else:
        raise ValueError("Unsupported file type")

    return [chunk.strip() for chunk in text_chunks if chunk.strip()]
