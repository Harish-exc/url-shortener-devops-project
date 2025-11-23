from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/shorten")
def shorten_url():
    return {"short_url": "http://short.ly/abc123"}
