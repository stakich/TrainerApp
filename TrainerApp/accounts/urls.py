from django.urls import path
from TrainerApp.accounts import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', views.AppUserLoginView.as_view(), name='login'),
    path('register/', views.AppUserRegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('favorite-trainers/', views.FavoriteTrainersListView.as_view(), name='favorite-trainers'),
    path('approve-trainers/', views.ApproveTrainersListView.as_view(), name='approve-trainers'),
    path('profile/<int:pk>/', views.UserDetailView.as_view(), name='profile-details'),
    path('profile/<int:pk>/edit/', views.UserUpdateView.as_view(), name='profile-edit'),
    path('profile/<int:pk>/delete/', views.UserDeleteView.as_view(), name='profile-delete'),
    path('profile/<int:pk>/edit-profile/', views.ProfileUpdateView.as_view(), name='info-edit'),
]
