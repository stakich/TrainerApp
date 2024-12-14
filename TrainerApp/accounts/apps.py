from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'TrainerApp.accounts'

    def ready(self):
        import TrainerApp.accounts.signals