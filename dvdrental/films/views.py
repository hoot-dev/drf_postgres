from rest_framework import generics

from .models import Film
from .serializers import FilmSerializer


class FilmListView(generics.ListAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
