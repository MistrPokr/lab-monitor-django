from django.apps import AppConfig


class MonitorAppConfig(AppConfig):
    name = "monitor_app"

    def ready(self):
        from monitor_app.tasks import read_from_serial_task
        from background_task.models import Task

        read_from_serial_task()
