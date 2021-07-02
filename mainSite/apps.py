from django.apps import AppConfig


class MainsiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mainSite'

    def ready(self) -> None:
        from . import signals
        