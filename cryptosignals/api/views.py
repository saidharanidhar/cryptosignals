"""
API Views
"""
from django.http import HttpResponse

from cryptosignals.services.refresh import update_currencies_and_send_notification


def hotload(request):
    """Refreshes the data and updates database"""
    update_currencies_and_send_notification()
    return HttpResponse(content="ok")
