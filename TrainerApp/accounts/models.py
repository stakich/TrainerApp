from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin


# Create your models here.

class AppUser(AbstractUser, PermissionsMixin):
    is_trainer = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='appuser_groups',  # Use a custom related_name to avoid conflict
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='appuser_permissions',  # Use a custom related_name to avoid conflict
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )


class UserProfile(models.Model):
    user = models.OneToOneField(AppUser, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.URLField(blank=True, null=True)
    specialization = models.CharField(max_length=255, null=True, blank=True)
    experience_years = models.PositiveIntegerField(default=0, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    is_approved = models.BooleanField(default=False, null=True, blank=True)
