import googlemaps
from datetime import datetime
import json

gmaps = googlemaps.Client(key="AIzaSyAYxbcOA_G3K6lbXREMwlgvE7z4AYhqReU")
now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="driving",
                                     departure_time=now)
print(json.dumps(directions_result, indent=4))