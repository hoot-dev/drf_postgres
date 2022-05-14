from django.contrib import admin

from .models import Store, Staff, Rental, Payment, Inventory


admin.site.register(Store)
admin.site.register(Staff)
admin.site.register(Rental)
admin.site.register(Payment)
admin.site.register(Inventory)