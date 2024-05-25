from django.urls import path

from .views import index_view

app_name = "core"
urlpatterns = [
    ####################################################################################################
    # Index
    ####################################################################################################
    path("", index_view, name="index"),
]
