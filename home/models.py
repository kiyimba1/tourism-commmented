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
    fee = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    contact_name = models.CharField(max_length=255)
    description = models.TextField()
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
    contact = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    checkin = models.CharField(max_length=255, null=True, blank=True)
    checkout = models.CharField(max_length=255, null=True, blank=True)
    foods = models.CharField(max_length=255, null=True, blank=True)
    dishes = models.CharField(max_length=255, null=True, blank=True)
    sauces = models.CharField(max_length=255, null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    location = models.PointField()
    number_of_beds = models.CharField(max_length=255, null=True, blank=True)
    number_of_rooms = models.CharField(max_length=255, null=True, blank=True)
    fee = models.TextField(null=True, blank=True)
    type = models.ForeignKey(
        ChillType, related_name="chills", on_delete=models.CASCADE)
    district = models.ForeignKey(
        District, on_delete=models.CASCADE, related_name='chills')


class Media(models.Model):
    link = models.CharField(max_length=500)
    site = models.ForeignKey(TouristSites, blank=True,
                             null=True, on_delete=models.CASCADE, related_name="media")
    chill = models.ForeignKey(
        Chill, blank=True, null=True,  on_delete=models.CASCADE, related_name="media")
