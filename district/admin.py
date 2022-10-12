from django.contrib.gis import admin

from district.models import District
from leaflet.admin import LeafletGeoAdmin


# Register your models here.


@admin.register(District)
class District(LeafletGeoAdmin):
    list_display = ('name', 'geom')
