from django.contrib import admin
from App1.models.student import Student
from App1.models.address import Country
from App1.models.address import State
from App1.models.address import City
from App1.models.user import User
from App1.models.black_listed_token import BlackListedToken



class StudentUser(admin.ModelAdmin):
    list_display = ('id', 'name', 'subject', 'address', 'number')


class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'country')


class StateAdmin(admin.ModelAdmin):
    list_display = ('id', 'state')


class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'city')


admin.site.register(Student, StudentUser)
admin.site.register(Country, CountryAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(User)
admin.site.register(BlackListedToken)

