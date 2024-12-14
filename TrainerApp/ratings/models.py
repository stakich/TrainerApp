from django.db import models
from django.contrib.auth import get_user_model
from TrainerApp.accounts.models import UserProfile
from TrainerApp.ratings.choices import RatingChoices
UserModel = get_user_model()


class Rating(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    trainer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RatingChoices.choices, default=RatingChoices.RATING_1)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'trainer')