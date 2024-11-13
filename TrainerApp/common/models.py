from django.db import models
from django.contrib.auth import get_user_model
from TrainerApp.accounts.models import UserProfile

UserModel = get_user_model()


# Create your models here.

class Favorite(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    trainer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'trainer')


class Comment(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)

    content = models.TextField(max_length=256)

    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.workout}"

    class Meta:
        indexes = [
            models.Index(fields=['date_time_of_publication']),
        ]
        ordering = ['-date_time_of_publication']


class Like(models.Model):
    to_workout = models.ForeignKey(
        to=Workout,
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
    )

