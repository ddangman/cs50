from django.db import models

### Create your models here ###

# Create a new model called Airport that has the following fields:
class Airport(models.Model):
    # code - a unique 3 letter code for each airport
    code = models.CharField(max_length=3)
    # city - the city where the airport is located
    city = models.CharField(max_length=64)

    # Add a __str__ method to the Airport model that returns the city of the airport and its code in parentheses
    def __str__(self):
        return f"{self.city} ({self.code})"

# must run python manage.py makemigrations and python manage.py migrate after creating models
class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id} : {self.origin} to {self.destination}"


class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.first} {self.last}"