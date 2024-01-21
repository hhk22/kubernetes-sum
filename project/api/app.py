from fastapi import FastAPI
from utils import encode_url
import requests

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/scrape")
async def scape(url: str):
    encoded_url = encode_url(url)
    path = f"./html/{encoded_url}.txt"
    with open(path, "w", encoding="utf-8") as f:
        html = requests.get(url).text
        f.write(html)
        return path
