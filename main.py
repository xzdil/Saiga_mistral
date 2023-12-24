from fastapi import FastAPI
from model import generate
app = FastAPI()


@app.get("/")
def read_root(text: str):
    return generate(text)

