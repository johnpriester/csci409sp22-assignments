from django.http import HttpResponse
from django.shortcuts import render
from .models import Reservation
from .forms import TicketForm
from django.contrib.auth.decorators import login_required
@login_required
def index(request):
    # Create instance of form class
    form = TicketForm()
    return render(request, 'tickets/index.html', {'form': form})
    #return HttpResponse('Hello from tickets')


@login_required
def search(request):
    form = TicketForm(request.POST)
    if form.is_valid():
        reservation = Reservation.objects.get(id=form.cleaned_data['confirmation_number'])
        return render(request, 'tickets/ticket_search.html', {'reservation': reservation})
@login_required
def ticket_search(request, confirmation_number):
    # Select the singular reservation for the confirmation number
    # Note: the confirmation_number is the id in the Reservation table
    reservation = Reservation.objects.get(id=confirmation_number)
    return HttpResponse('Number of tickets for confirmation number: ' + str(confirmation_number) + " is " + str(reservation.num_people))