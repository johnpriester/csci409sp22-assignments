from django.urls import path
from . import views
urlpatterns = [
    path('/', views.index),
    path('/<str:flight_origin>/<str:flight_destination>/', views.route_search),
]