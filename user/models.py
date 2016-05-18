"""
Model for storing user details
"""

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.gis.db import models
from django.core.validators import RegexValidator

from core.utils import CITIES


class MyUserManager(BaseUserManager):
    def create_user(self, Email, Name, City, Phone, password=None):
        """
        Creates and saves a User with the given Email, Name, city, phone
        """
        if not Email:
            raise ValueError('Users must have an Email address')

        user = self.model(
            Email=MyUserManager.normalize_email(Email),
            Name=Name,
            City=City,
            Phone=Phone,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, Email, Name, City, Phone, password):
        """
        Creates and saves a superuser with the given email, name, city, phone and password
        """
        print("dd", Email, Name, City, Phone, password)
        u = self.create_user(Email=Email,
                             Name=Name,
                             City=City,
                             Phone=Phone,
                             password=password,
                             )
        u.is_admin = True
        u.save(using=self._db)
        return u


class User(AbstractBaseUser, PermissionsMixin):
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
    is_admin = models.BooleanField(default=False)
    objects = MyUserManager()

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

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    @property
    def is_staff(self):
        """
        Is the user a member of staff?
        """
        return self.is_admin
