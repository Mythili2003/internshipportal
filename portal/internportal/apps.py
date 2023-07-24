from django.apps import AppConfig


class InternportalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'internportal'




    def ready(self):
        import internportal.signals 
