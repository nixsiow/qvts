from django.db import models


class HarbourManager(models.Manager):
    """
    Custom manager for the Harbour model.
    """

    def get_visited_harbours_by(self, ship):
        """
        Custom manager for the Harbour model to return a list of harbours
        visited by a given ship. A ship is considered to have visited a harbour
        if it has entered the harbour regardless of whether it has exited it.
        """
        return self.get_queryset().filter(
            pk__in=list(
                ship.ship_movements.values_list("harbour_id", flat=True),
            ),
        )
