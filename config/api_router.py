from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from qvts.harbours.api.views import HarbourViewSet
from qvts.ships.api.views import ShipMovementViewSet
from qvts.ships.api.views import ShipViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

# router.register("users", UserViewSet)
router.register("ships", ShipViewSet)
router.register("ship_movements", ShipMovementViewSet)
router.register("harbours", HarbourViewSet)


app_name = "api"
urlpatterns = router.urls
