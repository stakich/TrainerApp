from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView
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
from django.contrib import messages
from django.db.models import Q

# Create your views here.

UserModel = get_user_model()


class AppUserLoginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = forms.CustomAuthenticationForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().get(request, *args, **kwargs)


class AppUserRegisterView(CreateView):
    form_class = forms.AppUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('home')
    model = UserModel

    def form_valid(self, form):
        response = super().form_valid(form)

        login(self.request, self.object)

        return response


class UserDetailView(DetailView):
    model = UserModel
    pk_url_kwarg = 'pk'
    template_name = 'accounts/profile_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['userprofile'] = self.object.userprofile
        context['is_authenticated'] = self.request.user.is_authenticated
        if isinstance(self.request.user, AnonymousUser):
            is_favorited = False

        else:
            is_favorited = Favorite.objects.filter(user=self.request.user, trainer=self.object.userprofile).exists()

        context['is_favorited'] = is_favorited
        return context


class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
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

    def get_template_name(self):
        if self.request.user.is_authenticated:
            return 'accounts/profile_personal_info_edit.html'
        return 'accounts/login.html'

    def form_valid(self, form):
        profile = form.save(commit=False)
        profile.is_approved = self.object.is_approved
        profile.save()
        return redirect('home')

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.object.user.pk})

    def test_func(self):
        profile_being_edited = self.get_object()
        return self.request.user.userprofile == profile_being_edited


class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = UserModel
    template_name = "accounts/user_confirm_delete.html"
    success_url = reverse_lazy("home")
    form_class = forms.UserDeleteForm

    def test_func(self):
        user = self.get_object()
        return self.request.user.is_superuser or self.request.user == user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.method == "POST":
            context["form"] = self.form_class(self.request.POST, instance=self.object)
        else:
            context["form"] = self.form_class(instance=self.object)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.form_class(request.POST, instance=self.object)
        if form.is_valid():
            return super().post(request, *args, **kwargs)
        return self.render_to_response(self.get_context_data(form=form))


class FavoriteTrainersListView(LoginRequiredMixin, ListView):
    model = Favorite
    template_name = 'accounts/favorite_trainers_list.html'
    context_object_name = 'favorites'
    paginate_by = 3

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user).select_related('trainer')


class ApproveTrainersListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = UserProfile
    template_name = 'accounts/trainer_approvals_list.html'
    context_object_name = 'trainer_approvals'
    paginate_by = 10

    def get_queryset(self):
        print(UserProfile.objects.filter(
            (Q(is_approved=False) | Q(is_approved=None)) & Q(experience_years__isnull=False)
        ))
        return UserProfile.objects.filter(
            (Q(is_approved=False) | Q(is_approved=None)) & Q(experience_years__isnull=False)
        )

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['trainers'] = UserProfile.objects.filter(
            (Q(is_approved=False) | Q(is_approved=None)) & Q(experience_years__isnull=False)
        ).count() > 0
        return context

    def post(self, request, *args, **kwargs):
        trainer_id = request.POST.get('trainer_id')
        action = request.POST.get('action')

        if trainer_id and action:
            try:
                trainer = UserProfile.objects.get(id=trainer_id)
                if action == 'approve':
                    trainer.is_approved = True
                    trainer.is_trainer = True
                    trainer.save()
                elif action == 'reject':
                    trainer.is_approved = None
                    trainer.save()
            except UserProfile.DoesNotExist:
                messages.error(request, "Trainer not found.")
        else:
            messages.error(request, "Invalid action or trainer ID.")

        return redirect('approve-trainers')
