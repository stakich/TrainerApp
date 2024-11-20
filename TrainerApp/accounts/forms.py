from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm


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
        fields = ['email', 'username']

    def __init__(self, *args, **kwargs):
        super(AppUserCreationForm, self).__init__(*args, **kwargs)
        # Add placeholders to fields
        self.fields['email'].widget.attrs.update({'placeholder': 'Enter your email'})
        self.fields['username'].widget.attrs.update({'placeholder': 'Enter your username'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Enter a strong password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm your password'})
