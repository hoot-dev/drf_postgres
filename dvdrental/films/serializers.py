from rest_framework import serializers

from .models import Film, Language


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = [
            'name'
        ]

class FilmSerializer(serializers.ModelSerializer):
    language = LanguageSerializer()

    class Meta:
        model = Film
        fields = [
            'title',
            'description',
            'release_year',
            'rental_duration',
            'length',
            'replacement_cost',
            'rating',
            'special_features',
            'language'
        ]
    
    def to_representation(self, obj):
        representation = super().to_representation(obj)
        flat_representation = representation.pop('language')
        representation['language'] = flat_representation['name']
        return representation