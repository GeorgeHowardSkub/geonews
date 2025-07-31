from geotext import GeoText

def extract_locations(text):
    places = GeoText(text)
    return list(set(places.cities + places.countries))