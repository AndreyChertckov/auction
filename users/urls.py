"""
Users related urls, such that `login` and `registration`
"""

from django.urls import path
from rest_framework.authtoken import views as token_views
from users import views

urlpatterns = [
    path("signin", token_views.obtain_auth_token),
    path("signup", views.UserCreate.as_view()),
]
