# SD-WAN GPS Filter with Security

# Introduction 

SD-WAN features from Viptela with Geo location requirements need to be crossed with another features such as role-based access control in specific feature with security enhancements.

This code shows a customize  portal that  align Geo-locations  devices and role-base access control  security  feature  to offer secure sd-wan 

# High level Design

![High Level Design](https://github.com/moacosta/sdwan_gpsfilter/blob/master/GPS_Vitpela_PoV.png)


# Mock up 

![Mock Up](https://github.com/moacosta/sdwan_gpsfilter/blob/master/GPS_Viptela2.3png)



# How to start

Be aware that you need to have a Viptela solutioon and have vManage to add this feature. 

1. Clone the repository
2. Go into the directory tony_project
3. Start the web server via: python3 manage.py runserver
4. Open the website via: http://127.0.0.1:8000/geo_app/

Now there should be a login mask that looks like the one vManage usually provides. The login credentials are hard coded into the Python code so far (a database will added later on) and there are two different accounts:

1. Roberto // 1
2. Tony // 1

If the login is successfull, the user is redirected to the page tony_project/geo_app/templates/geo_app/map.html

This mock up only display showing the on the map, to show the gps feature. 

Currently it does not work that any parameters are sent to map.html, but to have the full feature it is needed to send the users country via a GET or POST parameter to map.html, so that we can include a map on the page and filter by the given country.

Example: Lee logs in successfully, the string "China" is send to map.html and on map.html we poll the vEdge routers, filter for everything that can be seen in "China" (or "Asia" or however we want to name them later).
