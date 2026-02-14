
from pydantic import BaseModel, Field
from typing import Optional

class BookCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=200, description="Titre du livre")
    author: str = Field(..., min_length=2, max_length=100, description="Auteur du livre")
    year: int = Field(..., ge=1000, le=2100, description="Année de publication")
    genre: str = Field(..., max_length=50, description="Genre littéraire")
    isbn: str = Field(..., max_length=17, description="Code ISBN-13")
    
    class Config:
        json_schema_extra = {
            "example": {
                "title": "1984",
                "author": "George Orwell",
                "year": 1949,
                "genre": "Science-fiction dystopique",
                "isbn": "978-0451524935"
            }
        }

class BookUpdate(BaseModel):
    title: str = Field(..., min_length=3, max_length=200, description="Titre du livre") 
    author: str = Field(..., min_length=2, max_length=100, description="Auteur du livre")
    year: Optional[int] = Field(None, ge=1000, le=2100, description="Année de publication")
    genre: Optional[str] = Field(None, max_length=50, description="Genre littéraire")
    isbn: Optional[str] = Field(None, max_length=17, description="Code ISBN-13")

    class Config:
        json_schema_extra = {
            "example": {
                "title": "1984",
                "author": "George Orwell",
                "year": 1949,
                "genre": "Science-fiction dystopique",
                "isbn": "978-0451524935"
            }
        }

class BookRead(BaseModel):
    id: int = Field(..., description="ID unique du livre")
    title: str = Field(..., description="Titre du livre")
    author: str = Field(..., description="Auteur du livre")
    year: Optional[int] = Field(None, description="Année de publication")
    genre: Optional[str] = Field(None, description="Genre littéraire")
    isbn: Optional[str] = Field(None, description="Code ISBN-13")

class BookPatch(BaseModel):
    title: Optional[str] = Field(None, min_length=3, max_length=200, description="Titre du livre")
    author: Optional[str] = Field(None, min_length=2, max_length=100, description="Auteur du livre")
    year: Optional[int] = Field(None, ge=1000, le=2100, description="Année de publication")
    genre: Optional[str] = Field(None, max_length=50, description="Genre littéraire")
    isbn: Optional[str] = Field(None, max_length=17, description="Code ISBN-13")
    class Config:
        json_schema_extra = {
            "example": {
                "title": "1984",
                "author": "George Orwell",
                "year": 1949,
                "genre": "Science-fiction dystopique",
                "isbn": "978-0451524935"
            }
        }

class BookDelete(BaseModel):
    id: int = Field(..., description="ID unique du livre à supprimer")
    author: Optional[str] = Field(None, description="Auteur du livre à supprimer")
    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "author": "George Orwell"
            }
        }