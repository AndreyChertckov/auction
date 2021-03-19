from logging import getLogger

from django.utils import timezone
from rest_framework import serializers

from core.models import Auction
from users.serializers import UserSerializer

logger = getLogger(__name__)


class CreateAuctionSerializer(serializers.ModelSerializer):
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
