from django.db import models
from django.contrib.auth import get_user_model
from TrainerApp.accounts.models import UserProfile
from TrainerApp.workouts.models import Workout

UserModel = get_user_model()


# Create your models here.

class Favorite(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='favorites')
    trainer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'trainer')


class Like(models.Model):
    to_workout = models.ForeignKey(
        to=Workout,
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
    )

