from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello from routes')

def route_search(request, flight_origin, flight_destination):
    return HttpResponse("Showing routes from " + str(flight_origin) + " to " + str(flight_destination));