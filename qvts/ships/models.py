from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from qvts.core.models import BaseModel
from qvts.ships.managers import ShipManager

####################################################################################################
# ContactPerson
####################################################################################################


class ContactPerson(BaseModel):
    """
    Model to store contact persons for operating companies.
    """

    # Fields
    # -----------------------------------------------------------
    name = models.CharField(
        _("name"),
        max_length=100,
        help_text=_("Name of the contact person"),
    )
    phone = models.CharField(
        _("phone"),
        max_length=20,
        help_text=_("Phone number of the contact person"),
    )
    email = models.EmailField(
        _("email"),
        max_length=255,
        help_text=_("Email address of the contact person"),
    )

    class Meta:
        verbose_name = _("contact person")
        verbose_name_plural = _("contact persons")

    # Methods
    # -----------------------------------------------------------

    def __str__(self):
        return self.name


####################################################################################################
# OperatingCompany
####################################################################################################


class OperatingCompany(BaseModel):
    """
    Model to store operating companies.
    """

    # Fields
    # -----------------------------------------------------------

    name = models.CharField(
        _("name"),
        max_length=100,
        help_text=_("Name of the operating company"),
    )
    contact_person = models.ForeignKey(
        "ships.ContactPerson",
        verbose_name=_("contact person"),
        on_delete=models.CASCADE,
        related_name="operating_companies",
        related_query_name="operating_company",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _("operating company")
        verbose_name_plural = _("operating companies")

    # Methods
    # -----------------------------------------------------------

    def __str__(self):
        return self.name


####################################################################################################
# Ship
####################################################################################################


class Ship(BaseModel):
    """
    Model to store ships.
    """

    class Type(models.TextChoices):
        BULK_CARRIER = "bulk_carrier", _("Bulk carrier")
        FISHING = "fishing", _("Fishing")
        SUBMARINE = "submarine", _("Submarine")
        TANKER = "tanker", _("Tanker")
        CRUISE_SHIP = "cruise_ship", _("Cruise ship")

    # Fields
    # -----------------------------------------------------------

    name = models.CharField(
        _("name"),
        max_length=100,
        help_text=_("Name of the ship"),
    )
    tonnage = models.PositiveIntegerField(
        _("tonnage"),
        help_text=_("in metric tons"),
    )
    draft_max_load = models.FloatField(
        _("draft under maximum load"),
        help_text=_("Draft under maximum load in meters"),
    )
    draft_dry = models.FloatField(
        _("draft dry"),
        help_text=_("Draft without load in meters"),
    )
    type = models.CharField(
        _("type"),
        max_length=50,
        choices=Type.choices,
        help_text=_("Type of the ship"),
    )
    beam = models.FloatField(
        _("beam"),
        help_text=_("Beam in meters"),
    )
    length = models.FloatField(
        _("length"),
        help_text=_("Length in meters"),
    )
    flag = models.CharField(
        _("flag"),
        max_length=100,
        help_text=_("String representation of the flag"),
    )
    year_built = models.PositiveSmallIntegerField(
        _("year built"),
        help_text=_("Year the ship was built"),
        validators=[MinValueValidator(1900), MaxValueValidator(2100)],
    )

    operating_company = models.ForeignKey(
        "ships.OperatingCompany",
        verbose_name=_("operating company"),
        on_delete=models.CASCADE,
        related_name="ships",
        related_query_name="ship",
        help_text=_("Operating company of the ship"),
        null=True,
        blank=True,
    )

    objects = ShipManager()

    class Meta:
        verbose_name = _("ship")
        verbose_name_plural = _("ships")

    # Methods
    # -----------------------------------------------------------

    def __str__(self):
        return self.name

    def get_age(self):
        """
        Calculate the age of the ship in years.
        """
        from django.utils import timezone

        current_year = timezone.now().year
        return current_year - self.year_built

    def get_visited_harbours(self):
        # return self.ship_movements.values_list("harbour__name", "entered_at")
        return self.ship_movements.values_list("harbour__name", flat=True)


####################################################################################################
# ShipMovement
####################################################################################################


class ShipMovement(BaseModel):
    """
    Model to store ship movements.
    """

    # Fields
    # -----------------------------------------------------------
    entered_at = models.DateTimeField(
        _("entered at"),
        help_text=_("Date and time the ship entered the harbour"),
    )
    exited_at = models.DateTimeField(
        _("exited at"),
        null=True,
        blank=True,
        help_text=_("Date and time the ship exited the harbour"),
    )

    ship = models.ForeignKey(
        "ships.Ship",
        verbose_name=_("ship"),
        on_delete=models.CASCADE,
        related_name="ship_movements",
        related_query_name="ship_movement",
        help_text=_("Ship that moved"),
    )
    harbour = models.ForeignKey(
        "harbours.Harbour",
        on_delete=models.CASCADE,
        related_name="ship_movements",
        related_query_name="ship_movement",
        help_text=_("Harbour the ship moved to"),
    )

    class Meta:
        verbose_name = _("ship movement")
        verbose_name_plural = _("ship movements")

    # Methods
    # -----------------------------------------------------------

    def __str__(self):
        return (
            f"{self.ship.name} @ {self.harbour.name} [{self.entered_at.strftime('%Y-%m-%d %H:%M:%S')} "
            f"- {self.exited_at.strftime('%Y-%m-%d %H:%M:%S') if self.exited_at else 'now'}]"
        )
