from sqlalchemy.orm import Session
from app.model.book import Book


def create(db: Session, book: Book) -> Book:
    db.add(book)
    db.commit()
    db.refresh(book)
    return book


def get_by_id(db: Session, book_id: int) -> Book | None:
    return db.query(Book).filter(Book.id == book_id).first()


from sqlalchemy.orm import joinedload

def get_all(db: Session, author_id=None, category_id=None, year=None, limit=None):

    query = db.query(Book).options(
        joinedload(Book.author),
        joinedload(Book.category)
    )

    if author_id:
        query = query.filter(Book.author_id == author_id)

    if category_id:
        query = query.filter(Book.category_id == category_id)

    if year:
        query = query.filter(Book.publication_year == year)

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
