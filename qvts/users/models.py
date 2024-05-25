from typing import ClassVar

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from qvts.core.models import BaseModel

from .managers import UserManager


class User(BaseModel, AbstractUser):
    """
    Default custom user model for Queensland Vessel Traffic Service.
    """

    # Fields
    # -----------------------------------------------------------

    username = None  # type: ignore[assignment]
    email = models.EmailField(
        _("email address"),
        unique=True,
        max_length=255,
        help_text=_("Email address of user"),
    )
    role = models.CharField(
        _("role"),
        max_length=100,
        blank=True,
        help_text=_("Role of user"),
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects: ClassVar[UserManager] = UserManager()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    # Methods
    # -----------------------------------------------------------

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"pk": self.id})
