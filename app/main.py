from  fastapi import FastAPI

from app.routers import books

app = FastAPI(
    title="Library API",
    description="API REST pour gérer une bibliothèque de livres",
    version="1.0.0",
    contact={
        "name": "Support Technique",
        "url": "https://support.example.com",
        "email": "api-support@example.com"
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT"
    },
    openapi_tags=[                          # Tags pour organiser les routes
        {
            "name": "books",
            "description": "Opérations sur les livres"
        },
        {
            "name": "users",
            "description": "Gestion des utilisateurs"
        }
    ]
)
app.include_router(books.router)
@app.get("/")
def read_root():
    return {"message": "Bienvenue dans la bibliothèque API!"}