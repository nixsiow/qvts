from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from qvts.core.models import BaseModel


class VTSCentre(BaseModel):
    """
    Model to store VTS Centres.
    """

    # Fields
    # -----------------------------------------------------------
    name = models.CharField(
        _("name"),
        max_length=100,
        help_text=_("Name of the VTS Centre"),
    )
    phone = models.CharField(
        _("phone"),
        max_length=20,
        help_text=_("Phone number of the VTS Centre"),
        blank=True,
    )
    email = models.EmailField(
        _("email"),
        max_length=255,
        help_text=_("Email address of the VTS Centre"),
        blank=True,
    )

    class Meta:
        verbose_name = _("VTS Centre")
        verbose_name_plural = _("VTS Centres")

    # Methods
    # -----------------------------------------------------------

    def __str__(self):
        return self.name


class Operator(BaseModel):
    """
    Model to store operators.
    """

    # Fields
    # -----------------------------------------------------------

    role = models.CharField(
        _("role"),
        max_length=100,
        help_text=_("Role of the operator"),
        blank=True,
    )
    vts_centre = models.ForeignKey(
        "vts.VTSCentre",
        verbose_name=_("VTS Centre"),
        on_delete=models.CASCADE,
        related_name="operators",
        related_query_name="operator",
        help_text=_("VTS Centre the operator is assigned to"),
    )
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        verbose_name=_("user"),
        on_delete=models.CASCADE,
        help_text=_("User account of the operator"),
    )

    class Meta:
        verbose_name = _("operator")
        verbose_name_plural = _("operators")

    # Methods
    # -----------------------------------------------------------

    def __str__(self):
        return f"{self.user} ({self.role})"
