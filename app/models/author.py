from sqlalchemy import DateTime, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.settings.db import Base


class Author(Base):

    full_name: Mapped[str] = mapped_column(String(255))
    birth_date = mapped_column(DateTime)
    death_date = mapped_column(DateTime, nullable=True)
    biography = mapped_column(Text, nullable=True)

    books = relationship("Book", backref="author_books")
    tags = relationship("Tag", secondary="author_tags", backref="authors")
