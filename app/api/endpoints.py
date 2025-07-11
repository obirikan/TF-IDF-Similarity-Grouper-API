from fastapi import APIRouter, UploadFile, File, HTTPException, Query
from app.services.extractor import extract_text_chunks
from app.services.similarity import group_similar_chunks, search_chunks, init_vectorizer
from app.models.schemas import GroupedResult, SearchResult
from app.core.state import DOCUMENT_CHUNKS, TFIDF_VECTORIZER

router = APIRouter()

@router.post("/upload", response_model=list[GroupedResult])
async def upload_file(file: UploadFile = File(...)):
    try:
        chunks = await extract_text_chunks(file)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    if not chunks:
        raise HTTPException(status_code=400, detail="No valid content extracted.")

    DOCUMENT_CHUNKS.clear()
    DOCUMENT_CHUNKS.extend(chunks)
    TFIDF_VECTORIZER.clear()
    TFIDF_VECTORIZER.append(init_vectorizer(chunks))

    groups = group_similar_chunks(chunks)
    return groups


@router.get("/search", response_model=list[SearchResult])
def search_content(q: str = Query(..., min_length=2)):
    if not DOCUMENT_CHUNKS or not TFIDF_VECTORIZER:
        raise HTTPException(status_code=400, detail="No content uploaded yet.")

    return search_chunks(query=q, chunks=DOCUMENT_CHUNKS, vectorizer=TFIDF_VECTORIZER[0])
