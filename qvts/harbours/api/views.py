from rest_framework.mixins import CreateModelMixin
from rest_framework.mixins import ListModelMixin
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.mixins import UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from qvts.harbours.models import Harbour

from .serializers import HarbourListSerializer
from .serializers import HarbourSerializer


class HarbourViewSet(CreateModelMixin, RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = HarbourSerializer
    list_serializer_class = HarbourListSerializer
    queryset = Harbour.objects.all()
    lookup_field = "pk"

    def get_serializer_class(self):
        if self.action == "list":
            if hasattr(self, "list_serializer_class"):
                return self.list_serializer_class

        return super().get_serializer_class()
