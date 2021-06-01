from django.urls import path, re_path
from .views import scan_new_video

urlpatterns = [
    path("scan/", scan_new_video),
]
