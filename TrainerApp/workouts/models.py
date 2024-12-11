from django.db import models
from TrainerApp.workouts.choices import DifficultyChoices, WorkoutType
from TrainerApp.accounts.models import UserProfile
from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator


UserModel = get_user_model()


# Create your models here.

class Exercise(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False, validators=[
        MinLengthValidator(5)
    ])
    description = models.TextField(blank=True, null=True)
    sets = models.PositiveIntegerField(default=1)
    reps = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name.capitalize()


class Workout(models.Model):
    trainer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='workouts')
    title = models.CharField(max_length=255, null=False, blank=False, validators=[
        MinLengthValidator(10)
    ])
    description = models.TextField()
    difficulty = models.CharField(max_length=50, choices=DifficultyChoices.choices, default=DifficultyChoices.BEGINNER)
    category = models.CharField(max_length=50, choices=WorkoutType.choices, default=WorkoutType.STRENGTH)
    exercises = models.ManyToManyField(to=Exercise, through='WorkoutExercise', related_name='workouts')


class WorkoutExercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
