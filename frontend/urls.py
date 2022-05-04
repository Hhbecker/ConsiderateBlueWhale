
# specifies which views should be called when a given url is requested

from django.urls import path
from . import views

urlpatterns = [
    # URL pattern has three components:
    # 1. The addition to the base url of the site
    # 2. The view function you would like to be called when that url (base+addition) is requested
    # 3. The name of the ______________________ html page that should be called?

    # base URL is '' 

    # call the apiOverview view
    path('', views.apiOverview, name="overview"),
    path('library', views.library, name="library"),

]