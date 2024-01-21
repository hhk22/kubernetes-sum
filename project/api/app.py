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
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
    with open(path, "w", encoding="utf-8") as f:
        html = requests.get(url, headers=headers).text
        f.write(html)
        return path
