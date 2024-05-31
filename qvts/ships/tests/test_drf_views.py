import pytest
from rest_framework.test import APIRequestFactory

from qvts.ships.api.views import ShipViewSet
from qvts.ships.models import Ship


class TestShipViewSet:
    @pytest.fixture()
    def api_rf(self) -> APIRequestFactory:
        return APIRequestFactory()

    def test_get_queryset(self, ship: Ship, api_rf: APIRequestFactory):
        view = ShipViewSet()
        request = api_rf.get("/fake-url/")
        request.ship = ship

        view.request = request

        assert ship in view.get_queryset()
