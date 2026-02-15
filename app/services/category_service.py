from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.model.category import Category
from app.repo import category_repo


def create_category(db: Session, data):
    category = Category(**data.dict())
    return category_repo.create(db, category)


def get_category(db: Session, category_id: int):
    category = category_repo.get_by_id(db, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


def list_categories(db: Session, limit: int | None = None):
    return category_repo.get_all(db, limit)


def update_category(db: Session, category_id: int, data):
    category = get_category(db, category_id)
    update_data = data.dict(exclude_unset=True)
    return category_repo.update(db, category, update_data)


def delete_category(db: Session, category_id: int):
    category = get_category(db, category_id)
    category_repo.delete(db, category)
