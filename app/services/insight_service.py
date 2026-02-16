from sqlalchemy.orm import Session
from sqlalchemy import func
from app.model.book import Book
from app.model.author import Author


def generate_insights(db: Session):

    total_books = db.query(func.count(Book.id)).scalar()

    if total_books == 0:
        return {
            "top_authors": [],
            "busy_years": []
        }


    valid_books_query = db.query(Book).filter(
        Book.publication_year.between(1900, 2100)
    )


    top_authors_result = (
        db.query(
            Author.name.label("author"),
            func.count(Book.id).label("book_count")
        )
        .join(Book, Book.author_id == Author.id)
        .filter(Book.publication_year.between(1900, 2100))
        .group_by(Author.id)
        .order_by(func.count(Book.id).desc())
        .limit(5)
        .all()
    )

    top_authors = [
        {
            "author": row.author,
            "book_count": row.book_count
        }
        for row in top_authors_result
    ]


    busy_years_raw = (
        db.query(
            Book.publication_year.label("year"),
            func.count(Book.id).label("book_count")
        )
        .filter(Book.publication_year.between(1900, 2100))
        .group_by(Book.publication_year)
        .having(func.count(Book.id) >= 2)
        .order_by(Book.publication_year.asc())
        .all()
    )

    busy_years = []

    for row in busy_years_raw:
        books_in_year = (
            db.query(Book.title)
            .filter(
                Book.publication_year == row.year,
                Book.publication_year.between(1900, 2100)
            )
            .all()
        )

        busy_years.append({
            "year": row.year,
            "books": [book.title for book in books_in_year]
        })



    return {
        "top_authors": top_authors,
        "busy_years": busy_years
    }
