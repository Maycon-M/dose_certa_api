from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.models.settings.db_conn_handler import postgres_connection_handler

from src.main.routes.lembretes_routes import router as lembretes_router

postgres_connection_handler.connect_to_db()

app = FastAPI()

@app.get("/")
def health_check():
    return {"message": "API is running!"}


origins = [
    "http://localhost",
    "http://127.0.0.1"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(lembretes_router)
