from django.shortcuts import redirect
from rest_framework.views import exception_handler
from django.urls import reverse_lazy
from rest_framework.exceptions import NotAuthenticated


class RedirectOnUnAuthMixin:
    def handle_exception(self, exc):
        if isinstance(exc, NotAuthenticated):
            print('zdr')
            return redirect('http://localhost:8000/accounts/login/')
        return super().handle_exception(exc)