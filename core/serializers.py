from logging import getLogger

from django.utils import timezone
from rest_framework import serializers

from core.models import Auction, Bet
from users.serializers import UserSerializer

logger = getLogger(__name__)


class AuctionSerializer(serializers.ModelSerializer):
    owner = UserSerializer(default=serializers.CurrentUserDefault())
    status = serializers.CharField(source="get_status_display", required=False)

    class Meta:
        model = Auction
        fields = "__all__"
        read_only = ("status",)

    def validate_end_time(self, value):
        """
        Validated that end_time in the future
        """
        if value < timezone.now():
            raise serializers.ValidationError("Must be in the future")
        return value

    def validate_start_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Must be greater than zero")
        return value

    def validate_step_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Must be greater than zero")
        return value


class BetSerializer(serializers.ModelSerializer):
    user = UserSerializer(default=serializers.CurrentUserDefault())

    class Meta:
        model = Bet
        fields = "__all__"
        extra_kwargs = {"auction": {"write_only": True}}

    def validate(self, values):
        values = super().validate(values)
        if values["auction"].owner == values["user"]:
            raise serializers.ValidationError(
                {"user": "You donot allowed to put bets on your auctions."}
            )

        try:
            minimum_price = max(
                values["auction"].start_price,
                values["auction"].bet_set.order_by("-pk")[0].price
                + values["auction"].step_price,
            )
        except IndexError:
            minimum_price = values["auction"].start_price

        if minimum_price > values["price"]:
            raise serializers.ValidationError(
                {"price": f"Must be greater than higher bet: {minimum_price}"}
            )

        if values["auction"].end_time < timezone.now():
            raise serializers.ValidationError("You are late")

        return values


class DetailAuctionSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    status = serializers.CharField(source="get_status_display", required=False)
    bets = BetSerializer(many=True, read_only=True, source="bet_set")

    class Meta:
        model = Auction
        fields = "__all__"
        read_only = "__all__"
