from  fastapi import FastAPI

from app.routers.books import router as router_books
from app.routers.authentication import router as router_authentication

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

    openapi_tags=[  
         {
            "name": "auth",
            "description": "Gestion des utilisateurs"
        },                        # Tags pour organiser les routes
        {
            "name": "books",
            "description": "Opérations sur les livres"
        },
       
    ]
)
app.include_router(router_authentication)
app.include_router(router_books)
app.get("/")
def read_root():
    return {"message": "Bienvenue dans la bibliothèque API!"}