from django.db import models


# Country -----1
class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# State -----2
class State(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# City -----3
class City(models.Model):
    name = models.CharField(max_length=50)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
