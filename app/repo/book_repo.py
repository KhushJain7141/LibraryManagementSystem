from sqlalchemy.orm import Session
from app.model.book import Book


def create(db: Session, book: Book) -> Book:
    db.add(book)
    db.commit()
    db.refresh(book)
    return book


def get_by_id(db: Session, book_id: int) -> Book | None:
    return db.query(Book).filter(Book.id == book_id).first()


def get_all(
    db: Session,
    author_id: int | None = None,
    category_id: int | None = None,
    year: int | None = None,
    limit: int | None = None,
):
    query = db.query(Book)

    if author_id:
        query = query.filter(Book.author_id == author_id)

    if category_id:
        query = query.filter(Book.category_id == category_id)

    if year:
        query = query.filter(Book.publication_year == year)

    query = query.order_by(Book.title.asc())

    if limit:
        query = query.limit(limit)

    return query.all()


def update(db: Session, book: Book, update_data: dict) -> Book:
    for key, value in update_data.items():
        setattr(book, key, value)

    db.commit()
    db.refresh(book)
    return book


def delete(db: Session, book: Book):
    db.delete(book)
    db.commit()
