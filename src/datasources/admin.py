from django.contrib import admin

from import_export.admin import ImportExportModelAdmin
from datasources.models import SourceSubdivision
from datasources.resources import SourceSubdivisionResource

# Register your models here.


@admin.register(SourceSubdivision)
class SourceSubdivisionAdmin(ImportExportModelAdmin):
    """
    Admin interface for Source Subdivision model.
    """

    list_display = (
        "name",
        "display_name",
        "external_name",
        "description",
        "license",
        "dua",
        "datasource_name",
    )
    search_fields = ("name", "display_name", "external_name")
    ordering = ["name"]
    list_filter = ["datasource_name"]
    resource_classes = [SourceSubdivisionResource]
