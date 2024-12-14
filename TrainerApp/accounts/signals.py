from django.db.models.signals import post_save
from django.dispatch import receiver
from TrainerApp.accounts.models import AppUser, UserProfile


@receiver(post_save, sender=AppUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(
            user=instance,
            is_trainer=False,
            specialization="Default Specialization",
        )