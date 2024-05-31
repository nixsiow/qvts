from django.core.exceptions import MultipleObjectsReturned

from qvts.ships.models import ContactPerson
from qvts.ships.models import OperatingCompany
from qvts.ships.models import Ship


def create_ship(validated_data, try_get=False) -> Ship:  # noqa: FBT002
    """
    Service to create a new ship from validated serializer data.
    Create the nested operating company and contact person if they do not exist.
    """
    operating_company_data = validated_data.pop("operating_company")
    contact_person_data = operating_company_data.pop("contact_person")
    contact_person, _ = ContactPerson.objects.get_or_create(**contact_person_data)
    operating_company, _ = OperatingCompany.objects.get_or_create(
        contact_person=contact_person,
        **operating_company_data,
    )
    if try_get:
        try:
            return Ship.objects.get_or_create(operating_company=operating_company, **validated_data)
        except MultipleObjectsReturned:
            return Ship.objects.create(operating_company=operating_company, **validated_data)
    return Ship.objects.create(operating_company=operating_company, **validated_data)


def update_ship(instance, validated_data) -> Ship:
    """
    Service to update an existing ship with validated serializer data.
    Update the nested operating company and contact person if they exist.
    """
    contact_person = instance.operating_company.contact_person

    if "operating_company" in validated_data:
        # if changes to the operating company data
        operating_company_data = validated_data.pop("operating_company")
        if "contact_person" in operating_company_data:
            # changes to the contact person data
            contact_person_data = operating_company_data.pop("contact_person")
            contact_person, _ = ContactPerson.objects.get_or_create(**contact_person_data)

        operating_company, _ = OperatingCompany.objects.get_or_create(
            contact_person=contact_person,
            **operating_company_data,
        )

        instance.operating_company = operating_company
        # instance.save()
    return instance, validated_data
