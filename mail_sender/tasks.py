"""
Mail sending tasks are placed here
"""

from logging import getLogger

from django.urls import reverse
from django.contrib.auth import get_user_model
from django.conf import settings

import celery

from core.models import Auction, Bet
from core.constants import AuctionStatus
from mail_sender.utils import broadcast_emails

User = get_user_model()
logger = getLogger(__name__)


@celery.shared_task()
def new_auction(auction_id: int):
    """
    Send notification for all sign up users about new auction
    """
    auction = Auction.objects.get(pk=auction_id)
    users = list(User.objects.all().values_list("email", flat=True))
    broadcast_emails(
        users,
        f"Hi there, new auction are here! {settings.ADDRESS + reverse('get-auction', args=(auction_id,))}",
    )


@celery.shared_task()
def price_of_auction_has_changed(bet_id: int):
    """
    Notify users that participated in auction that price has been changed
    """
    bet = Bet.objects.get(pk=bet_id)
    auction = bet.auction
    participance_id = auction.bet_set.exclude(user=bet.user).values_list(
        "user", flat=True
    )
    participance = list(
        User.objects.filter(pk__in=participance_id).values_list("email", flat=True)
    )

    broadcast_emails(
        participance,
        f"Hi there, price of the auction {auction.name} has been changed. Current price is {bet.price}",
    )


@celery.shared_task()
def auction_end(auction_id: int):
    """
    Winner detection. Send notfification about end of the auction
    """
    auction = Auction.objects.get(pk=auction_id)
    auction.status = AuctionStatus.FINISHED
    auction.save()
    try:
        winner_bet = auction.bet_set.reverse()[0]
    except IndexError:
        logger.warning(f"Nobody participated in auction {auction.name}")
        return

    winner = winner_bet.user
    participance_id = auction.bet_set.values_list("user", flat=True)
    participance = list(
        User.objects.filter(pk__in=participance_id).values_list("email", flat=True)
    )

    broadcast_emails(
        participance,
        f"Hi there, Auction is ending now, winner is {winner.email}, last price is {winner_bet.price}",
    )
