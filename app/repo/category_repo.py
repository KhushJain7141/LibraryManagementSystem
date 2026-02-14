from sqlalchemy.orm import Session
from app.model.category import Category


def create(db: Session, category: Category) -> Category:
    db.add(category)
    db.commit()
    db.refresh(category)
    return category


def get_by_id(db: Session, category_id: int) -> Category | None:
    return db.query(Category).filter(Category.id == category_id).first()


def get_by_name(db: Session, name: str) -> Category | None:
    return db.query(Category).filter(Category.name == name).first()


def get_all(db: Session, limit: int | None = None):
    query = db.query(Category)

    if limit:
        query = query.limit(limit)

    return query.all()


def update(db: Session, category: Category, update_data: dict) -> Category:
    for key, value in update_data.items():
        setattr(category, key, value)

    db.commit()
    db.refresh(category)
    return category


def delete(db: Session, category: Category):
    db.delete(category)
    db.commit()
