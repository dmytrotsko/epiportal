from django.db import models

USED_IN_CHOICES = (
    ("indicators", "Indicators"),
    ("indicatorsets", "Indicator Sets"),
)


class Pathogen(models.Model):

    name: models.CharField = models.CharField(
        verbose_name="Name", max_length=255, unique=True
    )
    display_name: models.CharField = models.CharField(
        verbose_name="Display Name", max_length=255, blank=True
    )

    used_in: models.CharField = models.CharField(
        verbose_name="Used In",
        max_length=255,
        blank=True,
        choices=USED_IN_CHOICES,
        help_text="Indicates where the pathogen is used",
    )

    class Meta:
        verbose_name = "Pathogen"
        verbose_name_plural = "Pathogens"
        ordering = ["name"]
        indexes = [
            models.Index(fields=["name"], name="pathogen_name_idx"),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=["name", "used_in"], name="unique_pathogen_name_used_in"
            )
        ]

    def __str__(self):
        return self.name


class GeographicScope(models.Model):

    name: models.CharField = models.CharField(verbose_name="Name", max_length=255)

    used_in: models.CharField = models.CharField(
        verbose_name="Used In",
        max_length=255,
        blank=True,
        choices=USED_IN_CHOICES,
        help_text="Indicates where the geographic scope is used",
    )

    class Meta:
        verbose_name = "Geographic Scope"
        verbose_name_plural = "Geographic Scopes"
        ordering = ["name"]
        indexes = [
            models.Index(fields=["name"], name="geographic_scope_name_idx"),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=["name", "used_in"],
                name="unique_geographic_scope_name_used_in",
            )
        ]

    def __str__(self):
        return self.name


class Geography(models.Model):

    name: models.CharField = models.CharField(verbose_name="Name", max_length=255)
    display_name: models.CharField = models.CharField(
        verbose_name="Display Name", max_length=255, blank=True
    )
    display_order_number: models.IntegerField = models.IntegerField(
        verbose_name="Display Order Number", blank=True, null=True
    )
    used_in: models.CharField = models.CharField(
        verbose_name="Used In",
        max_length=255,
        blank=True,
        choices=USED_IN_CHOICES,
        help_text="Indicates where the geography is used",
    )

    class Meta:
        verbose_name = "Geography"
        verbose_name_plural = "Geographies"
        ordering = ["name"]
        indexes = [
            models.Index(fields=["name"], name="geography_name_idx"),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=["name", "used_in"], name="unique_geography_name_used_in"
            )
        ]

    def __str__(self):
        return self.name


class SeverityPyramidRung(models.Model):

    name: models.CharField = models.CharField(verbose_name="Name", max_length=255)
    display_name: models.CharField = models.CharField(
        verbose_name="Display Name", max_length=255, blank=True
    )
    display_order_number: models.IntegerField = models.IntegerField(
        verbose_name="Display Order Number", blank=True, null=True
    )
    used_in: models.CharField = models.CharField(
        verbose_name="Used In",
        max_length=255,
        blank=True,
        choices=USED_IN_CHOICES,
        help_text="Indicates where the severity pyramid rung is used",
    )

    class Meta:
        verbose_name = "Severity Pyramid Rung"
        verbose_name_plural = "Severity Pyramid Rungs"
        ordering = ["name"]
        indexes = [
            models.Index(fields=["name"], name="severity_pyramid_rung_name_idx"),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=["name", "used_in"],
                name="unique_severity_pyramid_rung_name_used_in",
            )
        ]

    def __str__(self):
        return self.display_name if self.display_name else self.name
