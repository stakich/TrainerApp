from django.urls import path
from TrainerApp.accounts import views


urlpatterns = [
    path('login/', views.AppUserLoginView.as_view(), name='login'),
    path('register/', views.AppUserRegisterView.as_view(), name='register'),
]
