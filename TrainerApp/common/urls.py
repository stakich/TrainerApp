from django.urls import path
from TrainerApp.common import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home')
]