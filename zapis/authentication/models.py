from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from rest_framework.authtoken.models import Token
from authentication.task import  mock_otp_verification

class User(AbstractUser):
    ROLE_CHOICES = (
        ('administrator', 'Administrator'),
        ('master', 'Master'),
        ('client', 'Client'),
    )

    role = models.CharField(max_length=15, choices=ROLE_CHOICES)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

class OTPRecord(models.Model):
    phone_number = models.CharField(max_length=15)
    otp = models.CharField(max_length=6)

    def __str__(self):
        return f"OTPRecord for {self.phone_number}"
