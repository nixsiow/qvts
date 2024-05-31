import pytest

from qvts.harbours.models import Harbour
from qvts.harbours.models import Location
from qvts.harbours.tests.factories import HarbourFactory
from qvts.harbours.tests.factories import LocationFactory
from qvts.ships.models import ContactPerson
from qvts.ships.models import OperatingCompany
from qvts.ships.models import Ship
from qvts.ships.models import ShipMovement
from qvts.ships.tests.factories import ContactPersonFactory
from qvts.ships.tests.factories import OperatingCompanyFactory
from qvts.ships.tests.factories import ShipFactory
from qvts.ships.tests.factories import ShipMovementFactory
from qvts.users.models import User
from qvts.users.tests.factories import UserFactory
from qvts.vts.models import Operator
from qvts.vts.models import VTSCentre
from qvts.vts.tests.factories import OperatorFactory
from qvts.vts.tests.factories import VTSCentreFactory


@pytest.fixture(autouse=True)
def _media_storage(settings, tmpdir) -> None:
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture()
def user(db) -> User:
    return UserFactory()


@pytest.fixture()
def contact_person(db) -> ContactPerson:
    return ContactPersonFactory()


@pytest.fixture()
def operating_company(db, contact_person) -> OperatingCompany:
    return OperatingCompanyFactory(contact_person=contact_person)


@pytest.fixture()
def ship(db, operating_company) -> Ship:
    return ShipFactory(operating_company=operating_company)


@pytest.fixture()
def ship_movement(db, ship, harbour) -> ShipMovement:
    return ShipMovementFactory(ship=ship, harbour=harbour)


@pytest.fixture()
def location(db) -> Location:
    return LocationFactory()


@pytest.fixture()
def harbour(db, location, vts_centre) -> Harbour:
    return HarbourFactory(location=location, vts_centre=vts_centre)


@pytest.fixture()
def vts_centre(db) -> VTSCentre:
    return VTSCentreFactory()


@pytest.fixture()
def operator(db, user, vts_centre) -> Operator:
    return OperatorFactory(user=user, vts_centre=vts_centre)
