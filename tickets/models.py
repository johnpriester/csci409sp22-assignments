from django.db import models
from flights.models import Flight
# Create your models here.
class Reservation(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.PROTECT)
    num_people = models.IntegerField()
    total_cost = models.DecimalField(max_digits=5, decimal_places=2)

class Ticket(models.Model):
    firstClass = 'F'
    businessClass = 'B'
    mainCabin = 'M'
    TICKET_DESIGNATION_CHOICES = [
        (firstClass, 'First Class'),
        (businessClass, 'Business Class'),
        (mainCabin, 'Main Cabin'),
    ]
    reservation = models.ForeignKey(Reservation, on_delete=models.PROTECT)
    seat = models.CharField(max_length=10)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    ticket_class = models.CharField(
        max_length=1,
        choices=TICKET_DESIGNATION_CHOICES,
        default=mainCabin
    )