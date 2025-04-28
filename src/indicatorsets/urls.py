from django.urls import path
from django.urls.resolvers import URLPattern

from indicatorsets.views import (IndicatorSetListView, epivis,
                                 generate_export_data_url, preview_data)

urlpatterns: list[URLPattern] = [
    path("", IndicatorSetListView.as_view(), name="indicatorsets"),
    path("epivis/", epivis, name="epivis"),
    path("export/", generate_export_data_url, name="export"),
    path("preview_data/", preview_data, name="preview_data")
]
