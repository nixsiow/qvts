# ruff: noqa

from django.contrib import admin
from django.contrib.admin.models import DELETION
from django.contrib.admin.models import LogEntry
from django.urls import NoReverseMatch
from django.urls import reverse
from django.utils.html import escape
from django.utils.safestring import mark_safe

#########################################################################################
# Log Entry
#########################################################################################


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    """
    LogEntry records all changes made to the models in the admin interface.
    Only superuser can view the log entries.
    """

    list_filter = ("user", "content_type", "action_flag")
    search_fields = ("object_repr", "change_message")
    list_display = (
        "action_time",
        "user",
        "content_type",
        "object_link",
        "action_flag",
    )
    date_hierarchy = "action_time"

    # Managing Permissions:
    # - Only superuser can view the log entries
    # - set all other permissions to False
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser

    # to add the edited object's link
    @admin.display(
        description="object",
        ordering="object_repr",
    )
    def object_link(self, obj):
        if obj.action_flag == DELETION:
            link = escape(obj.object_repr)
        else:
            ct = obj.content_type

            change_link = reverse(f"admin:{ct.app_label}_{ct.model}_change", args=[obj.object_id])
            change_link_text = escape(obj.object_repr)

            try:
                link = f'<a href="{change_link}">{change_link_text}</a>'  # type: ignore[assignment]

            except NoReverseMatch:
                return None
        return mark_safe(link)
