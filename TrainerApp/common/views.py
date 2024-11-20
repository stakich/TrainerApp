from django.shortcuts import render
from TrainerApp.accounts.models import UserProfile
from django.views import generic
# Create your views here.


class HomePage(generic.ListView):
    template_name = 'common/homepage.html'
    context_object_name = 'all_trainers'
    paginate_by = 5

    def get_queryset(self):
        queryset = UserProfile.objects.filter(user__is_trainer=True)

        return queryset