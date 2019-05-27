"""
Notification settings Module
"""
from django.contrib.auth.mixins import LoginRequiredMixin

from cryptosignals.forms import SettingsForm
from django.views.generic.edit import FormView


class SettingsView(LoginRequiredMixin, FormView):
    """Settings View Class"""
    template_name = 'settings.html'
    form_class = SettingsForm
    success_url = '/'

    def form_valid(self, form):
        """Saves Form along with user instance"""
        form.instance.user = self.request.user
        form.save()
        return super(SettingsView, self).form_valid(form)

    def get_form(self, form_class=None):
        """Provides form with initial data"""
        if not form_class:
            form_class = self.get_form_class()
        return form_class(instance=self.request.user, **self.get_form_kwargs())
