"""
Forms Module
"""
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    """SignUp form"""
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)

    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email',)


class SettingsForm(forms.ModelForm):
    """Notification settings Form"""
    token = forms.CharField(max_length=255, required=False)
    channel = forms.CharField(max_length=32, required=False)
    subscription = forms.BooleanField(required=False)

    class Meta:
        model = get_user_model()
        fields = ('token', 'channel', 'subscription')


class EditUserDetailsForm(forms.ModelForm):
    """Edit User details Form"""
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254, required=False)

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email',)

