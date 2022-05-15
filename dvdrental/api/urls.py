from django.urls import path, include


urlpatterns = [
    path('customers/', include('customers.urls')),
    path('films/', include('films.urls')),
    path('rentals/', include('rentals.urls')),
]