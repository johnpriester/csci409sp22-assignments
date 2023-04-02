from django.http import HttpResponse
from django.shortcuts import render
from .models import Flight # Import Flight model
from airports.models import Airport # Import airport model to get airport id and code
from .forms import FlightForm
def index(request):
    # Fetch all flights
    # CHANGED FOR assignment 10
    form = FlightForm()
    return render(request, 'flights/index.html', {'form': form})


def search(request):
    form = FlightForm(request.POST)
    if form.is_valid():
        origin = form.cleaned_data['origin']
        destination = form.cleaned_data['destination']
    #Fetch all airports from Database
    origin = Airport.objects.get(airport_code=origin)
    destination = Airport.objects.get(airport_code=destination)
    #place all airports in context variable for retriveal in view
    flight = Flight.objects.filter(origin=origin, destination=destination)
    context = {'flight': flight}
    return render(request, 'flights/flight_search.html', context)

def flight_search(request, origin, destination):
    origin = Airport.objects.get(airport_code=origin)
    destination = Airport.objects.get(airport_code=destination)
     #Code to select flights from the database
    flights = Flight.objects.filter(origin_id=origin, destination_id=destination)
    flight_list = ', '.join([f.origin.airport_code + "->" + f.destination.airport_code + " Airline Code: " +
                             f.airline.airline_code for f in flights])
    return HttpResponse('Showing flights: ' + flight_list)



