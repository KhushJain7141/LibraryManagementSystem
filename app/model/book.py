from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Book(Base):
    __tablename__ = "books"  # Naming the table 

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    isbn = Column(String)
    publication_year = Column(Integer)

    author_id = Column(Integer, ForeignKey("authors.id"))  # Creates a fk tablename.attributename
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    
    author = relationship("Author", back_populates="books")
    category = relationship("Category", back_populates="books")