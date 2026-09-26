from django.shortcuts import render
from django.http import HttpResponse
import time
from .tasks import sending_email


def send_email(request):
    sending_email.delay()
    return HttpResponse("Done")