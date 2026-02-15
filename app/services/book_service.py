from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.model.book import Book
from app.repo import book_repo


def create_book(db: Session, data):
    book = Book(**data.dict())
    return book_repo.create(db, book)


def get_book(db: Session, book_id: int):
    book = book_repo.get_by_id(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


def list_books(db: Session,author_id=None,category_id=None,year=None,limit=None):
    return book_repo.get_all(db, author_id, category_id, year, limit)


def update_book(db: Session, book_id: int, data):
    book = get_book(db, book_id)
    update_data = data.dict(exclude_unset=True)
    return book_repo.update(db, book, update_data)


def delete_book(db: Session, book_id: int):
    book = get_book(db, book_id)
    book_repo.delete(db, book)
