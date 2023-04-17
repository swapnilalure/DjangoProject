from django.db import models


# Country -----1
class Country(models.Model):
    country = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.country


# State -----2
class State(models.Model):
    state = models.CharField(max_length=50, blank=False, null=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True, related_name="cty_name")

    def __str__(self):
        return self.state


# City -----3
class City(models.Model):
    city = models.CharField(max_length=50, blank=False, null=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True, related_name="cty_name_c")
    state = models.ForeignKey(State, on_delete=models.CASCADE, blank=True, null=True, related_name="ste_name")

    def __str__(self):
        return self.city
