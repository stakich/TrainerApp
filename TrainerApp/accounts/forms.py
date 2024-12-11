from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from TrainerApp.accounts.models import UserProfile


UserModel = get_user_model()


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self,  *args, **kwargs):
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({'placeholder': 'Enter your username'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Enter your password'})


class AppUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserModel


class AppUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ['email', 'username', 'first_name', 'last_name']


class UserEditForm(forms.ModelForm):

    class Meta:
        model = UserModel
        fields = ('email', 'username', 'first_name', 'last_name')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'location', 'specialization', 'experience_years', 'profile_picture']

    def clean_experience_years(self):
        experience_years = self.cleaned_data['experience_years']
        if experience_years is None or experience_years < 0:
            raise forms.ValidationError('Invalid number input. Cannot be negative or empty')
        return experience_years


class UserDeleteForm(forms.ModelForm):
    confirm = forms.BooleanField(required=True, label="I confirm the deletion of this user.")

    class Meta:
        model = UserModel
        fields = []

    def clean(self):
        cleaned_data = super().clean()
        confirm = cleaned_data.get("confirm")
        if not confirm:
            raise forms.ValidationError("You must confirm the deletion.")
        return cleaned_data
    