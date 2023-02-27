from django.contrib import admin
from .models import Ticket, Flight, Reservation

# Register your models here.

class TicketsInline(admin.StackedInline):
    model = Ticket
    extra = 2


class ReservationAdmin(admin.ModelAdmin):
    fields = ['flight', 'num_people', 'total_cost']
    inlines = [TicketsInline]  # Load the runway inline class   





admin.site.register(Reservation, ReservationAdmin)
