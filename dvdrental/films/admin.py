from django.contrib import admin

from .models import Film, FilmActor, FilmCategory, Actor, Category, Language

admin.site.register(Film)
admin.site.register(FilmActor)
admin.site.register(FilmCategory)
admin.site.register(Actor)
admin.site.register(Category)
admin.site.register(Language)
