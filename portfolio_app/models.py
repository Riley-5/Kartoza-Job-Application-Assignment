from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver

# Create your models here.
"""
    Extends user class to include additional information
        Home address
        Phone Number
        Location
    Sets is_staff to true so that the user can log in from Django Admin
"""
class User(AbstractUser):
    is_staff = models.BooleanField(default=True)
    home_address = models.CharField(max_length=500, null=True)
    phone_number = models.PositiveBigIntegerField(null=True)
    location_latitude = models.DecimalField(max_digits=30, decimal_places=28, null=True)
    location_longitude = models.DecimalField(max_digits=30, decimal_places=28, null=True)

    def __str__(self):
        return f"{self.id} | {self.username}"

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "home_address": self.home_address,
            "phone_number": self.phone_number,
            "location_latitude": self.location_latitude,
            "location_longitude": self.location_longitude
        }

@receiver(user_logged_in, sender=User)
def log_login(sender, request, user, **kwargs):
    print(f"{user.username} logged in")

@receiver(user_logged_out, sender=User)
def log_login(sender, request, user, **kwargs):
    print(f"{user.username} logged out")