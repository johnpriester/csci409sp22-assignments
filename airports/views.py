from django.http import HttpResponse
from django.shortcuts import render
from .models import Airport
from flights.models import Flight
from tickets.forms import TicketForm
from tickets.models import Reservation
def index(request):
    #Fetch all airports from Database
    airports = Airport.objects.all()
    #place all airports in context variable for retriveal in view
    context = {'airports': airports}
    return render(request, 'airports/index.html', context)


def airport_info(request, airport_code):
    # Fetch the airport by a certain code
    # Remember we are only expecting one airport per code we should use get
    airport = Airport.objects.get(airport_code=airport_code)
    # Display the airport name and code
    context = {'airport': airport}
    return render(request, 'airports/airports.html', context)

