from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello from flights');

def flight_search(request, flight_origin, flight_destination):
    # return HttpResponse(f'Showing flights from {flight_origin} to {flight_destination}');
    return HttpResponse("Showing flights from " + str(flight_origin) + " to " + str(flight_destination));



