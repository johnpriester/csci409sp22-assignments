from django.contrib import admin
from .models import Airport, Runway


# Register your models here.
class RunwayInline(admin.StackedInline):
    model = Runway
    extra = 2


class AirportAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name','airport_code','is_open']}),
        ('Airport Address', {'fields': ['address', 'city', 'state', 'zipcode'], 'classes': ['collapse']})
    ]
    inlines = [RunwayInline] #Load the runway inline class
admin.site.register(Airport, AirportAdmin)