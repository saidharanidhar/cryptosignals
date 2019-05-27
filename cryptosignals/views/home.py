"""
Index View Module
"""
from django.http import HttpResponseRedirect


def index(request):
    """Redirects user based on the authentication"""
    if request.user.is_authenticated:
        return HttpResponseRedirect("/dashboard")
    return HttpResponseRedirect("/login")
