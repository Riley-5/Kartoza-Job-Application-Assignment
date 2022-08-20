from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    home_address = models.Charfield(max_length=500)
    phone_number = models.PositiveBigIntegerField()
    location_latitude = models.DecimalField(max_digits=30, decimal_places=28)
    location_longtitude = models.DecimalField(max_digits=30, decimal_places=28)

    def __str__(self):
        return f"{self.id} | {self.username}"

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "home_address": self.home_address,
            "phone_number": self.phone_number,
            "location_latitude": self.location_latitude,
            "location_longitude": self.location_longtitude
        }