from django.apps import AppConfig

class NotificationsConfig(AppConfig):
    name = 'notifications'

    def ready(self):
        # use a relative import so it works regardless of project name
        from . import signals
