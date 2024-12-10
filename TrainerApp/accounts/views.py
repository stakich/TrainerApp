from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.views import LoginView
from TrainerApp.accounts import forms
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth import login
from TrainerApp.accounts.models import UserProfile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import get_object_or_404
from TrainerApp.common.models import Favorite
from django.contrib.auth.models import AnonymousUser


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


class UserProfileDetailView(DetailView):
    model = UserModel
    pk_url_kwarg = 'pk'
    template_name = 'accounts/profile_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['userprofile'] = self.object.userprofile
        if isinstance(self.request.user, AnonymousUser):
            is_favorited = False

        else:
            is_favorited = Favorite.objects.filter(user=self.request.user, trainer=self.object.userprofile).exists()

        context['is_favorited'] = is_favorited
        return context


class UserProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = UserModel
    form_class = forms.UserEditForm
    template_name = 'accounts/profile_details_edit.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        user = get_object_or_404(UserModel, pk=self.kwargs['pk'])
        return self.request.user == user


class ProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = UserProfile
    form_class = forms.ProfileEditForm
    template_name = 'accounts/profile_personal_info_edit.html'

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.object.user.pk})

    def test_func(self):
        profile_being_edited = self.get_object()
        print(profile_being_edited)
        print(self.request.user.userprofile)
        return self.request.user.userprofile == profile_being_edited
