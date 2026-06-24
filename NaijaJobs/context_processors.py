import time

from django.conf import settings


def cache_buster(request):
    return {
        "static_version": time.time_ns() if settings.DEBUG else "",
    }
