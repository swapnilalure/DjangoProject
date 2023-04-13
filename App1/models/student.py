from django.db import models

from App1.models.address import City


class Student(models.Model):
    name = models.CharField(max_length=50, default='', null=False, blank=False)
    subject = models.CharField(max_length=50, default='', null=False, blank=False)
    address = models.ForeignKey(City, on_delete=models.CASCADE)
    number = models.CharField(max_length=10, default='', null=True, blank=True)


    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name