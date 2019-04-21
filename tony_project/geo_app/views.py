from django.shortcuts import render
from django.http import HttpResponse
from django.template.context import RequestContext
from django.shortcuts import redirect

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
        if(region): 
            return redirect('map')
        else:
            return http

    #return render(request, 'geo_app/index.html', {})
    #return HttpResponse(t.render(c))
    #return render_to_response('tony_project/geo_app/index.html')

#def index(request):
#    return HttpResponse("Welcome to the SD WAN Login page. Please login.")

def map(request):
     #print(region)
     http = render(request, 'geo_app/map.html', {})
     return http
    

# Create your views here.
