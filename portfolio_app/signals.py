from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
import logging

logger = logging.getLogger("django")

@receiver(user_logged_in)
def after_login(sender, request, user):
    logger.info(f"{user.username} logged in at {user.last_login}")

@receiver(user_logged_out)
def after_logout(sender, request, user):
    logger.info(f"{user.username} logged out")
