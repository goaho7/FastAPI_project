from sqlalchemy import DateTime, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.settings.db import Base


class Book(Base):
    title: Mapped[str] = mapped_column(String(255))
    publication_date = mapped_column(DateTime, nullable=True)
    genre: Mapped[str] = mapped_column(String(150), nullable=True)
    notes = mapped_column(Text, nullable=True)

    author_id: Mapped[int] = mapped_column(ForeignKey("author.id"))
    author = relationship("Author", backref="book_list")

    tags = relationship("Tag", secondary="book_tags", backref="books")
