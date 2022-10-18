from email.policy import default
from django.contrib.gis.db import models

from district.models import District, Village

# Create your models here.


class ChillType(models.Model):
    name = models.CharField(max_length=255)
    incon = models.CharField(max_length=255, default='fa-coffee')
    color = models.CharField(max_length=255, default='blue')


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


class Chill(models.Model):
    contact = models.CharField(max_length=255)
    checkin = models.CharField(max_length=255)
    checkout = models.CharField(max_length=255)
    foods = models.CharField(max_length=255)
    dishes = models.CharField(max_length=255)
    sauces = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    number_of_beds = models.CharField(max_length=255)
    number_of_rooms = models.CharField(max_length=255)
    chill = models.ForeignKey(
        ChillType, related_name="chills", on_delete=models.CASCADE)


class Media(models.Model):
    link = models.CharField(max_length=500)
    site = models.ForeignKey(TouristSites, blank=True,
                             null=True, on_delete=models.CASCADE, related_name="media")
    chill = models.ForeignKey(
        Chill, blank=True, null=True,  on_delete=models.CASCADE, related_name="media")
