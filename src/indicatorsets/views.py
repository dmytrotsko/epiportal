import logging
import json

from django.views.generic import ListView
from django.conf import settings

from indicatorsets.models import IndicatorSet
from indicatorsets.forms import IndicatorSetFilterForm
from base.models import Geography, GeographyUnit

logger = logging.getLogger(__name__)


class IndicatorSetListView(ListView):
    model = IndicatorSet
    template_name = "indicatorsets/indicatorsets.html"
    context_object_name = "indicatorsets"

    def get_queryset(self):
        try:
            return IndicatorSet.objects.all().prefetch_related(
                "geographic_scope",
            )
        except Exception as e:
            logger.error(f"Error fetching indicator sets: {e}")
            return IndicatorSet.objects.none()

    def get_related_indicators(self, queryset, indicator_set_ids: list):
        related_indicators = []
        for indicator in queryset.filter(
            indicator_set__id__in=indicator_set_ids
        ).prefetch_related("indicator_set", "source", "severity_pyramid_rungs"):
            related_indicators.append(
                {
                    "id": indicator.id,
                    "display_name": indicator.get_display_name,
                    "member_name": indicator.member_name,
                    "member_short_name": indicator.member_short_name,
                    "name": indicator.name,
                    "indicator_set": indicator.signal_set.id,
                    "indicator_set_name": indicator.signal_set.name,
                    "indicator_set_short_name": indicator.signal_set.short_name,
                    "endpoint": indicator.signal_set.endpoint,
                    "source": indicator.source.name,
                    "time_type": indicator.time_type,
                    "description": indicator.description,
                    "member_description": indicator.member_description,
                    "restricted": indicator.signal_set.dua_required,
                }
            )
        return related_indicators

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        # url_params_dict, url_params_str = self.get_url_params()
        # filter = SignalSetFilter(self.request.GET, queryset=queryset)
        # context["url_params_dict"] = url_params_dict
        # context["url_params_str"] = url_params_str
        context["epivis_url"] = settings.EPIVIS_URL
        context["epidata_url"] = settings.EPIDATA_URL
        # context["form"] = SignalSetFilterForm(initial=url_params_dict)
        context["form"] = IndicatorSetFilterForm()
        # context["filter"] = filter
        # context["signal_sets"] = filter.qs
        # context["related_signals"] = json.dumps(
        #     self.get_related_indicators(
        #         filter.signals_qs, filter.qs.values_list("id", flat=True)
        #     )
        # )
        # context["related_signals"] = json.dumps(
        #     self.get_related_indicators(
        #         queryset=queryset, indicator_set_ids=queryset.values_list("id", flat=True)
        #     )
        # )
        context["available_geographies"] = Geography.objects.filter(used_in="signals")
        context["geographic_granularities"] = [
            {
                "id": str(geo_unit.geo_id),
                "geoType": geo_unit.geo_level.name,
                "text": geo_unit.display_name,
            }
            for geo_unit in GeographyUnit.objects.all().prefetch_related("geo_level")
        ]
        return context
