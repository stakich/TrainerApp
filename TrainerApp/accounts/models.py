from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.core.validators import MinLengthValidator
from TrainerApp.accounts.managers import AppUserManager


class AppUser(AbstractUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150, blank=False, null=False, validators=[
        MinLengthValidator(5)
    ])
    last_name = models.CharField(max_length=150, blank=False, null=False, validators=[
        MinLengthValidator(5)
    ])
    username = models.CharField(
        max_length=150,
        unique=True,
        blank=False,
        null=False,
        validators=[MinLengthValidator(5)]
    )

    objects = AppUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='appuser_groups',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='appuser_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )


class UserProfile(models.Model):
    user = models.OneToOneField(AppUser, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.URLField(blank=True, null=True)
    specialization = models.CharField(max_length=255, null=True, blank=True, validators=[
        MinLengthValidator(5)
    ])
    experience_years = models.PositiveIntegerField(default=0, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True, validators=[
        MinLengthValidator(5)
    ])
    is_approved = models.BooleanField(default=None, null=True, blank=True)
    is_trainer = models.BooleanField(default=False)
