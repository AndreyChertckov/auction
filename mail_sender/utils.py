"""
Sending utils
"""
from logging import getLogger

from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()

logger = getLogger(__name__)


def broadcast_emails(users_emails: list[str], text: str):
    send_mail(
        "Auction app",
        text,
        settings.DEFAULT_FROM_EMAIL,
        users_emails,
        fail_silently=False,
    )
