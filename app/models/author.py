from sqlalchemy import DateTime, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.settings.db import Base


class Author(Base):
    __tablename__ = "author"

    full_name: Mapped[str] = mapped_column(String(255))
    birth_date: Mapped[DateTime] = mapped_column(DateTime(timezone=True))
    death_date: Mapped[DateTime] = mapped_column(DateTime(timezone=True), nullable=True)
    biography: Mapped[str] = mapped_column(Text, nullable=True)

    books = relationship("Book", backref="author_books")
    tags = relationship("Tag", secondary="author_tags", backref="authors")
