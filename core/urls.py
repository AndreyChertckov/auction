"""
Main routes of an api
"""

from django.urls import path, include

from core.views import ListCreateAuction


urlpatterns = [
    path("users/", include("users.urls")),
    path("auctions", ListCreateAuction.as_view()),
]
