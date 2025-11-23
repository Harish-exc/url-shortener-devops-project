from fastapi import FastAPI
from pydantic import BaseModel
from .database import init_db, save_url, get_url
from .models import URLItem

app = FastAPI()

# initialize DB
init_db()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/shorten")
def shorten_url(item: URLItem):
    short_id = save_url(item.original_url)
    return {"short_url": short_id}

@app.get("/{short_id}")
def redirect(short_id: str):
    original = get_url(short_id)
    if original:
        return {"original_url": original}
    return {"error": "Not found"}
