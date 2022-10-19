from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin

from .models import ChillType, TouristSites

# Register your models here.


@admin.register(TouristSites)
class TouristSites(LeafletGeoAdmin):
    list_display = ('name', 'location')


class ChillTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "color", "incon")
    list_editable = ("color", "incon")


admin.site.register(ChillType, ChillTypeAdmin)
