from allauth.account.decorators import secure_admin_login
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.utils.translation import gettext_lazy as _

from qvts.vts.models import Operator

from .forms import UserAdminChangeForm
from .forms import UserAdminCreationForm
from .models import User

if settings.DJANGO_ADMIN_FORCE_ALLAUTH:
    # Force the `admin` sign in process to go through the `django-allauth` workflow:
    # https://docs.allauth.org/en/latest/common/admin.html#admin
    admin.autodiscover()
    admin.site.login = secure_admin_login(admin.site.login)  # type: ignore[method-assign]


class UserOperatorInline(admin.TabularInline):
    model = Operator
    readonly_fields = ("role", "vts_centre")
    show_change_link = True
    can_delete = False
    fields = ("role", "vts_centre")

    def has_add_permission(self, request, obj):
        return False


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    inlines = (UserOperatorInline,)
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    readonly_fields = (
        "created_at",
        "updated_at",
        "uuid",
        "last_login",
    )
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            _("Personal info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                ),
                "classes": ["wide", "extrapretty"],
            },
        ),
        (
            _("Metadata"),
            {
                "fields": (
                    "uuid",
                    "last_login",
                    "created_at",
                    "updated_at",
                ),
                "classes": ["wide", "extrapretty"],
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
                "classes": ["wide", "extrapretty"],
            },
        ),
    )
    list_display = ["id", "email", "first_name", "last_name", "is_superuser", "operator"]
    list_display_links = ["id", "email"]
    search_fields = ["first_name", "last_name"]
    ordering = ["id"]
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
