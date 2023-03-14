from django.urls import path
from . import views
urlpatterns = [
    path('/', views.index),
    path('/<str:origin>/<str:destination>/', views.flight_search),
]
