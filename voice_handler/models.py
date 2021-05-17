from django.db import models
from django.core.files import File
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

# Create your models here.


class VoiceFile(models.Model):
    text = models.CharField(max_length=100)
    voice_file = models.FileField(upload_to="documents/")
    upload_time = models.DateTimeField(auto_now_add=True)
    synthesized = models.BooleanField()

