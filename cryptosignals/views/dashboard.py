"""
DashboardView Module
"""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView

from cryptosignals.services.utils import get_dashboard_data


class Dashboard(LoginRequiredMixin, TemplateView):
    """Dashboard View"""
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        """Adds Currency data along with subscription details"""
        context = super().get_context_data(**kwargs)
        subscribed = self.request.user.get_subscription_list()
        context['currencies'] = get_dashboard_data(subscribed)
        return context
