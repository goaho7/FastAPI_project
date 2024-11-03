from app.repositories.author import AuthorRepository
from app.repositories.book import BookRepository
from app.repositories.tag import TagRepository
from app.services.author import AuthorService
from app.services.book import BookService
from app.services.tag import TagService


def author_service():
    return AuthorService(AuthorRepository, TagRepository)


def book_service():
    return BookService(BookRepository, AuthorRepository)


def tag_service():
    return TagService(TagRepository)
