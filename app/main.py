from fastapi import FastAPI
from app.news_fetcher import fetch_headlines
from app.location_parser import extract_locations
from app.geocoder import get_coordinates
app = FastAPI()

@app.get("/news")
def news_with_locations(q: str = "world"):
    articles = fetch_headlines(query=q)
    results = []

    for article in articles:
        locations = extract_locations(article.get("title", ""))
        coords = [get_coordinates(loc) for loc in locations if get_coordinates(loc)]
        results.append({
            "title": article["title"],
            "url": article["url"],
            "locations": coords
        })

    return results
