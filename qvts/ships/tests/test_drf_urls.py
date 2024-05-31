from django.urls import resolve
from django.urls import reverse

from qvts.ships.models import Ship


def test_ship_detail(ship: Ship):
    assert reverse("api:ship-detail", kwargs={"pk": ship.pk}) == f"/api/ships/{ship.pk}/"
    assert resolve(f"/api/ships/{ship.pk}/").view_name == "api:ship-detail"


def test_ship_list():
    assert reverse("api:ship-list") == "/api/ships/"
    assert resolve("/api/ships/").view_name == "api:ship-list"
