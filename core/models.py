"""
Models for core application
"""
from django.db import models
from django.conf import settings

from core.constants import AuctionStatus


class Auction(models.Model):
    """
    Model for auction

    Fields
    ------
    name:
        Name of the product
    description:
        Short description of the product
    owner:
        Owner of the auction
    end_time:
        Time of the end of the auction
    status:
        If auction is active or not
    """

    name = models.CharField(max_length=256)
    description = models.TextField()

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    end_time = models.DateTimeField()
    status = models.SmallIntegerField(
        choices=AuctionStatus.CHOICES, default=AuctionStatus.ACTIVE
    )

    start_price = models.FloatField()
    step_price = models.FloatField()
