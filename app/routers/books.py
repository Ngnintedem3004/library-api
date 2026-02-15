from typing import List 
from fastapi import APIRouter, Depends, HTTPException
from app.models import Book
from app.schemas import *
from database import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/books", tags=["books"])

@router.post("", response_model=BookCreate, status_code=201,
             summary="Créer un nouveau livre", description="""
    Crée un nouveau livre dans la bibliothèque.
    
    ## Validations
    - **title** : 3-200 caractères
    - **author** : 2-100 caractères
    - **year** : 1000-2100 (optionnel)
    - **isbn** : Format ISBN-13 (optionnel)
    
    ## Headers de réponse
    - **Location** : URL de la ressource créée (/books/{id})
    """,
             response_description="Le livre créé avec succès",
                responses={
                    201: {"description": "Livre créé avec succès"},
                    400: {"description": "Requête invalide"},
                    500: {"description": "Erreur serveur"}
                }
             )
def create_book( payload: BookCreate, db: Session = Depends(get_db)):
    book = Book(
        title=payload.title,
        author=payload.author,
        published_year=payload.year,
        genre=payload.genre,
        isbn=payload.isbn,
    )
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

@router.get("/{book_id}", response_model=BookRead, status_code=200)
def read_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Livre non trouvé")
    return book
@router.get("", response_model=List[BookRead], status_code=200)
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    books = db.query(Book).offset(skip).limit(limit).all()
    if not books:
        raise HTTPException(status_code=404, detail="Aucun livre trouvé")
    return books
@router.put("/{book_id}", response_model=BookRead, status_code=200)
def update_book(book_id: int, payload: BookUpdate, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Livre non trouvé")
    book.title = payload.title
    book.author = payload.author
    book.published_year = payload.year
    book.genre = payload.genre
    book.isbn = payload.isbn
    db.commit()
    db.refresh(book)
    return book
@router.patch("/{book_id}", response_model=BookRead, status_code=200)
def patch_book(book_id: int, payload: BookPatch, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Livre non trouvé")
    if payload.title is not None:
        book.title = payload.title
    if payload.author is not None:
        book.author = payload.author
    if payload.year is not None:
        book.published_year = payload.year
    if payload.genre is not None:
        book.genre = payload.genre
    if payload.isbn is not None:
        book.isbn = payload.isbn
    db.commit()
    db.refresh(book)
    return book
