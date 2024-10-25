from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Author(BaseModel):

    full_name: str
    birth_date: datetime
    death_date: Optional[datetime] = None
    biography: Optional[str] = None
