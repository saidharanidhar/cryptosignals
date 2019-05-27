"""
Details View Module
"""

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from cryptosignals.models import Currency


class Details(LoginRequiredMixin, TemplateView):
    """Details View class"""
    template_name = "details.html"

    def get_context_data(self, **kwargs):
        """Return the Coin and Subscription details"""
        currency = get_object_or_404(Currency, **kwargs)
        details = dict(value=currency.value, stats=currency.get_stats())
        details['subscription'] = currency.coin in self.request.user.get_subscription_list()
        return details

    def post(self, request, *args, **kwargs):
        """Handles subscription requests"""
        coin = kwargs.get('coin')
        self.request.user.toggle_subscription(coin)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        """Return the URL to redirect to after processing post request."""
        return self.request.path
