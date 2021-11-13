from django.apps import AppConfig


class SevenpmConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Sevenpm'
    def ready(self):
        import Sevenpm.signals
        
