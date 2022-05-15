from rest_framework import serializers

from .models import Staff, Store, Inventory, Payment, Rental
from films.serializers import ShortFilmSerializer
from customers.serializers import CustomerSerializer


class InventorySerializer(serializers.ModelSerializer):
    film =  ShortFilmSerializer()
    class Meta:
        model = Inventory
        fields = [
            'inventory_id',
            'film',
            'store'
        ]

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = [
            'amount',
            'payment_date'
        ]


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = [
            'first_name',
            'last_name',
            'email',
            'store_id',
        ]


class RentalSerializer(serializers.ModelSerializer):
    inventory = InventorySerializer()
    customer = CustomerSerializer()
    staff = StaffSerializer()
    payments = PaymentSerializer(many=True)
    class Meta:
        model = Rental
        fields = [
            'rental_date',
            'return_date',
            'inventory',
            'customer',
            'staff',
            'payments'
        ]