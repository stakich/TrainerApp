from rest_framework import serializers
from TrainerApp.ratings.models import Rating
from rest_framework.decorators import action
from rest_framework.response import Response



class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['user', 'trainer', 'rating', 'timestamp']
        read_only_fields = ['timestamp']

