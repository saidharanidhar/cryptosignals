"""
SignUp module
"""
from cryptosignals.forms import SignUpForm
from django.views.generic.edit import FormView


class SignUpView(FormView):
    """Signup View"""
    template_name = 'registration/signup.html'
    form_class = SignUpForm
    success_url = '/login/'

    def form_valid(self, form):
        """Saves Form and redirects"""
        form.save()
        return super().form_valid(form)
