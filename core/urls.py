"""
Main routes of an api
"""

from django.urls import path, include

from core.views import ListCreateAuction, CreateBet, RetrieveAuction


urlpatterns = [
    path("users/", include("users.urls")),
    path("auctions", ListCreateAuction.as_view()),
    path("auctions/<pk>", RetrieveAuction.as_view()),
    path("bets", CreateBet.as_view()),
]
