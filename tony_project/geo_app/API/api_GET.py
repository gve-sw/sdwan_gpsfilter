import urllib3
import requests
import json
import sys

def api_get(endpoint):

    vManage = "https://sdwandemo.cisco.com:443/"

    url = vManage + endpoint

    payload = ""
    auth = requests.auth.HTTPBasicAuth('demo','demo')

    headers = {
        'Accept': "application/json",
        'cache-control': "no-cache",
        #'Postman-Token': "86b19ce7-dbf3-4c5f-8c00-3cf55589443c"
        }

    # Disable the SSL certificate verification warning
    urllib3.disable_warnings()

    response = requests.request("GET",
                               url,
                               auth=auth,
                               data=payload,
                               headers=headers,
                               verify=False) # Disable SSL verification

    if response.status_code == 200:
        print('Status Code: ' + str(response.status_code))
        # Json.load method converts JSON string to Python Object (dictionnary here)
        json_data = json.loads(response.text)
        return (json_data)
    else:
        print('ERROR Code: ' + str(response.status_code))
        sys.exit(1) # Stop process