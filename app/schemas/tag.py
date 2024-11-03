from typing import Optional

from pydantic import BaseModel


class TagSchema(BaseModel):

    title: str
    description: Optional[str] = None


class TagUpdateSchema(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
