from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin

from .models import TouristSites

# Register your models here.


@admin.register(TouristSites)
class TouristSites(LeafletGeoAdmin):
    list_display = ('name', 'location')
