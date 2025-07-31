import requests
import os

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

def fetch_headlines(query="world", language="en", limit=100):
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": query,
        "language": language,
        "pageSize": limit,
        "sortBy": "publishedAt",
        "apiKey": NEWS_API_KEY
    }
    response = requests.get(url, params=params)
    return response.json().get("articles", [])