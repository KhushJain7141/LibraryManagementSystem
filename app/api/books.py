from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.schemas.book import BookCreate, BookUpdate, BookResponse
from app.services import book_service

router = APIRouter(prefix="/books", tags=["Books"])


@router.post("/", response_model=BookResponse)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    return book_service.create_book(db, book)


@router.get("/{book_id}", response_model=BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    return book_service.get_book(db, book_id)


@router.get("/", response_model=list[BookResponse])
def list_books(
    author_id: int | None = None,
    category_id: int | None = None,
    year: int | None = None,
    limit: int | None = None,
    db: Session = Depends(get_db),
):
    return book_service.list_books(
        db,
        author_id=author_id,
        category_id=category_id,
        year=year,
        limit=limit,
    )


@router.put("/{book_id}", response_model=BookResponse)
def update_book(
    book_id: int,
    data: BookUpdate,
    db: Session = Depends(get_db),
):
    return book_service.update_book(db, book_id, data)


@router.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book_service.delete_book(db, book_id)
    return {"message": "Book deleted successfully"}
