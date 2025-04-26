import requests
from django.conf import settings
from django.http import JsonResponse
from django.views.generic import TemplateView


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
