from pydantic import BaseModel
from typing import Optional



class AuthorSimple(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class CategorySimple(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True



class BookBase(BaseModel):
    title: str
    isbn: str
    publication_year: int
    author_id: int
    category_id: int




class BookCreate(BookBase):
    pass


class BookUpdate(BaseModel):
    title: Optional[str] = None
    isbn: Optional[str] = None
    publication_year: Optional[int] = None
    author_id: Optional[int] = None
    category_id: Optional[int] = None


class BookResponse(BaseModel):
    id: int
    title: str
    isbn: str
    publication_year: int

    author: AuthorSimple
    category: CategorySimple

    class Config:
        orm_mode = True