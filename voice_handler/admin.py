from django.contrib import admin
from .models import VoiceFile

# Register your models here.
class VoiceAdmin(admin.ModelAdmin):
    fields = (
        "text",
        "voice_file",
    )


admin.site.register(VoiceFile, VoiceAdmin)
