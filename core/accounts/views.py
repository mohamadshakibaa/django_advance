from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
from django.views.decorators.cache import cache_page
from .tasks import sending_email


def send_email(request):
    sending_email.delay()
    return HttpResponse("Done")


@cache_page
def test(request):
    response = requests.get(
        "https://0ee50da1-514c-411f-a289-027a2f6f5572.mock.pstmn.io/test/delay/5"
    )
    return JsonResponse(response.json())
