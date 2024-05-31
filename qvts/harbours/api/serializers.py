from rest_framework import serializers

from qvts.harbours.models import Harbour
from qvts.harbours.models import Location
from qvts.ships.models import Ship

####################################################################################################
# Location
####################################################################################################


class LocationSerializer(serializers.ModelSerializer[Location]):
    """
    Serializer for the location model.
    """

    class Meta:
        model = Location
        fields = [
            "city",
            "country",
        ]


####################################################################################################
# Harbour
####################################################################################################


class HarbourListSerializer(serializers.ModelSerializer[Harbour]):
    """
    List serializer for the harbour model.
    """

    class Meta:
        model = Harbour
        fields = [
            "url",
            "id",
            "name",
            "berth_depth_max",
        ]

        extra_kwargs = {
            "url": {"view_name": "api:harbour-detail", "lookup_field": "pk"},
        }


class HarbourSerializer(serializers.ModelSerializer[Harbour]):
    """
    Serializer for the harbour model.
    """

    location = LocationSerializer(many=False)
    ships_in_harbour = serializers.SerializerMethodField()
    vts_centre = serializers.StringRelatedField()

    class Meta:
        model = Harbour
        fields = [
            "id",
            "uuid",
            "name",
            "berth_depth_max",
            "harbour_master",
            "location",
            "ships_in_harbour",
            "vts_centre",
        ]

    def create(self, validated_data):
        """
        Create a new harbour with a location that is created
        if it does not exist.
        """
        location_data = validated_data.pop("location")
        location, _ = Location.objects.get_or_create(**location_data)

        return Harbour.objects.create(location=location, **validated_data)

    def update(self, instance, validated_data):
        """
        Update an existing harbour with a location that is created
        if it does not exist.
        """
        location_data = validated_data.pop("location")
        location, _ = Location.objects.get_or_create(**location_data)
        instance.location = location
        instance.save()
        return super().update(instance, validated_data)

    def get_ships_in_harbour(self, obj):
        ships_in_harbour_qs = Ship.objects.get_ships_in_harbour(obj)
        return list(ships_in_harbour_qs.values_list("name", flat=True))
