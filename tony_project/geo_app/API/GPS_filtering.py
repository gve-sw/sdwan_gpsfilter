from .get_Device_GPS import get_GPS
import json
import reverse_geocode 
from geopy.geocoders import Nominatim
import certifi
import ssl
import reverse_geocoder as rg
import json


def map_filter(country):
    user_loc = country
    
    # Retrieve Device GPS locations
    GPS = get_GPS()

    map = []

    for device in GPS:
        
        coordinates = (GPS[device]['lat'], GPS[device]['lon'])

        loc = rg.search(coordinates)
        country = loc[0]['cc']

        if country == user_loc:
            map.append (    ({'device' : device, 'Country' : country, 'GPS' : coordinates})     )
    #print("Map:")
    #print(map)

    json_map = json.dumps(map)
    print("JSON Map:")
    print(json_map)

    return (json_map) 


