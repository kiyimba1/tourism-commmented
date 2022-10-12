from django.urls import path

from home.views import HomePage, district_dataset, get_sites

urlpatterns = [
    path('district_data', district_dataset, name='districts'),
    path('sites_data', get_sites, name='get_sites'),
    path("", HomePage.as_view(), name="home")
]
