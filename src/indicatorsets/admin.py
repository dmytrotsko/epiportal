from django.contrib import admin

from import_export.admin import ImportExportModelAdmin
from indicatorsets.models import IndicatorSet, NonDelphiIndicatorSet
from indicatorsets.resources import IndicatorSetResource, NonDelphiIndicatorSetResource


# Register your models here.
@admin.register(IndicatorSet)
class IndicatorSetAdmin(ImportExportModelAdmin):
    """
    Admin interface for the IndicatorSet model.
    """

    resource_class = IndicatorSetResource
    list_display = (
        "name",
        "short_name",
        "description",
        "maintainer_name",
        "maintainer_email",
        "organization",
        "origin_datasource",
        "language",
        "version_number",
        "original_data_provider",
        "origin_datasource",
    )
    search_fields = ("name", "short_name", "description")
    ordering = ["name"]
    list_filter = ["original_data_provider"]


@admin.register(NonDelphiIndicatorSet)
class NonDelphiIndicatorSetAdmin(ImportExportModelAdmin):
    """
    Admin interface for the IndicatorSet model.
    """

    resource_class = NonDelphiIndicatorSetResource
    list_display = (
        "name",
        "short_name",
        "description",
        "maintainer_name",
        "maintainer_email",
        "organization",
        "origin_datasource",
        "language",
        "version_number",
        "original_data_provider",
        "origin_datasource",
        "source_type",
    )
    search_fields = ("name", "short_name", "description")
    ordering = ["name"]
    list_filter = ["original_data_provider", "source_type"]
