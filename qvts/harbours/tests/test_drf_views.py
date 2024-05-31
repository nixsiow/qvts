import pytest
from rest_framework.test import APIRequestFactory

from qvts.harbours.api.views import HarbourViewSet
from qvts.harbours.models import Harbour


class TestHarbourViewSet:
    @pytest.fixture()
    def api_rf(self) -> APIRequestFactory:
        return APIRequestFactory()

    def test_get_queryset(self, harbour: Harbour, api_rf: APIRequestFactory):
        view = HarbourViewSet()
        request = api_rf.get("/fake-url/")
        request.harbour = harbour

        view.request = request

        assert harbour in view.get_queryset()
