from django.db import models


class DifficultyChoices(models.TextChoices):
    BEGINNER = 'beginner', 'Beginner'
    INTERMEDIATE = 'intermediate', 'Intermediate'
    ADVANCED = 'advanced', 'Advanced'
    EXPERT = 'expert', 'Expert'


class WorkoutType(models.TextChoices):
    STRENGTH = 'strength', 'Strength'
    CARDIO = 'cardio', 'Cardio'
    FLEXIBILITY = 'flexibility', 'Flexibility'
