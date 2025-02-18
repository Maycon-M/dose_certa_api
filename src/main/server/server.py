from fastapi import FastAPI
from src.models.settings.db_conn_handler import postgres_connection_handler

postgres_connection_handler.connect_to_db()

app = FastAPI()

@app.get("/")
def health_check():
    return {"message": "API is running!"}
