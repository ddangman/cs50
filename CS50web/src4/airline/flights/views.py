from django import forms
from django.http import HttpResponseBadRequest, HttpResponseRedirect, Http404
from django.shortcuts import render
# reverse function redirect to reverse path() defined in urls.py
from django.urls import reverse

from .models import Flight, Passenger

## Create your views here ##
def index(request):
    # Django returns all Flight available for display in the flights/index.html template
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })


def flight(request, flight_id):
    try:
        flight = Flight.objects.get(id=flight_id)
    except Flight.DoesNotExist:
        raise Http404("Flight not found.")
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all(),
        # used to add passengers who are not on the flight
        "non_passengers": Passenger.objects.exclude(flights=flight).all()
    })

def book(request, flight_id):
    # POST method should be used to manipulate data
    if request.method == "POST":
        try: # error checking to ensure that the passenger and flight exist
            # pk is the primary key
            passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
            flight = Flight.objects.get(pk=flight_id)
        except KeyError:
            return HttpResponseBadRequest("Bad Request: no flight chosen")
        except Flight.DoesNotExist:
            return HttpResponseBadRequest("Bad Request: flight does not exist")
        except Passenger.DoesNotExist:
            return HttpResponseBadRequest("Bad Request: passenger does not exist")
        # add the passenger to the flight given they both exist in database
        passenger.flights.add(flight)
        # redirect to the flight page
        return HttpResponseRedirect(reverse("flights:flight", args=(flight_id,)))