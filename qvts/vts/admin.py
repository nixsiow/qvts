from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from qvts.harbours.models import Harbour
from qvts.vts.models import Operator
from qvts.vts.models import VTSCentre

####################################################################################################
# Operator
####################################################################################################


@admin.register(Operator)
class OperatorAdmin(admin.ModelAdmin):
    search_fields = ("user__email", "vts_centre__name")
    readonly_fields = (
        "id",
        "uuid",
        "created_at",
        "updated_at",
    )
    list_display = (
        "id",
        "user",
        "role",
        "vts_centre",
    )
    list_display_links = (
        "id",
        "user",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "user",
                    "vts_centre",
                    "role",
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


####################################################################################################
# VTSCentre
####################################################################################################


class VTSCentreHarbourInline(admin.TabularInline):
    model = Harbour
    readonly_fields = (
        "name",
        "berth_depth_max",
        "location",
    )
    show_change_link = True
    can_delete = False
    fields = (
        "name",
        "berth_depth_max",
        "harbour_master",
        "location",
    )

    def has_add_permission(self, request, obj):
        return False


class VTSCentreOperatorInline(admin.TabularInline):
    model = Operator
    readonly_fields = ("user",)
    show_change_link = True
    can_delete = False
    fields = ("user", "role")

    def has_add_permission(self, request, obj):
        return False


@admin.register(VTSCentre)
class VTSCentreAdmin(admin.ModelAdmin):
    inlines = (
        VTSCentreHarbourInline,
        VTSCentreOperatorInline,
    )
    search_fields = ("name", "phone", "email")
    readonly_fields = (
        "id",
        "uuid",
        "created_at",
        "updated_at",
    )
    list_display = (
        "id",
        "name",
        "phone",
        "email",
        "get_operators_count",
        "get_harbours_count",
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
                    "phone",
                    "email",
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

    @admin.display(
        description=_("Harbours count"),
    )
    def get_harbours_count(self, obj):
        return obj.harbours.count()

    @admin.display(
        description=_("Operators count"),
    )
    def get_operators_count(self, obj):
        return obj.operators.count()
