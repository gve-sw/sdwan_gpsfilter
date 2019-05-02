from .api_GET import api_get


def get_GPS():

    response = api_get("dataservice/device")
    data = response['data']

    location = {}

    for item in data:
        hostname = item['host-name']
        device_type = item['device-type']
        latitude = float(item['latitude'])
        longitude = float(item['longitude'])

        #location.update ({hostname: {'Device-type': device_type, 'GPS' : latitude + " , " + longitude}})
        location.update ({hostname: {'Device-type': device_type, 'lat' : latitude, 'lon' : longitude}})

    return (location)


    