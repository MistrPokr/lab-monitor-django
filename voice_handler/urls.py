from django.urls import path, re_path

from voice_handler import views

urlpatterns = [
    re_path(r"^upload/", views.file_upload_handler),
    re_path(r"^tts/", views.tts_handler),
    re_path(r"^list/", views.voice_list_handler),
    re_path(r"^play/(?P<pk>[0-9]+)/$", views.play_voice_handler)
]
