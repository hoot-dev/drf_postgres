from rest_framework import serializers

from .models import Customer, Address, City, Country


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = [
            'country'
        ]

class CitySerializer(serializers.ModelSerializer):
    country = CountrySerializer()
    class Meta:
        model = City
        fields = [
            'city',
            'country'
        ]
    
    def to_representation(self, obj):
        representation = super().to_representation(obj)
        flat_representation = representation.pop('country')
        for key in flat_representation:
            representation[key] = flat_representation[key]

        return representation

class AddressSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    class Meta:
        model = Address
        fields = [
            'address',
            'city',
            'postal_code',
            'district',
            'phone'
        ]
    
    def to_representation(self, obj):
        representation = super().to_representation(obj)
        flat_representation = representation.pop('city')
        for key in flat_representation:
            representation[key] = flat_representation[key]

        return representation

class CustomerSerializer(serializers.ModelSerializer):
    contact_info = AddressSerializer()

    class Meta:
        model = Customer
        fields = [
            'first_name',
            'last_name',
            'email',
            'contact_info'
        ]
