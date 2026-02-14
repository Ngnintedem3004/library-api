from  fastapi import FastAPI

from app.routers import books

app = FastAPI(
    title="Library API",
    description="API REST pour gérer une bibliothèque de livres",
    version="1.0.0"
)
app.include_router(books.router)
@app.get("/")
def read_root():
    return {"message": "Bienvenue dans la bibliothèque API!"}