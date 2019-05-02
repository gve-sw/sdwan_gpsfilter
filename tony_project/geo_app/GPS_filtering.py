from .get_Device_GPS import get_GPS
import json
import reverse_geocode 
from geopy.geocoders import Nominatim
import certifi
import ssl
import geopy.geocoders


def map_filter(country):
	user_loc = country

	# Retrieve Device GPS locations
	GPS = get_GPS()

	ctx = ssl.create_default_context(cafile=certifi.where())
	geopy.geocoders.options.default_ssl_context = ctx
	geopy.geocoders.options.default_user_agent = "my-application"
	geolocator = Nominatim()

	map = {}

	for device in GPS:
		# print("Device : " + location + " GPS: " + GPS[location]['GPS'])
		coordinates = GPS[device]['GPS']
		loc = geolocator.reverse(coordinates)
		country = loc.raw['address']['country']

		if country == user_loc:
			map.update ({device: {'Country': country, 'GPS' : coordinates}})
	
	return (map) 


