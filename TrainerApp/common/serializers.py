from rest_framework import serializers
from TrainerApp.common.models import Favorite, Like


class FavoriteSerializer(serializers.Serializer):
    class Meta:
        model = Favorite
        fields = '__all__'
        read_only_fields = ['timestamp']


class LikeSerializer(serializers.Serializer):
    class Meta:
        model = Like
        fields = '__all__'
        read_only_fields = ['timestamp']