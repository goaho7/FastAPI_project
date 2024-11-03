from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class AuthorSchema(BaseModel):

    full_name: str
    birth_date: datetime
    death_date: Optional[datetime] = None
    biography: Optional[str] = None
    tags: Optional[list[int]] = None

    class Config:
        orm_mode = True


class AuthorUpdateSchema(BaseModel):

    full_name: Optional[str] = None
    birth_date: Optional[datetime] = None
    death_date: Optional[datetime] = None
    biography: Optional[str] = None

    class Config:
        orm_mode = True
