from django.urls import path, include

from .views import CustomerListView


urlpatterns = [
    path('', CustomerListView.as_view(), name='customer_list'),
]