"""
Sending utils
"""
from logging import getLogger
from typing import Iterable

from django.contrib.auth import get_user_model

User = get_user_model()

logger = getLogger(__name__)


def broadcast_emails(users: Iterable[User], text: str):
    for user in users:
        send_email(user, text)


def send_email(user: User, text: str):
    logger.info(f"Try to send email to {user.email} - {text}")
