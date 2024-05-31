import factory
from factory.django import DjangoModelFactory
from faker import Faker

from qvts.harbours.models import Harbour
from qvts.harbours.models import Location
from qvts.vts.tests.factories import VTSCentreFactory

# initialise the faker with en_AU locale
fake = Faker("en_AU")


class LocationFactory(DjangoModelFactory):
    class Meta:
        model = Location

    city = fake.city()
    country = fake.country()


class HarbourFactory(DjangoModelFactory):
    class Meta:
        model = Harbour

    name = fake.word()
    berth_depth_max = factory.Faker(
        "random_int",
        min=5,
        max=20,
    )
    harbour_master = fake.name()
    location = factory.SubFactory(LocationFactory)
    vts_centre = factory.SubFactory(VTSCentreFactory)
