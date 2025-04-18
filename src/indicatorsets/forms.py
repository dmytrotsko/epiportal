from django import forms

from base.models import Pathogen, GeographicScope, Geography, SeverityPyramidRung
from indicatorsets.models import IndicatorSet





class IndicatorSetFilterForm(forms.ModelForm):

    pathogens = forms.ModelMultipleChoiceField(
        queryset=Pathogen.objects.filter(used_in="indicatorsets"),
        widget=forms.CheckboxSelectMultiple(),
    )

    geographic_scope = forms.ModelChoiceField(
        queryset=GeographicScope.objects.filter(used_in="indicatorsets").order_by(
            "display_order_number"
        ),
        widget=forms.CheckboxSelectMultiple(),
    )

    geographic_levels = forms.ModelMultipleChoiceField(
        queryset=Geography.objects.filter(used_in="indicatorsets").order_by(
            "display_order_number"
        ),
        widget=forms.CheckboxSelectMultiple(),
    )
    severity_pyramid_rungs = forms.ModelMultipleChoiceField(
        queryset=SeverityPyramidRung.objects.filter(used_in="indicatorsets").order_by(
            "display_order_number"
        ),
        widget=forms.CheckboxSelectMultiple(),
    )

    original_data_provider = forms.ChoiceField(
        choices=[
            (el, el)
            for el in set(
                IndicatorSet.objects.values_list("original_data_provider", flat=True)
            )
        ],
        widget=forms.CheckboxSelectMultiple(),
    )

    temporal_granularity = forms.ChoiceField(
        choices=[
            ("Annually", "Annually"),
            ("Monthly", "Monthly"),
            ("Weekly", "Weekly"),
            ("Daily", "Daily"),
            ("Hourly", "Hourly"),
            ("Other", "Other"),
        ],
        widget=forms.CheckboxSelectMultiple(),
    )

    temporal_scope_end = forms.ChoiceField(
        choices=[
            ("Ongoing", "Ongoing Surveillance Only"),
        ],
        required=False,
        widget=forms.CheckboxSelectMultiple(),
    )

    location_search = forms.CharField(
        label=("Location Search"),
        widget=forms.TextInput(),
    )

    class Meta:
        model = IndicatorSet
        fields: list[str] = [
            "pathogens",
            "geographic_scope",
            "geographic_levels",
            "severity_pyramid_rungs",
            "original_data_provider",
            "temporal_granularity",
            "temporal_scope_end",
        ]

    def __init__(self, *args, **kwargs) -> None:
        """
        Initialize the form.
        """
        super().__init__(*args, **kwargs)

        # Set required attribute to False and disable helptext for all fields
        for field_name, field in self.fields.items():
            field.required = False
            field.help_text = ""
            field.label = ""
