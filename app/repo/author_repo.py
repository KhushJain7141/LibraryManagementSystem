from sqlalchemy.orm import Session,joinedload
from app.model.author import Author


def create(db: Session, author: Author) -> Author:
    db.add(author)
    db.commit()
    db.refresh(author)
    return author


def get_by_id(db: Session, author_id: int) -> Author | None:
    return (
        db.query(Author)
        .options(joinedload(Author.books))
        .filter(Author.id == author_id)
        .first()
    )


def get_all(db: Session, limit: int | None = None):
    query = db.query(Author)

    if limit:
        query = query.limit(limit)

    return query.all()


def update(db: Session, author: Author, update_data: dict) -> Author:
    for key, value in update_data.items():
        setattr(author, key, value)

    db.commit()
    db.refresh(author)
    return author


def delete(db: Session, author: Author):
    db.delete(author)
    db.commit()
