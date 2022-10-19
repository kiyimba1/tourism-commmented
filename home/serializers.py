from rest_framework_gis import serializers

from home.models import Chill, ChillType, Media, TouristSites


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = "__all__"


class ChillTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChillType
        fields = ('name', 'incon', 'color')


class ChillSerializer(serializers.GeoFeatureModelSerializer):
    type = ChillTypeSerializer()
    media = MediaSerializer(many=True)

    class Meta:
        model = Chill
        fields = ("name", "contact", "checkin", "checkout", "foods", "dishes",
                  "sauces", "website", "email", "number_of_beds", "number_of_rooms", "fee", "type", "media")
        geo_field = "location"


class SiteSerializer(serializers.GeoFeatureModelSerializer):
    media = MediaSerializer(many=True)

    class Meta:
        model = TouristSites
        fields = ("name", "year_of_inception", "fee", "phone", "contact_name",
                  "popular_stop_overs", "nearest_main_hospital", "email", "fee", "media", "description")
        geo_field = "location"
