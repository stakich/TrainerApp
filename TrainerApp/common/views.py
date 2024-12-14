from django.shortcuts import render
from TrainerApp.accounts.models import UserProfile
from django.views import generic
from TrainerApp.common import forms
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from TrainerApp.common.serializers import FavoriteSerializer, LikeSerializer
from TrainerApp.common.models import Favorite, Like
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from TrainerApp.common.mixin import RedirectOnUnAuthMixin
from TrainerApp.workouts.models import Workout


# Create your views here.


class HomePage(generic.ListView):
    model = UserProfile
    template_name = 'common/homepage.html'
    context_object_name = 'all_trainers'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['searchform'] = forms.SearchForm(self.request.GET)

        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        trainer_name = self.request.GET.get('trainer_name')
        queryset = queryset.filter(is_trainer=True)

        if trainer_name:
            queryset = queryset.filter(user__first_name__icontains=trainer_name)

        return queryset


class FavoriteTrainerAPIView(RedirectOnUnAuthMixin, APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, trainer_id):
        user = request.user
        trainer = get_object_or_404(UserProfile, id=trainer_id)

        favorite, created = Favorite.objects.get_or_create(user=user, trainer=trainer)

        if created:
            serializer = FavoriteSerializer(favorite)
            return Response({'message': 'Trainer added to favorites!'}, status=status.HTTP_201_CREATED)
        else:
            favorite.delete()
            return Response({'message': 'Trainer removed from favorites!'}, status=status.HTTP_200_OK)


class LikeWorkoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, workout_id):
        user = request.user
        workout = get_object_or_404(Workout, id=workout_id)

        like, created = Like.objects.get_or_create(user=user, to_workout=workout)

        if created:
            serializer = LikeSerializer(like)
            return Response({'message': 'Workout liked!'}, status=status.HTTP_201_CREATED)
        else:
            like.delete()
            return Response({'message': 'Workout unliked!'}, status=status.HTTP_200_OK)