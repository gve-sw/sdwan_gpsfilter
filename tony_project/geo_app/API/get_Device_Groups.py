from .api_GET import api_get
import json

def api_device_group(region):
	response = api_get("dataservice/group/devices?groupId=" + region)
	data = response['data']

	map = {}

	for item in data:
		hostname = item['host-name']
		device_type = item['device-model']
		latitude = float(item['latitude'])
		longitude = float(item['longitude'])
		coordinates = (latitude, longitude)
		map.update ({hostname: {'Type': device_type, 'lat' : latitude, 'lon' : longitude}})


	json_map = json.dumps(map)

	return (json_map) 

    