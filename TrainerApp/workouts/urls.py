from django.urls import path
from TrainerApp.workouts import views

urlpatterns = [
    path('create-workout/', views.WorkoutCreateView.as_view(), name='create-workout'),
    path('create-exercise/', views.ExerciseCreateView.as_view(), name='create-exercise'),
    path('workout-details/<int:pk>/', views.WorkoutDetailView.as_view(), name='workout-details'),
    path('delete/<int:pk>/', views.WorkoutDeleteView.as_view(), name='workout-delete'),
    path('edit/<int:pk>/', views.WorkoutEditView.as_view(), name='workout-edit'),
    path('popular-workouts/', views.PopularWorkoutsView.as_view(), name='popular-workouts'),
    path('liked-workouts/', views.LikedWorkoutsView.as_view(), name='liked-workouts'),

]
