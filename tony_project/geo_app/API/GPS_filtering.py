from .get_Device_GPS import get_GPS
import json
import reverse_geocode 
from geopy.geocoders import Nominatim
import certifi
import ssl
import geopy.geocoders
import reverse_geocoder as rg


def map_filter(country):
    user_loc = country
    
    # Retrieve Device GPS locations
    GPS = get_GPS()

    map = {}

    for device in GPS:
        
        coordinates = (GPS[device]['lat'], GPS[device]['lon'])

        loc = rg.search(coordinates)
        country = loc[0]['cc']

        if country == user_loc:
            map.update ({device: {'Country': country, 'GPS' : coordinates}})
	
    return (map) 


