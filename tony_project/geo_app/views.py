from django.shortcuts import render
from django.http import HttpResponse
from django.template.context import RequestContext
from django.shortcuts import redirect
from .API.get_Device_GPS import get_GPS


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

        if(region): 
            return render(request, 'geo_app/map.html', locals())

        else:
            return http