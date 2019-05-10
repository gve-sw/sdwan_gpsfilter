from django.shortcuts import render
from django.http import HttpResponse
from django.template.context import RequestContext
from django.shortcuts import redirect
from .API.get_Device_GPS import get_GPS
import json


def check_creds(username, password):
    if(username == 'Roberto' and password == '1'):
        return 'BR'
    if(username == 'Tony' and password == '1'):
        return 'US'
    return False

def index (request):

    http = render(request, 'geo_app/index.html', {})

    if request.method == 'GET':
        return http

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        region = check_creds(username, password)

        display = get_GPS(region)

        display_json = json.loads(display)

        print("Display ========================================")
        print(display_json)
        print("================================================")

        


        for device in display_json:
            print(device)

            dscr = '''<iframe srcdoc='<html><b>Name: {}</b><br>Polled via dataservice/device/data/<br><br><b>GPS: ({}, {})</b><br>Polled via dataservice/device/data/<br><br>Visible because user <b>{}</b> is from <b>{}</b></html>'></iframe>'''.format(device, display_json[device]["lat"], display_json[device]["lon"], username, region)
            # <iframe style="width:100%; height:500px;overflow:auto;">
            #dscr = '''<iframe srcdoc='<html>Hallo</html>'</iframe>'''
            temp = {"dscr": dscr}
            display_json[device].update(temp)
        display = json.dumps(display_json)

        print("Display ========================================")
        print(display_json)
        print("================================================")


        if(region): 
            return render(request, 'geo_app/map.html', locals())

        else:
            return http