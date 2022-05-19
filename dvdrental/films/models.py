import datetime

from django.db import models

from django.contrib.postgres.search import SearchVectorField
from django.contrib.postgres.indexes import GinIndex
from django.contrib.postgres.fields import ArrayField


class Actor(models.Model):
    actor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'actor'
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'category'
    
    def __str__(self):
        return self.name


class Film(models.Model):
    ratings = (
        ('G', 'G'),
        ('PG', 'PG'),
        ('PG-13', 'PG-13'),
        ('R', 'R'),
        ('NC-17', 'NC-17')
    )
    film_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    release_year = models.IntegerField(blank=True, null=True)
    language = models.ForeignKey('Language', models.DO_NOTHING)
    rental_duration = models.SmallIntegerField()
    rental_rate = models.DecimalField(max_digits=4, decimal_places=2)
    length = models.SmallIntegerField(blank=True, null=True)
    replacement_cost = models.DecimalField(max_digits=5, decimal_places=2)
    rating = models.CharField(max_length=6, blank=True, null=True, choices=ratings)
    last_update = models.DateTimeField(auto_now=True)
    # Postgres ArrayField - https://docs.djangoproject.com/en/3.2/ref/contrib/postgres/fields/
    # This can basically be used as "tags" for this model
    special_features = ArrayField(models.CharField(max_length=100, blank=True, null=True))
    # Full text search field (tsvector) in postgres - https://pganalyze.com/blog/full-text-search-django-postgres
    fulltext = SearchVectorField(null=True)
    actors = models.ManyToManyField(Actor, through='FilmActor', related_name='films')
    categories = models.ManyToManyField(Category, through='FilmCategory', related_name='films')

    class Meta:
        db_table = 'film'
        # Indexing full text search field in postgres
        indexes = (GinIndex(fields=['fulltext']),)
    
    def __str__(self):
        return self.title


class FilmActor(models.Model):
    actor = models.ForeignKey(Actor, models.CASCADE)
    film = models.ForeignKey(Film, models.CASCADE)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'film_actor'
        unique_together = (('actor', 'film'),)
    
    def __str__(self):
        return f'{self.film} - {self.actor}'


class FilmCategory(models.Model):
    film = models.ForeignKey(Film, models.CASCADE)
    category = models.ForeignKey(Category, models.CASCADE)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'film_category'
        unique_together = (('film', 'category'),)
    
    def __str__(self):
        return f'{self.film} - {self.category}'


class Language(models.Model):
    language_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'language'
    
    def __str__(self):
        return self.name
