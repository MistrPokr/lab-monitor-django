from django.db import models
from django.core.files.storage import FileSystemStorage
from lab_monitor.settings import VIDEO_STORAGE

video_fs = FileSystemStorage(location=VIDEO_STORAGE)


class VideoModel(models.Model):
    name = models.CharField(max_length=50)
    file = models.FilePathField()
    time = models.DateTimeField()
