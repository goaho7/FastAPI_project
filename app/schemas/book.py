from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Book(BaseModel):

    title: str
    publication_date: datetime
    genre: str
    notes: Optional[str] = None
