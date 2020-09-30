from django.apps import AppConfig


class ApiConfig(AppConfig):
    name = 'api'

    def ready(self):
        from .matching import GazetteerCache
        GazetteerCache.get_latest()
