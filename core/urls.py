"""
Main routes of an api
"""

from django.urls import path, include

from core.views import ListCreateAuction, CreateBet, RetrieveAuction


urlpatterns = [
    path("users/", include("users.urls")),
    path("auctions", ListCreateAuction.as_view(), name="get-all-auctions"),
    path("auctions/<pk>", RetrieveAuction.as_view(), name="get-auction"),
    path("bets", CreateBet.as_view(), name="create-bets"),
]
