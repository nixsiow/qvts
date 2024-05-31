import re
from http import HTTPStatus

from django.http import JsonResponse
from django.utils.translation import gettext_lazy as _
from django.views.defaults import page_not_found as django_handler404
from django.views.generic import TemplateView

####################################################################################################
# Index
####################################################################################################


class IndexView(TemplateView):
    """
    Index view to render the index page for authenticated users.
    """

    template_name = "pages/index.html"


index_view = IndexView.as_view()


####################################################################################################
# Error handlers
####################################################################################################


def handler404(request, exception=None):
    """
    Custom 404 handler to return JSON response for API URLs
    and HTML for browser requested URLs.
    """
    # browser requested HTML
    requested_html = re.search(
        r"^text/html",
        request.headers.get("accept"),
    )

    # API requested URL (assumption: starts with /api)
    api = re.search(
        r"^/api",
        request.get_full_path(),
    )

    # default to Django's 404 handler for browser requested URLs
    if requested_html and not api:
        return django_handler404(request, exception)

    return JsonResponse(
        {
            "detail": _("Requested API URL not found"),
        },
        status=HTTPStatus.NOT_FOUND,
        safe=False,
    )
