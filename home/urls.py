from django.urls import path

from home.views import ChillsView, HomePage, SitesView, district_dataset, get_chills, get_sites, upload_file

urlpatterns = [
    path('district_data', district_dataset, name='districts'),
    path('sites_data', SitesView.as_view(), name='get_sites'),
    path('chills_data', ChillsView.as_view(), name='get_chills'),
    path('add_chill', upload_file, name="upload_file"),
    path("", HomePage.as_view(), name="home")
]
