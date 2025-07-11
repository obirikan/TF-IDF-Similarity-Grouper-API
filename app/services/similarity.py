from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from typing import List

def init_vectorizer(chunks: List[str]) -> TfidfVectorizer:
    vectorizer = TfidfVectorizer()
    vectorizer.fit(chunks)
    return vectorizer

def group_similar_chunks(chunks: List[str], threshold: float = 0.75) -> List[dict]:
    vectorizer = TfidfVectorizer().fit_transform(chunks)
    sim_matrix = cosine_similarity(vectorizer)

    visited = set()
    groups = []

    for i in range(len(sim_matrix)):
        if i in visited:
            continue
        group = [i]
        visited.add(i)
        for j in range(i + 1, len(sim_matrix)):
            if sim_matrix[i][j] >= threshold:
                group.append(j)
                visited.add(j)
        if len(group) > 1:
            groups.append({
                "group": len(groups) + 1,
                "items": [chunks[k] for k in group]
            })

    return groups

def search_chunks(query: str, chunks: List[str], vectorizer: TfidfVectorizer, top_k: int = 5) -> List[dict]:
    vectors = vectorizer.transform(chunks + [query])

    query_vector = vectors[-1]
    doc_vectors = vectors[:-1]

    sims = cosine_similarity(query_vector, doc_vectors).flatten()
    top_indices = sims.argsort()[::-1][:top_k]

    return [
        {"chunk": chunks[i], "score": float(sims[i])}
        for i in top_indices if sims[i] > 0
    ]
