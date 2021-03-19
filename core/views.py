"""
CRUD for auction and bets
"""

from rest_framework.generics import ListCreateAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from core.models import Auction
from core.serializers import CreateAuctionSerializer


class ListCreateAuction(ListCreateAPIView):
    queryset = Auction.objects.all()
    serializer_class = CreateAuctionSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
