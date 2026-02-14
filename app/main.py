from  fastapi import FastAPI

app = FastAPI(
    title="Library API",
    description="API REST pour gérer une bibliothèque de livres",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "Bienvenue dans la bibliothèque API!"}