from django.contrib import admin

from .models import Film, Actor, Category, Language

admin.site.register(Film)
admin.site.register(Actor)
admin.site.register(Category)
admin.site.register(Language)
