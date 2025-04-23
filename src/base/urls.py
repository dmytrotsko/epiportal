from django.urls import path, re_path
from django.urls.resolvers import URLPattern

from base.views import epidata, get_epiweek

urlpatterns: list[URLPattern] = [
    re_path(r"^epidata/(?P<endpoint>.*)/$", epidata, name="epidata"),
    path("get_epiweek/", get_epiweek, name="get_epiweek"),
]
