import logging
import time

import logging.config
from fastapi import FastAPI
from app.news_fetcher import fetch_headlines
from app.location_parser import extract_locations
from app.geocoder import get_coordinates
from app.logging_config import LOGGING_CONFIG

from fastapi.middleware.cors import CORSMiddleware

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], #TODO: change this to web address
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/news")
def news_with_locations(q: str = "world"):
    start_time = time.time()
    logging.debug(f"Fetching news for query: '{q}'")
    articles = fetch_headlines(query=q)
    logging.debug(f"Fetched {len(articles)} articles")
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

    duration = time.time() - start_time
    logging.debug(f"Finished processing in {duration:.2f} seconds")
    return results
