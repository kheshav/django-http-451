from .models import http451_URLS as http451_URLS_Model
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib.gis.geoip2 import GeoIP2


class HttpResponseUnavailableForLegalReason(HttpResponse):
    status_code = 451
    reason_phrase = "Unavailable For Legal Reasons"


class http451Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # code to be executed before the view
        try:
            geoblocked = False
            remoteADDR = request.META["REMOTE_ADDR"]
            if "HTTP_X_FORWARDED_FOR" in request.META:
                remoteADDR = request.META["HTTP_X_FORWARDED_FOR"]
            URL = request.META['PATH_INFO'] + ("?" + request.META["QUERY_STRING"]) if (request.META["QUERY_STRING"] is not "") else request.META['PATH_INFO']
            restricted = http451_URLS_Model.objects.filter(urls_to_block=URL)
            if restricted.exists():
                geoIP = GeoIP2()
                restricted = restricted.values()[0]
                params = {
                    'censorship_reason': restricted['censorship_reason'],
                    'censorship_title': restricted['censorship_title'],
                    'url_of_authority': restricted['url_of_authority']
                }
                rendered = render_to_string('blockedResource.html', {**params})
                if restricted["block_by_country"] and remoteADDR != "127.0.0.1":
                    if geoIP.country(remoteADDR)["country_code"] not in restricted["country_code"].split():
                        return self.get_response(request)
                    else:
                        geoblocked = True
                response = HttpResponseUnavailableForLegalReason(rendered)
                response['Link'] = URL + '; rel="blocked-by"'
                if geoblocked:
                    response['geo-scope-block'] = geoIP.country(remoteADDR)["country_code"]
                return response

            return self.get_response(request)
        except Exception as e:
            print(e)
            return self.get_response(request)
