import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    """
    Base model for all models in the application.
    """

    # Fields
    # -----------------------------------------------------------

    created_at = models.DateTimeField(auto_now_add=True, help_text=_("Datetime when the record was created"))
    updated_at = models.DateTimeField(auto_now=True, help_text=_("Datetime when the record was last updated"))
    uuid = models.UUIDField(
        _("UUID"),
        default=uuid.uuid4,
        editable=False,
        help_text=_("Public unique identifier for the record"),
    )

    class Meta:
        abstract = True

    # Methods
    # -----------------------------------------------------------

    def get_uuid(self) -> str:
        """
        Get UUID of object.

        Returns:
            str: UUID of object.
        """
        return self.uuid
