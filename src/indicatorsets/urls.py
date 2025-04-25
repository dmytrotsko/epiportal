from django.urls import path
from django.urls.resolvers import URLPattern

from indicatorsets.views import IndicatorSetListView, epivis


urlpatterns: list[URLPattern] = [
    path("", IndicatorSetListView.as_view(), name="indicatorsets"),
    path("epivis/", epivis, name="epivis")
]
