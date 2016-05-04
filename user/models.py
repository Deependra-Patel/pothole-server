"""
Model for storing user details
"""

from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.contrib.gis.db import models
from django.core.validators import RegexValidator

from core.utils import CITIES


class User(AbstractBaseUser):
    """
    User model to store all the user related information
    """
    Name = models.CharField(max_length=50)
    Address = models.CharField(max_length=200, null=True, blank=True)
    HomeLocation = models.PointField(srid=4326, null=True, blank=True)
    City = models.CharField(max_length=3, choices=CITIES)
    Phone = models.CharField(
        validators=[RegexValidator(r'^\d{10}$', message="Phone number must be 10 digits")],
        max_length=10)
    Email = models.EmailField(unique=True)
    FbId = models.CharField(max_length=20, null=True, blank=True)
    Rating = models.FloatField(default=50)
    Credit = models.FloatField(default=0)
    DeActivate = models.BooleanField(default=False)
    Created = models.DateTimeField(auto_now_add=True)
    objects = UserManager()

    USERNAME_FIELD = 'Email'
    REQUIRED_FIELDS = ['Name', 'City', 'Phone']

    def get_full_name(self):
        # The user is identified by their email address
        return self.Email

    def get_short_name(self):
        # The user is identified by their email address
        return self.Email

    def __str__(self):
        return self.Email
