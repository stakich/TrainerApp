from django.urls import path
from TrainerApp.common import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('api/favorite-trainer/<int:trainer_id>/', views.FavoriteTrainerAPIView.as_view(), name='favorite-trainer'),
    path('api/like-workout/<int:workout_id>/', views.LikeWorkoutAPIView.as_view(), name='like-workout'),
]