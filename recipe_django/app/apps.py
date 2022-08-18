from django.apps import AppConfig
from django.db.models.signals import  post_save


class CustomAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'recipe_django.app'
    
    def ready(self):
        import recipe_django.app.signals