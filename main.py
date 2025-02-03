from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class News(BaseModel):
    title: str
    content: str | None = None
    views: int = 0

@app.post("/news/")
async def create_news(news: News) -> News:
    "endpoint to create news"
    return news