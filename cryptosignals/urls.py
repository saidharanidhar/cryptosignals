"""cryptosignals URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include

import cryptosignals.views.details
from cryptosignals.views import home, dashboard
from cryptosignals.views import signup
from cryptosignals.views import settings
from cryptosignals.views import profile

urlpatterns = [
    path('', home.index),
    path('login/', views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('signup/', signup.SignUpView.as_view(), name='signup'),

    path('profile/', profile.ProfileView.as_view(), name='profile'),
    path('dashboard/', dashboard.Dashboard.as_view(), name='dashboard'),
    path('dashboard/<slug:coin>/', cryptosignals.views.details.Details.as_view(), name='details'),
    path('settings/', settings.SettingsView.as_view(), name='settings'),

    path('api/', include('cryptosignals.api.urls')),
    path('admin/', admin.site.urls),
]
