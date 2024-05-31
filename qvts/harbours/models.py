from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from qvts.core.models import BaseModel
from qvts.harbours.managers import HarbourManager


class Location(BaseModel):
    """
    Model to store locations.
    """

    # Fields
    # -----------------------------------------------------------

    city = models.CharField(
        _("city"),
        max_length=100,
        help_text=_("City name"),
    )
    country = models.CharField(
        _("country"),
        max_length=100,
        help_text=_("Country name"),
    )

    class Meta:
        verbose_name = _("location")
        verbose_name_plural = _("locations")

    # Methods
    # -----------------------------------------------------------

    def __str__(self):
        return f"{self.city}, {self.country}"


class Harbour(BaseModel):
    """
    Model to store harbours.
    """

    # Fields
    # -----------------------------------------------------------
    name = models.CharField(
        _("name"),
        max_length=100,
        help_text=_("Harbour name"),
    )
    berth_depth_max = models.FloatField(
        _("maximum berth depth"),
        validators=[MinValueValidator(0.0)],
        help_text=_("Maximum berth depth in meters"),
    )
    harbour_master = models.CharField(
        _("harbour master"),
        max_length=100,
        help_text=_("Name of the harbour master"),
    )
    location = models.ForeignKey(
        "harbours.Location",
        verbose_name=_("location"),
        on_delete=models.CASCADE,
        related_name="harbours",
        help_text=_("Location of the harbour"),
    )
    vts_centre = models.ForeignKey(
        "vts.VTSCentre",
        verbose_name=_("VTS Centre"),
        on_delete=models.SET_NULL,
        related_name="harbours",
        related_query_name="harbour",
        help_text=_("VTS Centre that is managing the harbour"),
        null=True,
        blank=True,
    )

    objects = HarbourManager()

    class Meta:
        verbose_name = _("harbour")
        verbose_name_plural = _("harbours")

    # Methods
    # -----------------------------------------------------------

    def __str__(self):
        return self.name
