import logging
import time
import asyncio
import logging.config

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from datetime import datetime
from news_fetcher import fetch_headlines
from location_parser import extract_locations
from geocoder import get_coordinates
from logging_config import LOGGING_CONFIG
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    task = asyncio.create_task(fetch_news_periodically())
    yield
    task.cancel()


async def fetch_news_periodically():
    while True:
        try:
            fetch_news_and_cache("world")
        except Exception as e:
            print("Failed to fetch news:", e)
        await asyncio.sleep(600)

def fetch_news_and_cache(query):
    print("Fetching fresh news...")
    articles = fetch_headlines(query)
    results = []

    for article in articles:
        locations = extract_locations(article.get("title", ""))
        coords = []
        for loc in locations:
            c = get_coordinates(loc)
            if c:
                coords.append({**c, "name": loc})
        if coords:
            results.append({
                "title": article["title"],
                "url": article["url"],
                "locations": coords
            })

    news_cache[query] = {
        "articles": articles,
        "locations": results,
        "last_updated": datetime.utcnow()
    }

    print(f"Fetched and processed {len(results)} articles for '{query}'")

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], #TODO: change this to web address
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

news_cache = {
    "world": {
        "articles": [],         # raw articles if needed
        "locations": [],        # final locations
        "last_updated": None
    }
}

# Serve index.html manually at root
@app.get("/")
def root():
    return FileResponse("static/index.html")

@app.get("/news")
def news_with_locations(q: str = "world"):
    start_time = time.time()
    logging.debug(f"Fetching news for query: '{q}'")
    if q not in news_cache:
        fetch_news_and_cache(q)

    results = news_cache[q]["locations"]
    logging.debug(f"Returning {len(results)} processed articles")

    duration = time.time() - start_time
    logging.debug(f"Finished processing in {duration:.2f} seconds")
    return results