from typing import Optional

from pydantic import BaseModel


class Tag(BaseModel):

    title: str
    description: Optional[str] = None
