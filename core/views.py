"""
CRUD for auction and bets
"""

from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from django_filters.rest_framework import DjangoFilterBackend

from core.models import Auction, Bet
from core.serializers import AuctionSerializer, BetSerializer, DetailAuctionSerializer


class ListCreateAuction(ListCreateAPIView):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["status"]


class RetrieveAuction(RetrieveAPIView):
    queryset = Auction.objects.all()
    serializer_class = DetailAuctionSerializer


class CreateBet(CreateAPIView):
    queryset = Bet.objects.all()
    serializer_class = BetSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
