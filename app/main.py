from  fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from app.routers import books

app = FastAPI(
    doc_urls="none",
    redoc_url="/none",
)
app.include_router(books.router)
@app.get("/")
def read_root():
    return {"message": "Bienvenue dans la bibliothèque API!"}
@app.get("/docs",include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="Librairy API Documentation",
        swagger_favicon_url="https://fastapi.tiangolo.com/img/favicon.png",
        swagger_ui_parameters={
            "defaultModelsExpandDepth": -1 ,
             "syntaxHighlight.theme":"monokai",
             "tryItOutEnabled": True,
            },
    )
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = app.openapi(
        title="Librairy API",
        version="1.0.0",
        description="API REST pour gérer une bibliothèque de livres.",
        routes=app.routes,
    )
    openapi_schema["info"]["title"] = "Librairy API"
    openapi_schema["info"]["version"] = "1.0.0"
    openapi_schema["info"]["description"] = "API pour gérer une bibliothèque de livres."
    app.openapi_schema = openapi_schema
    return app.openapi_schema