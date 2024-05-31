from django.urls import resolve
from django.urls import reverse

from qvts.harbours.models import Harbour


def test_harbour_detail(harbour: Harbour):
    assert reverse("api:harbour-detail", kwargs={"pk": harbour.pk}) == f"/api/harbours/{harbour.pk}/"
    assert resolve(f"/api/harbours/{harbour.pk}/").view_name == "api:harbour-detail"


def test_harbour_list():
    assert reverse("api:harbour-list") == "/api/harbours/"
    assert resolve("/api/harbours/").view_name == "api:harbour-list"
