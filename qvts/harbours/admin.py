from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from qvts.harbours.models import Harbour
from qvts.harbours.models import Location
from qvts.ships.models import ShipMovement

####################################################################################################
# Ship
####################################################################################################


class HarbourShipMovementInline(admin.TabularInline):
    model = ShipMovement
    show_change_link = True
    can_delete = False
    fields = (
        "ship",
        "entered_at",
        "exited_at",
    )

    def has_add_permission(self, request, obj):
        return False


@admin.register(Harbour)
class HarbourAdmin(admin.ModelAdmin):
    # autocomplete_fields = ["operating_company"]
    inlines = (HarbourShipMovementInline,)
    search_fields = ("name", "type", "location__city", "location__country")
    readonly_fields = (
        "id",
        "uuid",
        "created_at",
        "updated_at",
    )
    list_display = (
        "id",
        "name",
        "berth_depth_max",
        "harbour_master",
        "location",
        "vts_centre",
    )
    list_display_links = (
        "id",
        "name",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "harbour_master",
                    "location",
                    "vts_centre",
                ),
                "classes": ["wide", "extrapretty"],
            },
        ),
        (
            _("Properties"),
            {
                "fields": ("berth_depth_max",),
                "classes": ["wide", "extrapretty"],
            },
        ),
        (
            _("Metadata"),
            {
                "fields": (
                    "uuid",
                    "created_at",
                    "updated_at",
                ),
                "classes": ["wide", "extrapretty"],
            },
        ),
    )


####################################################################################################
# Location
####################################################################################################


class LocationHarbourInline(admin.TabularInline):
    model = Harbour
    show_change_link = True
    can_delete = False
    fields = (
        "name",
        "harbour_master",
    )

    def has_add_permission(self, request, obj):
        return False


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    # autocomplete_fields = ["operating_company"]
    inlines = (LocationHarbourInline,)
    search_fields = ("city", "country")
    readonly_fields = (
        "id",
        "uuid",
        "created_at",
        "updated_at",
    )
    list_display = (
        "id",
        "city",
        "country",
    )
    list_display_links = (
        "id",
        "city",
        "country",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "city",
                    "country",
                ),
                "classes": ["wide", "extrapretty"],
            },
        ),
        (
            _("Metadata"),
            {
                "fields": (
                    "uuid",
                    "created_at",
                    "updated_at",
                ),
                "classes": ["wide", "extrapretty"],
            },
        ),
    )
