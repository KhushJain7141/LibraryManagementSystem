from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base

class Author(Base):  # Inherits from Base (in python extends keyword not used)
    __tablename__ = "authors"  # Naming the table 

    id = Column(Integer, primary_key=True, index=True)  # Creates a id of type int and with pk and indexing on 
    name = Column(String, index=True)
    bio = Column(String)

    books = relationship("Book", back_populates="author",cascade="all, delete")
