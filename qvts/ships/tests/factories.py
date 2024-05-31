import random

import factory
from django.utils import timezone
from factory.django import DjangoModelFactory
from faker import Faker

from qvts.ships.models import ContactPerson
from qvts.ships.models import OperatingCompany
from qvts.ships.models import Ship
from qvts.ships.models import ShipMovement

# initialise the faker with en_AU locale
fake = Faker("en_AU")


class ContactPersonFactory(DjangoModelFactory):
    class Meta:
        model = ContactPerson

    name = fake.name()
    phone = fake.phone_number()
    email = fake.email()


class OperatingCompanyFactory(DjangoModelFactory):
    class Meta:
        model = OperatingCompany

    name = fake.company()
    contact_person = factory.SubFactory(ContactPersonFactory)


class ShipFactory(DjangoModelFactory):
    class Meta:
        model = Ship

    name = fake.word()
    tonnage = fake.random_int(min=1000, max=200000)
    draft_max_load = factory.Faker(
        "random_int",
        min=5,
        max=20,
    )
    draft_dry = fake.random_int(min=2, max=10)
    type = fake.random_element(elements=[choice[0] for choice in Ship.Type.choices])
    beam = fake.random_int(min=10, max=50)
    length = fake.random_int(min=50, max=400)
    flag = fake.random_element(elements=["PL", "AA", "AZ"])
    year_built = fake.random_int(min=1900, max=2100)
    operating_company = factory.SubFactory(OperatingCompanyFactory)


class ShipMovementFactory(DjangoModelFactory):
    class Meta:
        model = ShipMovement

    entered_at = fake.date_time_this_decade(before_now=True, after_now=False, tzinfo=timezone.utc)
    exited_at = factory.Maybe(
        "exited",
        yes_declaration=fake.date_time_this_decade(before_now=False, after_now=True, tzinfo=timezone.utc),
        no_declaration=None,
    )
    ship = factory.SubFactory(ShipFactory)
    harbour = factory.SubFactory("qvts.harbours.factories.HarbourFactory")

    @factory.lazy_attribute
    def exited(self):
        return random.choice([True, False])  # noqa: S311
