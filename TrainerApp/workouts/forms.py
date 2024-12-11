from django import forms
from django.forms import modelformset_factory, inlineformset_factory
from TrainerApp.workouts.models import Workout, Exercise


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['name', 'description', 'sets', 'reps']

    def clean_name(self):
        name = self.cleaned_data['name'].lower()
        if Exercise.objects.filter(name=name).first():
            raise forms.ValidationError("Exercise with this name already exists.")
        return name

    def clean_sets(self):
        sets = self.cleaned_data['sets']
        if sets <= 0:
            raise forms.ValidationError("Sets must be a positive number.")
        return sets

    def clean_reps(self):
        reps = self.cleaned_data['reps']
        if reps <= 0:
            raise forms.ValidationError("Reps must be a positive number.")
        return reps


class WorkoutBaseForm(forms.ModelForm):
    class Meta:
        model = Workout
        exclude = ['trainer']


class WorkoutAddForm(WorkoutBaseForm):
    pass


class WorkoutEditForm(WorkoutBaseForm):
    def __init__(self,*args,  **kwargs):
        super().__init__(*args, **kwargs)


