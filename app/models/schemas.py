from pydantic import BaseModel
from typing import List

class GroupedResult(BaseModel):
    group: int
    items: List[str]

class SearchResult(BaseModel):
    chunk: str
    score: float

