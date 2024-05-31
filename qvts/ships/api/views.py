from rest_framework.mixins import CreateModelMixin
from rest_framework.mixins import ListModelMixin
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.mixins import UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from qvts.ships.models import Ship
from qvts.ships.models import ShipMovement

from .serializers import ShipListSerializer
from .serializers import ShipMovementDetailSerializer
from .serializers import ShipMovementListSerializer
from .serializers import ShipMovementSerializer
from .serializers import ShipSerializer


class ShipViewSet(CreateModelMixin, RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = ShipSerializer
    list_serializer_class = ShipListSerializer
    queryset = Ship.objects.all()
    lookup_field = "pk"

    def get_serializer_class(self):
        if self.action == "list":
            if hasattr(self, "list_serializer_class"):
                return self.list_serializer_class

        return super().get_serializer_class()


class ShipMovementViewSet(CreateModelMixin, RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = ShipMovementSerializer
    list_serializer_class = ShipMovementListSerializer
    retrieve_serializer_class = ShipMovementDetailSerializer
    queryset = ShipMovement.objects.all()
    lookup_field = "pk"

    def get_serializer_class(self):
        if self.action == "list":
            if hasattr(self, "list_serializer_class"):
                return self.list_serializer_class
        elif self.action == "retrieve":
            if hasattr(self, "retrieve_serializer_class"):
                return self.retrieve_serializer_class

        return super().get_serializer_class()
