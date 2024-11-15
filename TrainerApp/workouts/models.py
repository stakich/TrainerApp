from django.db import models
from TrainerApp.workouts.choices import DifficultyChoices, WorkoutType
from TrainerApp.accounts.models import UserProfile
from django.contrib.auth import get_user_model

UserModel = get_user_model()


# Create your models here.

class Exercise(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)


class Workout(models.Model):
    trainer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    difficulty = models.CharField(max_length=50, choices=DifficultyChoices.choices, default=DifficultyChoices.BEGINNER)
    category = models.CharField(max_length=50, choices=WorkoutType.choices, default=WorkoutType.STRENGTH)


class WorkoutExercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets = models.PositiveIntegerField(default=1)
    reps = models.PositiveIntegerField(default=1)
