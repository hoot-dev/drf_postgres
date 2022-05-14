from django.urls import path, include

from .views import FilmListView

urlpatterns = [
    path('', FilmListView.as_view(), name='film_list'),
]