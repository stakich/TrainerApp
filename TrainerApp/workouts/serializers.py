from rest_framework import serializers
from TrainerApp.workouts.models import Exercise, WorkoutExercise


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['id', 'name', 'description']


class WorkoutExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutExercise
        fields = ['exercise', 'sets', 'reps', 'workout']