from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.model.author import Author
from app.repo import author_repo



def create_author(db:Session,data):
    author = Author(**data.dict())
    return author_repo.create(db,author)

def get_author(db:Session,author_id:int):
    author = author_repo.get_by_id(db,author_id)
    if not author:
        raise HTTPException(status_code=404,detail="Author not found")
    return author

def list_authors(db:Session,limit:int | None = None):
    return author_repo.get_all(db,limit)

def update_author(db:Session,author_id:int,data):
    author = get_author(db,author_id)
    update_data = data.dict(exclude_unset=True)
    return author_repo.update(db,author,update_data)

def delete_author(db:Session,author_id:int):
    author = get_author(db,author_id)
    author_repo.delete(db,author)