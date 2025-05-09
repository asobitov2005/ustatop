from django.contrib import admin
from location.models import *


class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)


class AddressAdmin(admin.ModelAdmin):
    list_display = ('street_name',)
    search_fields = ('street_name',)
    list_filter = ('street_name',)



admin.site.register(City, CityAdmin)
admin.site.register(Address, AddressAdmin)