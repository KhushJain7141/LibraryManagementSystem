from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.schemas.author import AuthorCreate, AuthorUpdate, AuthorResponse
from app.services import author_service

router = APIRouter(prefix="/authors", tags=["Authors"])


@router.post("/", response_model=AuthorResponse)
def create_author(author: AuthorCreate, db: Session = Depends(get_db)):
    return author_service.create_author(db, author)


@router.get("/{author_id}", response_model=AuthorResponse)
def get_author(author_id: int, db: Session = Depends(get_db)):
    return author_service.get_author(db, author_id)


@router.get("/", response_model=list[AuthorResponse])
def list_authors(limit: int | None = None, db: Session = Depends(get_db)):
    return author_service.list_authors(db, limit)


@router.put("/{author_id}", response_model=AuthorResponse)
def update_author(
    author_id: int,
    data: AuthorUpdate,
    db: Session = Depends(get_db),
):
    return author_service.update_author(db, author_id, data)


@router.delete("/{author_id}")
def delete_author(author_id: int, db: Session = Depends(get_db)):
    author_service.delete_author(db, author_id)
    return {"message": "Author deleted successfully"}
