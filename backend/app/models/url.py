from typing import Optional, List, Dict, Any
from datetime import datetime
from pydantic import BaseModel, Field
from bson import ObjectId


class URLModel(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    url: str
    title: Optional[str] = None
    meta_description: Optional[str] = None
    meta_keywords: Optional[str] = None
    visible_text: Optional[str] = None
    meta_score: float = 0.0
    tfidf_vector: Optional[List[float]] = None
    click_count: int = 0
    last_updated: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        populate_by_name = True


class ClickLogModel(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    url_id: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        populate_by_name = True


class SearchHistoryModel(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    query: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    result_count: int = 0

    class Config:
        populate_by_name = True


class SearchResultModel(BaseModel):
    url_id: str
    url: str
    title: str
    meta_description: str
    meta_score: float
    relevance_score: float
    popularity_score: float
    final_score: float
