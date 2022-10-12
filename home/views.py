from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse
from django.core.serializers import serialize

from district.models import District
from home.models import TouristSites

# Create your views here.


class HomePage(ListView):
    context_object_name = 'districts'
    queryset = District.objects.all()
    template_name = 'home/home.html'


def district_dataset(request):
    district = serialize('geojson', District.objects.all())
    print("alled")
    return HttpResponse(district, content_type='json')


def get_sites(request):
    sites = serialize('geojson', TouristSites.objects.all())
    return HttpResponse(sites, content_type='json')
