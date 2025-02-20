from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.models.settings.db_conn_handler import postgres_connection_handler

from src.main.routes.lembretes_routes import router as lembretes_router

postgres_connection_handler.connect_to_db()

app = FastAPI(
    title="Dose Certa API",
    description="API para gerenciamento de lembretes de medicamentos.",
    version="1.0.0"
)

@app.get("/")
def health_check():
    return {"message": "API is running!"}


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(lembretes_router)
