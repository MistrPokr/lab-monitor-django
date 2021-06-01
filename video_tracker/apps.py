from django.apps import AppConfig


class VideoTrackerConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "video_tracker"

    def ready(self):
        from background_task.models import Task
        # from .tasks import scan_new_video
        #
        # scan_new_video(repeat=Task.HOURLY)
