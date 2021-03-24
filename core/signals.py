from logging import getLogger

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from core.models import Auction, Bet
from mail_sender.tasks import new_auction, price_of_auction_has_changed, auction_end

logger = getLogger(__name__)


@receiver(post_save, sender=Auction)
def send_notification_new_auction(sender, instance, created, **kwargs):
    """
    Post save signal, that will be called after new auction is created
    """
    logger.info("New action is creating")
    if created:
        new_auction.delay(instance.id)
        logger.info(f"End in {instance.end_time} seconds")
        auction_end.apply_async((instance.id,), eta=instance.end_time)


@receiver(post_save, sender=Bet)
def send_notification_new_bet(sender, instance, created, **kwargs):
    """
    Post save signal, that will be called after new auction is created
    """
    if created:
        price_of_auction_has_changed.delay(instance.id)
