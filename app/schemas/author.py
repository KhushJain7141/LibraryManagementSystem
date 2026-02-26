from pydantic import BaseModel
from typing import List, Optional


# Base schema (shared fields)
class AuthorBase(BaseModel):
    name: str
    bio: str


# Used when creating
class AuthorCreate(AuthorBase):
    name: str
    bio: Optional[str] = None


# Used when updating
class AuthorUpdate(BaseModel):
    name: Optional[str] = None
    bio: Optional[str] = None


# Used in responses
class AuthorResponse(AuthorBase):
    id: int

    class Config:
        orm_mode = True
