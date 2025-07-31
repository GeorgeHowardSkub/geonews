from geopy.geocoders import Nominatim
import time

geolocator = Nominatim(user_agent="geonews")

def get_coordinates(place_name):
    try:
        location = geolocator.geocode(place_name)
        time.sleep(5)
        if location:
            return {"lat": location.latitude, "lng": location.longitude}
    except Exception:
        pass
    return None