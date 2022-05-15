from django.urls import path

from .views import RentalListView


urlpatterns = [
    path('', RentalListView.as_view(), name='rental_list'),
]
