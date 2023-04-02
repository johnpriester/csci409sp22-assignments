from django.urls import path
from . import views
urlpatterns = [
    path('/', views.index),
    path('/search/<str:origin>/<str:destination>/', views.flight_search),
    path('/search/', views.search),
]
