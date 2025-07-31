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
'uvicorn app.main:app --reload'

Visit:

http://127.0.0.1:8000/docs – Swagger API docs

http://127.0.0.1:8000/news?q=technology – News with geotagged locations

# License
This project is licensed under the MIT License. See the LICENSE file for details.

