from statistics import mode
from unicodedata import name
from django.contrib.gis.db import models

# Create your models here.


class District(models.Model):
    name = models.CharField(max_length=255)
    geom = models.MultiPolygonField()

class Village(models.Model):
    name = models.CharField(max_length=255)
