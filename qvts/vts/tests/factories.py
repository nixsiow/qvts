import factory
from factory.django import DjangoModelFactory
from faker import Faker

from qvts.users.tests.factories import UserFactory
from qvts.vts.models import Operator
from qvts.vts.models import VTSCentre

# initialise the faker with en_AU locale
fake = Faker("en_AU")


class VTSCentreFactory(DjangoModelFactory):
    class Meta:
        model = VTSCentre

    name = fake.company()
    phone = fake.phone_number()
    email = fake.email()


class OperatorFactory(DjangoModelFactory):
    class Meta:
        model = Operator

    role = fake.job()
    vts_centre = factory.SubFactory(VTSCentreFactory)
    user = factory.SubFactory(UserFactory)
