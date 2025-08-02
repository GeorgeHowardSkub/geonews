# 🗺️ GeoNews — News on the Map

**GeoNews** is an open-source Python application that fetches live news headlines and displays them on an interactive map by extracting and geocoding location names from the article titles.

Built with FastAPI, newsapi, GeoText, and OpenStreetMap — deployable on AWS EKS.

## Getting Started

### Set up the environment

'python -m venv venv
source venv/bin/activate
pip install -r requirements.txt'

Create a .env file (based on .env.example):

'NEWS_API_KEY=your_newsapi_key_here'

### Run the app locally 
```
docker build -t geonews:latest .
docker run -p 8000:8000 -e NEWS_API_KEY=your_api_key geonews:latest
```

Visit:

http://localhost:8000/news?q=technology – News with geotagged locations
or 
http://localhost:8000 to see GeoNews UI

### Deployment
To upload new docker image to github
```
docker buildx create --use
docker buildx build \
  --platform linux/amd64 \
  -t ghcr.io/<username>/geonews:latest \
  --push .
```

# Infrastructure
Uses AWS EKS
```
eksctl create cluster \
  --name geonews-cluster \
  --region eu-central-1 \ 
  --node-type t3.small \
  --nodes 2 \
  --nodes-min 1 \
  --nodes-max 3 \
  --managed
  ```

# License
This project is licensed under the MIT License.

