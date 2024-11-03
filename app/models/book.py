from sqlalchemy import DateTime, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.settings.db import Base


class Book(Base):
    __tablename__ = "book"

    title: Mapped[str] = mapped_column(String(255))
    publication_date: Mapped[DateTime] = mapped_column(DateTime(timezone=True), nullable=True)
    genre: Mapped[str] = mapped_column(String(150), nullable=True)
    notes: Mapped[str] = mapped_column(Text, nullable=True)
    author_id: Mapped[int] = mapped_column(ForeignKey("author.id"))

    author = relationship("Author", backref="book_list")

    tags = relationship("Tag", secondary="book_tags", backref="books")
