from fastapi import FastAPI
from fastapi.responses import FileResponse
from model import generate
app = FastAPI()


@app.get("/")
def load():
    return FileResponse("index.html")

@app.post("/")
def read_root(text: str):
    return generate(text)

