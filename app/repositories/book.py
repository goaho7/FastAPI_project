from app.models.book import Book
from app.repositories.base_repository import SQLAlchemyRepository


class BookRepository(SQLAlchemyRepository):
    model = Book
