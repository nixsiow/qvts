from rest_framework import serializers

from qvts.harbours.api.serializers import HarbourSerializer
from qvts.harbours.models import Harbour
from qvts.harbours.models import Location
from qvts.ships.api.services import create_ship
from qvts.ships.api.services import update_ship
from qvts.ships.models import ContactPerson
from qvts.ships.models import OperatingCompany
from qvts.ships.models import Ship
from qvts.ships.models import ShipMovement

####################################################################################################
# ContactPerson
####################################################################################################


class ContactPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactPerson
        fields = [
            "name",
            "phone",
            "email",
        ]


####################################################################################################
# OperatingCompany
####################################################################################################


class OperatingCompanySerializer(serializers.ModelSerializer):
    contact_person = ContactPersonSerializer(many=False, required=False)

    class Meta:
        model = OperatingCompany
        fields = [
            "name",
            "contact_person",
        ]


####################################################################################################
# Ship
####################################################################################################


class ShipListSerializer(serializers.ModelSerializer[Ship]):
    age = serializers.SerializerMethodField()

    class Meta:
        model = Ship
        fields = [
            "url",
            "name",
            "tonnage",
            "draft_max_load",
            "draft_dry",
            "type",
            "beam",
            "length",
            "flag",
            "year_built",
            "age",
        ]

        extra_kwargs = {
            "url": {"view_name": "api:ship-detail", "lookup_field": "pk"},
        }

    def get_age(self, obj):
        return obj.get_age()


class ShipSerializer(serializers.ModelSerializer[Ship]):
    operating_company = OperatingCompanySerializer(many=False, required=False)
    visited_harbours = serializers.SerializerMethodField()
    ship_movements = serializers.StringRelatedField(many=True, read_only=True)  # type: ignore[var-annotated]

    class Meta:
        model = Ship
        fields = [
            "name",
            "tonnage",
            "draft_max_load",
            "draft_dry",
            "type",
            "beam",
            "length",
            "flag",
            "year_built",
            "operating_company",
            "ship_movements",
            "visited_harbours",
        ]

    def get_visited_harbours(self, obj):
        return obj.get_visited_harbours()

    def create(self, validated_data):
        """
        Invoke the service to create a new ship.
        """
        return create_ship(validated_data)

    def update(self, instance, validated_data):
        """
        Update an existing ship with an operating company that is created
        if it does not exist.
        """
        ship, validated_data = update_ship(instance, validated_data)
        return super().update(ship, validated_data)


####################################################################################################
# ShipMovement
####################################################################################################


class ShipMovementListSerializer(serializers.ModelSerializer[ShipMovement]):
    url = serializers.HyperlinkedIdentityField(view_name="api:shipmovement-detail")
    ship = serializers.StringRelatedField(many=False)
    harbour = serializers.StringRelatedField(many=False)
    # ship = ShipNoURLSerializer(many=False, read_only=True)
    # harbour = HarbourSerializer(many=False, read_only=True)
    entered_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    exited_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = ShipMovement
        fields = [
            "url",
            "ship",
            "harbour",
            "entered_at",
            "exited_at",
        ]


class ShipMovementDetailSerializer(serializers.ModelSerializer[ShipMovement]):
    ship = serializers.StringRelatedField(many=False)
    harbour = serializers.StringRelatedField(many=False)
    # ship = ShipNoURLSerializer(many=False, read_only=True)
    # harbour = HarbourSerializer(many=False, read_only=True)
    entered_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    exited_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)

    class Meta:
        model = ShipMovement
        fields = [
            "ship",
            "harbour",
            "entered_at",
            "exited_at",
        ]


class ShipMovementSerializer(serializers.ModelSerializer[ShipMovement]):
    # ship = serializers.StringRelatedField(many=False)
    # harbour = serializers.StringRelatedField(many=False)
    ship = ShipSerializer(many=False)
    harbour = HarbourSerializer(many=False)
    entered_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", input_formats=["%Y-%m-%d %H:%M:%S"])
    exited_at = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M:%S",
        input_formats=["%Y-%m-%d %H:%M:%S"],
        required=False,
    )

    class Meta:
        model = ShipMovement
        fields = [
            "ship",
            "harbour",
            "entered_at",
            "exited_at",
        ]

    def create(self, validated_data):
        """
        Create a new ship movement.
        """
        # TODO: NS - 30052024: Refactor this method to use the service
        # handle nested ship data
        ship_data = validated_data.pop("ship")
        ship = create_ship(ship_data, try_get=True)

        # handle nested harbour data
        harbour_data = validated_data.pop("harbour")
        location_data = harbour_data.pop("location")
        try:
            location, _ = Location.objects.get_or_create(**location_data)
        except Location.MultipleObjectsReturned:
            location = Location.objects.create(**location_data)

        try:
            harbour, _ = Harbour.objects.get_or_create(**harbour_data, location=location)
        except Harbour.MultipleObjectsReturned:
            harbour = Harbour.objects.create(**harbour_data, location=location)

        return ShipMovement.objects.create(ship=ship, harbour=harbour, **validated_data)

    def update(self, instance, validated_data):
        """
        Update an existing ship movement.
        """
        # TODO: NS - 30052024: Refactor this method to use the service
        if "ship" in validated_data:
            ship_data = validated_data.pop("ship")
            ship = create_ship(ship_data, try_get=True)

        if "harbour" in validated_data:
            harbour_data = validated_data.pop("harbour")
            location_data = harbour_data.pop("location")
            try:
                location, _ = Location.objects.get_or_create(**location_data)
            except Location.MultipleObjectsReturned:
                location = Location.objects.create(**location_data)

            try:
                harbour, _ = Harbour.objects.get_or_create(**harbour_data, location=location)
            except Harbour.MultipleObjectsReturned:
                harbour = Harbour.objects.create(**harbour_data, location=location)

            instance.ship = ship
            instance.harbour = harbour
            instance.save()
        return super().update(instance, validated_data)
