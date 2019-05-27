"""
Profile View Module
"""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView

from cryptosignals.forms import EditUserDetailsForm


class ProfileView(LoginRequiredMixin, FormView):
    """Profile view class"""
    template_name = 'profile.html'
    form_class = EditUserDetailsForm
    success_url = '/'

    def form_valid(self, form):
        """Saves the form along with user instance"""
        form.instance.user = self.request.user
        form.save()
        return super(ProfileView, self).form_valid(form)

    def get_form(self, form_class=None):
        """Provides form with initial data"""
        if not form_class:
            form_class = self.get_form_class()
        return form_class(instance=self.request.user, **self.get_form_kwargs())
