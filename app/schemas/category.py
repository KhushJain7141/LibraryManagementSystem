from pydantic import BaseModel
from typing import Optional,List


class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(BaseModel):
    name: Optional[str] = None


class CategoryResponse(CategoryBase):
    id: int
    books: List[CategoryBook] = []

    class Config:
        orm_mode = True
        
class CategoryBook(BaseModel):
    id: int
    title: str
    publication_year: Optional[int]

    class Config:
        orm_mode = True
        
CategoryResponse.model_rebuild()