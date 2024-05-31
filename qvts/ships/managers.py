from django.apps import apps
from django.db import models


class ShipManager(models.Manager):
    """
    Custom manager for the Ship model.
    """

    def get_ships_in_harbour(self, harbour):
        """
        Custom manager for the Ship model to return a list of ships currently
        in a given harbour. Ships are considered to be in a harbour if they have
        entered the harbour but not yet exited it.
        """
        return self.get_queryset().filter(
            pk__in=list(
                apps.get_model("ships", "ShipMovement")
                .objects.filter(harbour=harbour, exited_at=None)
                .values_list("ship_id", flat=True),
            ),
        )
