from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.settings.db import Base


class Tag(Base):

    title: Mapped[str] = mapped_column(String(55), unique=True)
    description = mapped_column(Text, nullable=True)


class AuthorTags(Base):
    __tablename__ = "author_tags"
    author_id: Mapped[int] = mapped_column(ForeignKey("author.id"), primary_key=True)
    tag_id: Mapped[int] = mapped_column(ForeignKey("tag.id"), primary_key=True)


class BookTags(Base):
    __tablename__ = "book_tags"
    book_id: Mapped[int] = mapped_column(ForeignKey("book.id"), primary_key=True)
    tag_id: Mapped[int] = mapped_column(ForeignKey("tag.id"), primary_key=True)
