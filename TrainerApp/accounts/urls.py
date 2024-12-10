from django.urls import path
from TrainerApp.accounts import views
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('login/', views.AppUserLoginView.as_view(), name='login'),
    path('register/', views.AppUserRegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', views.UserProfileDetailView.as_view(), name='profile-details'),
    path('profile/<int:pk>/edit/', views.UserProfileUpdateView.as_view(), name='profile-edit'),
    path('profile/<int:pk>/edit-profile/', views.ProfileUpdateView.as_view(), name='info-edit'),
    # path('profile/<int:pk>/delete/', views.UserProfileDeleteView.as_view(), name='delete_profile'),
]
