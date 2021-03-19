"""
Main routes of an api
"""

from django.urls import path, include


urlpatterns = [
    path("users/", include("users.urls")),
]
