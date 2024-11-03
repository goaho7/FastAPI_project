from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class BookSchema(BaseModel):
    title: str
    publication_date: datetime
    genre: str
    notes: Optional[str] = None
    author_id: int


class BookUpdateSchema(BaseModel):
    title: Optional[str] = None
    publication_date: Optional[datetime] = None
    genre: Optional[str] = None
    notes: Optional[str] = None
    author_id: Optional[int] = None
