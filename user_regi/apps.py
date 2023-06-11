from django.apps import AppConfig

class UserRegiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_regi'

    def ready(self):
        import user_regi.signals