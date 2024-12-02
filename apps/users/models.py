from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    # User info
    email = models.CharField(max_length=254, unique=True, null=False)
    phone = models.CharField(max_length=254, unique=True, null=False)

    # profile_pic     =   models.ImageField(upload_to='media/profile_pic',blank=True,null=True) # uncomment needed

    # Account info
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    last_login = models.DateTimeField(default=timezone.now)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['phone']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
