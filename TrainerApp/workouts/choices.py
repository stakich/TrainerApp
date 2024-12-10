from django.db import models


class DifficultyChoices(models.TextChoices):
    BEGINNER = 'Beginner', 'Beginner'
    INTERMEDIATE = 'Intermediate', 'Intermediate'
    ADVANCED = 'Advanced', 'Advanced'
    EXPERT = 'Expert', 'Expert'


class WorkoutType(models.TextChoices):
    STRENGTH = 'Strength', 'Strength'
    CARDIO = 'Cardio', 'Cardio'
    FLEXIBILITY = 'Flexibility', 'Flexibility'
