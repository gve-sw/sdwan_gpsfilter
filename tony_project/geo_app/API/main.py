from get_Device_Groups import api_device_group
import json

if __name__ == '__main__':

    # Retrieve Devices Groups
    #DG = api_device_group()

    # Retrieve Device GPS locations
    #GPS = get_GPS()

    display = api_device_group("europe")

    # Json.dumps method converts the dictionary it into a JSON string for a prettier display
    pretty_json = (json.dumps(display, indent=3, sort_keys=True))
    print(pretty_json)