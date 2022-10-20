from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
from rest_framework.response import Response
from rest_framework.views import APIView

from district.models import District
from home.models import Chill, TouristSites
from home.serializers import ChillSerializer, SiteSerializer
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt

from home.utils import chill_data

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


def get_chills(request):
    # hotels = serialize('geojson', Chill.objects.all())
    hotels = ChillSerializer(Chill.objects.all(), many=True)
    return Response(hotels.data)


class ChillsView(APIView):
    serializer_class = ChillSerializer

    def get(self, request):
        hotels = ChillSerializer(Chill.objects.all(), many=True)
        return Response(hotels.data)


class SitesView(APIView):
    serializer_class = TouristSites

    def get(self, request):
        sites = SiteSerializer(TouristSites.objects.all(), many=True)
        return Response(sites.data)


@csrf_exempt
def upload_file(request):
    if request.method == "POST":
        file = request.FILES["file"]
        # print(file)
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        file_path = fs.path(filename)
        print(file_path)
        task = chill_data(file_path)
    return JsonResponse({"status": "ok"})
