from django.shortcuts import render
from django.http import HttpResponse
from django.template.context import RequestContext
from django.shortcuts import redirect
from .GPS_filtering import map_filter

def check_creds(username, password):
    if(username == 'Lee' and password == 'eggroll'):
        return 'China'
    if(username == 'Tony' and password == 'burger'):
        return 'USA'
    return False

def index (request):

    http = render(request, 'geo_app/index.html', {})

    if request.method == 'GET':
        return http

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        region = check_creds(username, password)

        display = map_filter(region)

        if(region): 
            return render(request, 'geo_app/map.html', locals())

        else:
            return http