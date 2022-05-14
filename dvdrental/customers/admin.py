from django.contrib import admin

from .models import Customer, Address, City, Country

admin.site.register(Customer)
admin.site.register(Address)
admin.site.register(City)
admin.site.register(Country)
