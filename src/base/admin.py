from django.contrib import admin

from base.models import Pathogen, GeographicScope, Geography, SeverityPyramidRung

# Register your models here.


@admin.register(Pathogen)
class PathogenAdmin(admin.ModelAdmin):
    """
    Admin interface for Pathogen model.
    """

    list_display = ["name", "used_in"]
    search_fields = ["name"]
    ordering = ["name"]
    list_filter = ["used_in"]
    list_per_page = 20
    list_display_links = ["name"]


@admin.register(GeographicScope)
class GeographicScopeAdmin(admin.ModelAdmin):
    """
    Admin interface for GeographicScope model.
    """

    list_display = ["name", "used_in"]
    search_fields = ["name"]
    ordering = ["name"]
    list_filter = ["used_in"]
    list_per_page = 20
    list_display_links = ["name"]


@admin.register(Geography)
class GeographyAdmin(admin.ModelAdmin):
    """
    Admin interface for Geography model.
    """

    list_display = ["name", "display_name", "used_in"]
    search_fields = ["name", "display_name"]
    ordering = ["name"]
    list_filter = ["used_in"]
    list_per_page = 20
    list_display_links = ["name"]


@admin.register(SeverityPyramidRung)
class SeverityPyramidRungAdmin(admin.ModelAdmin):
    """
    Admin interface for SeverityPyramidRung model.
    """

    list_display = ["name", "display_name", "used_in"]
    search_fields = ["name", "display_name"]
    ordering = ["name"]
    list_filter = ["used_in"]
    list_per_page = 20
    list_display_links = ["name"]
