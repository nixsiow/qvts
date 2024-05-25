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
