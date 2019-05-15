from django.shortcuts import render
from django.http import HttpResponse
from django.template.context import RequestContext
from django.shortcuts import redirect
from .API.get_Device_GPS import get_GPS
from .API.get_Device_Groups import api_device_group
import json
from django.template.loader import render_to_string




def check_creds(username, password):
    if(username == 'Roberto' and password == '1'):
        return 'BR', 'America'
    if(username == 'Tony' and password == '1'):
        return 'US', 'America'
    return False

def index (request):

    http = render(request, 'geo_app/index.html', {})

    if request.method == 'GET':
        return http

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        country, region = check_creds(username, password)

        if(region): 
            return render(request, 'geo_app/choice.html', locals())

        else:
            return http

def map_country (request, country):

    country = country
    display = get_GPS(country)

    display_json = json.loads(display)

    for device in display_json:

        dscr = '''<iframe srcdoc='<html><b>Name: {}</b><br>Polled via dataservice/device/data/<br><br><b>GPS: ({}, {})</b><br>Polled via dataservice/device/data/<br><br>Visible because user <b></b> is from <b>{}</b></html>'></iframe>'''.format(device, display_json[device]["lat"], display_json[device]["lon"], country)
        # <iframe style="width:100%; height:500px;overflow:auto;">
        #dscr = '''<iframe srcdoc='<html>Hallo</html>'</iframe>'''
        temp = {"dscr": dscr}
        display_json[device].update(temp)
        display = json.dumps(display_json)


    return render(request, 'geo_app/map.html', locals())



def map_region (request, region):

    region = region
    display = api_device_group(region)
    print("this is a test")
    print(display)


    display_json = json.loads(display)

    for device in display_json:

        dscr = '''<iframe srcdoc='<html><b>Name: {}</b><br>Polled via dataservice/group/devices?groupId={})<br><br><b>GPS: ({}, {})</b><br>Polled via dataservice/device/data/<br><br>Visible because user <b></b> is from <b>{}</b></html>'></iframe>'''.format(device,region, display_json[device]["lat"], display_json[device]["lon"], region)
        # <iframe style="width:100%; height:500px;overflow:auto;">
        #dscr = '''<iframe srcdoc='<html>Hallo</html>'</iframe>'''
        temp = {"dscr": dscr}
        display_json[device].update(temp)
        display = json.dumps(display_json)


    return render(request, 'geo_app/map.html', locals())
