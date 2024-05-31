from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from qvts.ships.models import ContactPerson
from qvts.ships.models import OperatingCompany
from qvts.ships.models import Ship
from qvts.ships.models import ShipMovement

####################################################################################################
# ContactPerson
####################################################################################################


class ContactPersonOperatingCompanyInline(admin.TabularInline):
    model = OperatingCompany
    readonly_fields = ("name",)
    show_change_link = True
    can_delete = False
    fields = ("name",)

    def has_add_permission(self, request, obj):
        return False


@admin.register(ContactPerson)
class ContactPersonAdmin(admin.ModelAdmin):
    # autocomplete_fields = ["contact_person"]
    inlines = (ContactPersonOperatingCompanyInline,)
    search_fields = ("name", "email", "operating_company__name")
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
        "get_operating_companies",
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
        description="operating companies",
    )
    def get_operating_companies(self, obj):
        """
        Return a comma-separated list of operating companies associated with the contact person.
        """
        return ",".join([oc.name for oc in obj.operating_companies.all()])


####################################################################################################
# OperatingCompany
####################################################################################################


class OperatingCompanyShipInline(admin.TabularInline):
    model = Ship
    readonly_fields = ("name",)
    show_change_link = True
    can_delete = False
    fields = (
        "name",
        "flag",
    )

    def has_add_permission(self, request, obj):
        return False


@admin.register(OperatingCompany)
class OperatingCompanyAdmin(admin.ModelAdmin):
    # autocomplete_fields = ["contact_person"]
    inlines = (OperatingCompanyShipInline,)
    search_fields = ("name", "ship__name")
    readonly_fields = (
        "id",
        "uuid",
        "created_at",
        "updated_at",
    )
    list_display = (
        "id",
        "name",
        "get_ships_count",
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
                    "contact_person",
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

    # get a count of all the ships associated with the operating company
    @admin.display(
        description="ships count",
    )
    def get_ships_count(self, obj):
        return obj.ships.count()


####################################################################################################
# Ship
####################################################################################################


class ShipShipMovementInline(admin.TabularInline):
    model = ShipMovement
    show_change_link = True
    can_delete = False
    fields = (
        "harbour",
        "entered_at",
        "exited_at",
    )
    ordering = ("exited_at",)
    readonly_fields = (
        "harbour",
        "entered_at",
    )

    def has_add_permission(self, request, obj):
        return False


@admin.register(Ship)
class ShipAdmin(admin.ModelAdmin):
    # autocomplete_fields = ["operating_company"]
    inlines = (ShipShipMovementInline,)
    search_fields = ("name", "type", "operating_company__name")
    readonly_fields = (
        "id",
        "uuid",
        "created_at",
        "updated_at",
    )
    list_display = (
        "id",
        "name",
        "tonnage",
        "draft_max_load",
        "draft_dry",
        "type",
        "beam",
        "length",
        "flag",
        "year_built",
        "get_age",
    )
    list_display_links = (
        "id",
        "name",
    )
    # ordering = ("transaction_date",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "flag",
                    "operating_company",
                ),
                "classes": ["wide", "extrapretty"],
            },
        ),
        (
            _("Properties"),
            {
                "fields": (
                    "tonnage",
                    "draft_max_load",
                    "draft_dry",
                    "type",
                    "beam",
                    "length",
                    "year_built",
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
# ShipMovement
####################################################################################################


@admin.register(ShipMovement)
class ShipMovementAdmin(admin.ModelAdmin):
    search_fields = ("ship__name", "harbour__name")
    readonly_fields = (
        "id",
        "uuid",
        "created_at",
        "updated_at",
    )
    list_display = (
        "id",
        "ship",
        "harbour",
        "entered_at",
        "exited_at",
    )
    list_display_links = ("id",)
    ordering = ("-exited_at",)
    fieldsets = (
        (
            _("Ship"),
            {
                "fields": ("ship",),
                "classes": ["wide", "extrapretty"],
            },
        ),
        (
            _("Harbour"),
            {
                "fields": ("harbour",),
                "classes": ["wide", "extrapretty"],
            },
        ),
        (
            _("Timestamps"),
            {
                "fields": (
                    "entered_at",
                    "exited_at",
                ),
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
