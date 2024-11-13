from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class AppUser(AbstractUser):
    is_trainer = models.BooleanField(default=False)


class UserProfile(models.Model):
    user = models.OneToOneField(AppUser, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.URLField(blank=True, null=True)
    specialization = models.CharField(max_length=255, null=True, blank=True)
    experience_years = models.PositiveIntegerField(default=0, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    is_approved = models.BooleanField(default=False, null=True, blank=True)
