from django.contrib import admin
from App1.models.student import Student
from App1.models.address import Country
from App1.models.address import State
from App1.models.address import City
from App1.models.user import User


class StudentUser(admin.ModelAdmin):
    list_display = ('name', 'subject', 'address', 'number')


# Register your models here.
admin.site.register(Student, StudentUser)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)

admin.site.register(User)

