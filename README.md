# CSAP_FY2019_SDWAN

## How to start

1. Clone the repository
2. Go into the directory tony_project
3. Start the web server via: python3 manage.py runserver
4. Open the website via: http://127.0.0.1:8000/geo_app/

Now there should be a login mask that looks like the one vManage usually provides. The login credentials are hard coded into the Python code so far (a database will added later on) and there are two different accounts:

1. Lee // eggroll
2. Tony // burger

If the login is successfull, the user is redirected to the page tony_project/geo_app/templates/geo_app/map.html

Currently it did not work that any parameters are sent to map.html, but the plan is to send the users country via a GET or POST parameter to map.html, so that we can include a map on the page and filter by the given country.

Example: Lee logs in successfully, the string "China" is send to map.html and on map.html we poll the vEdge routers, filter for everything that can be seen in "China" (or "Asia" or however we want to name them later).
