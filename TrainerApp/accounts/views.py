from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.views import LoginView
from TrainerApp.accounts import forms
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth import login
# Create your views here.

UserModel = get_user_model()


class AppUserLoginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = forms.CustomAuthenticationForm



class AppUserRegisterView(CreateView):
    form_class = forms.AppUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('home')
    model = UserModel

    def form_valid(self, form):
        response = super().form_valid(form)

        login(self.request, self.object)

        return response