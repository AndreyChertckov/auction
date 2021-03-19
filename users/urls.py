"""
Users related urls, such that `login` and `registration`
"""

from django.urls import path
from rest_framework.authtoken import views as token_views

urlpatterns = [
    path("login", token_views.obtain_auth_token),
]
