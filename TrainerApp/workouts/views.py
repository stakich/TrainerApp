from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from django.forms import inlineformset_factory
from TrainerApp.workouts.models import Workout, Exercise, WorkoutExercise
from TrainerApp.workouts.forms import WorkoutAddForm, ExerciseForm, WorkoutEditForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from TrainerApp.accounts.models import UserProfile
from django.views.generic.list import ListView
from django.db.models import Count
from TrainerApp.common.models import Like


class WorkoutCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Workout
    form_class = WorkoutAddForm
    success_url = reverse_lazy('home')
    template_name = 'workouts/create_workout.html'

    def form_valid(self, form, **kwargs):
        workout = form.save(commit=False)
        workout.trainer = self.request.user.userprofile
        workout.save()

        exercises = form.cleaned_data.get('exercises')
        if exercises:
            workout.exercises.set(exercises)

        return redirect(self.success_url)

    def test_func(self):
        if self.request.user.is_authenticated and hasattr(self.request.user, 'userprofile'):
            return self.request.user.userprofile.is_trainer
        return False


class WorkoutEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Workout
    form_class = WorkoutEditForm
    template_name = 'workouts/edit_workout.html'

    def get_success_url(self):
        return reverse_lazy('workout-details', kwargs={'pk': self.object.id})

    def test_func(self):
        workout = self.get_object()
        return self.request.user.is_authenticated and self.request.user.userprofile == workout.trainer


class ExerciseCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Exercise
    form_class = ExerciseForm
    template_name = 'workouts/create_exercise.html'
    success_url = reverse_lazy('create-workout')

    def test_func(self):
        if self.request.user.is_authenticated and hasattr(self.request.user, 'userprofile'):
            return self.request.user.userprofile.is_trainer
        return False


class WorkoutDetailView(DetailView):
    model = Workout
    pk_url_kwarg = 'pk'
    template_name = 'workouts/workout_detail.html'


class WorkoutDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Workout

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.request.user.pk})

    def test_func(self):
        workout = self.get_object()
        return self.request.user.is_authenticated and self.request.user.userprofile.pk == workout.trainer_id


class PopularWorkoutsView(ListView):
    model = Workout
    template_name = 'workouts/popular_workouts.html'
    context_object_name = 'workouts'
    paginate_by = 2

    def get_queryset(self):
        return Workout.objects.annotate(like_count=Count('like')).order_by('-like_count')


class LikedWorkoutsView(LoginRequiredMixin, ListView):
    model = Like
    template_name = 'workouts/liked_workouts.html'
    context_object_name = 'likes'

    def get_queryset(self):
        return Like.objects.filter(user=self.request.user).select_related('to_workout')
