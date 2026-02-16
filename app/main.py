from fastapi import FastAPI
from app.core.database import engine, Base
from app.middleware.auth_middleware import auth_middleware
from app.model import author  
from app.model import book    
from app.model import category  
from app.api import authors
from app.api import books
from app.api import categories

app = FastAPI(
    title="Library Management System",
    description="FastAPI + SQLAlchemy layered architecture example",
    version="1.0.0",
)


app.middleware("http")(auth_middleware)

Base.metadata.create_all(bind=engine)


app.include_router(authors.router)
app.include_router(categories.router)
app.include_router(books.router)

