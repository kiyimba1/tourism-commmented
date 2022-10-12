from django.contrib.gis.db import models

from district.models import District, Village

# Create your models here.


class TouristSites(models.Model):
    name = models.CharField(max_length=255)
    year_of_inception = models.CharField(max_length=255, null=True, blank=True)
    fee = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    contact_name = models.CharField(max_length=255)
    popular_stop_overs = models.CharField(
        max_length=255, blank=True, null=True)
    nearest_main_hospital = models.CharField(
        max_length=255, null=True, blank=True)
    location = models.PointField()
    district = models.ForeignKey(
        District, on_delete=models.CASCADE, related_name='sites')
    village = models.ForeignKey(
        Village, on_delete=models.CASCADE, related_name='sites')
