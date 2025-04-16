from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from indicators.models import (
    Category,
    FormatType,
    Indicator,
    IndicatorGeography,
    IndicatorType,
    OtherEndpointIndicator,
)
from indicators.resources import (
    IndicatorResource,
    IndicatorBaseResource,
    OtherEndpointIndicatorResource,
)


@admin.register(IndicatorType)
class IndicatorTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "display_name")
    search_fields = ("name", "display_name")
    ordering = ("name",)
    list_per_page = 50


@admin.register(FormatType)
class FormatTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "display_name")
    search_fields = ("name", "display_name")
    ordering = ("name",)
    list_per_page = 50


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "display_name")
    search_fields = ("name", "display_name")
    ordering = ("name",)
    list_per_page = 50


@admin.register(IndicatorGeography)
class IndicatorGeographyAdmin(admin.ModelAdmin):
    list_display = ("indicator", "geography", "aggregated_by_delphi")
    search_fields = ("indicator__name", "geography__name")
    list_filter = ("aggregated_by_delphi",)
    ordering = ("indicator__name",)
    list_per_page = 50
    list_select_related = True


@admin.register(Indicator)
class IndicatorAdmin(ImportExportModelAdmin):
    list_display = (
        "name",
        "description",
        "indicator_type",
        "format_type",
        "category",
        "geographic_scope",
    )
    search_fields = ("name", "description")
    list_filter = ("indicator_type", "format_type", "category", "geographic_scope")
    ordering = ("name",)
    list_per_page = 50
    list_select_related = True
    list_editable = ("indicator_type", "format_type", "category", "geographic_scope")
    list_display_links = ("name",)

    resource_classes = [IndicatorResource, IndicatorBaseResource]


@admin.register(OtherEndpointIndicator)
class OtherEndpointIndicatorAdmin(ImportExportModelAdmin):
    list_display = (
        "name",
        "description",
        "indicator_type",
        "format_type",
        "category",
        "geographic_scope",
    )
    search_fields = ("name", "description")
    list_filter = ("indicator_type", "format_type", "category", "geographic_scope")
    ordering = ("name",)
    list_per_page = 50
    list_select_related = True
    list_editable = ("indicator_type", "format_type", "category", "geographic_scope")
    list_display_links = ("name",)

    resource_classes = [OtherEndpointIndicatorResource]
