from django.apps import AppConfig


class DwfjobConfig(AppConfig):
    name = 'dwfjob'

    def ready(self):
        import dwfjob.signals
