from django.contrib import admin

from .models import Airport, Flight, Passenger


# configure the admin interface to display the duration of the flight
class FlightAdmin(admin.ModelAdmin):
    list_display = ("__str__", "duration")

# configure the admin interface to display the flights that the passenger is on
class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)
    

# Register your models here.
admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, PassengerAdmin)
