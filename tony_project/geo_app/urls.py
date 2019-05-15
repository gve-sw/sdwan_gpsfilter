from django.urls import path, include


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', include('django.contrib.auth.urls')),
    path('map/gps/<country>', views.map_country), 
    path('map/device/<region>', views.map_region),  
]
