from rest_framework import serializers

from .models import Film, Language, Actor, Category


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = [
            'first_name',
            'last_name'
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name'
        ]


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = [
            'name'
        ]

class FilmSerializer(serializers.ModelSerializer):
    language = LanguageSerializer()
    actors = ActorSerializer(many=True)
    categories = CategorySerializer(many=True)

    class Meta:
        model = Film
        fields = [
            'title',
            'description',
            'release_year',
            'rental_duration',
            'rental_rate',
            'length',
            'replacement_cost',
            'rating',
            'special_features',
            'language',
            'actors',
            'categories'
        ]
    
    def to_representation(self, obj):
        representation = super().to_representation(obj)
        flat_representation = representation.pop('language')
        representation['language'] = flat_representation['name']
        return representation

class ShortFilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = [
            'title',
            'rental_rate'
        ]