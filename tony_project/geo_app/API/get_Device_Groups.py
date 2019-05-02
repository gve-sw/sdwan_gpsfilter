from api_GET import api_get

def api_device_group():

    # Retrieve Devices Groups
    data = api_get("dataservice/group/device")
    return(data)
