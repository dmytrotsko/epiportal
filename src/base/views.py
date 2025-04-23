from datetime import datetime as dtime

import requests
from django.conf import settings
from django.http import JsonResponse
from django.views.generic import TemplateView
from epiweeks import Week


class BadRequestErrorView(TemplateView):
    """
    Displays a custom 400 error page when a bad request is made.
    """

    template_name = "http_errors/400.html"


class ForbiddenErrorView(TemplateView):
    """
    Displays a custom 403 error page when access to a resource is forbidden.
    """

    template_name = "http_errors/403.html"


class NotFoundErrorView(TemplateView):
    """
    Displays a custom 404 error page when a page is not found.
    """

    template_name = "http_errors/404.html"


class InternalServerErrorView(TemplateView):
    """
    Displays a custom 500 error page when an internal server error occurs.
    """

    template_name = "http_errors/500.html"


def epidata(request, endpoint=""):
    params = request.GET.dict()
    params["api_key"] = settings.EPIDATA_API_KEY
    url = f"{settings.EPIDATA_URL}{endpoint}"
    response = requests.get(url, params=params)
    return JsonResponse(response.json(), safe=False)


def get_epiweek(request):
    start_date = dtime.strptime(request.POST["start_date"], "%Y-%m-%d")
    start_date = Week.fromdate(start_date)
    end_date = dtime.strptime(request.POST["end_date"], "%Y-%m-%d")
    end_date = Week.fromdate(end_date)
    return JsonResponse(
        {
            "start_date": f"{start_date.year}{start_date.week if start_date.week >= 10 else '0' + str(start_date.week)}",
            "end_date": f"{end_date.year}{end_date.week if end_date.week >= 10 else '0' + str(end_date.week)}",
        }
    )
