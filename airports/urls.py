# Load path from django.urls
from django.urls import path
# Load this applications views.py file
from . import views

# define url patterns
urlpatterns = [
    # get index view
    # example url : /airports/
    path('/', views.index),
    # show airport info
    # example url /airports/MYR
    # notice the airport_code parameter in the url matches
    # the parameter in the airport_info function
    path('/<str:airport_code>', views.airport_info),
]