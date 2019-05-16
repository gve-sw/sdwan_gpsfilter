from .api_GET import api_get
import json
import reverse_geocode 
from geopy.geocoders import Nominatim
import certifi
import ssl
import reverse_geocoder as rg
import json


def get_GPS(country):

    user_loc = country

    response = api_get("dataservice/device")
    data = response['data']
    
    map = {}

    for item in data:
        hostname = item['host-name']
        device_type = item['device-type']
        latitude = float(item['latitude'])
        longitude = float(item['longitude'])
        coordinates = (latitude, longitude)

        #location.update ({hostname: {'Device-type': device_type, 'GPS' : latitude + " , " + longitude}})
        #location.update ({hostname: {'Device-type': device_type, 'lat' : latitude, 'lon' : longitude}})

        loc = rg.search(coordinates)
        country = loc[0]['cc']

        if country == user_loc:
            map.update ({hostname: {'Country': country, 'lat' : latitude, 'lon' : longitude}})


    json_map = json.dumps(map)

    return (json_map) 

    