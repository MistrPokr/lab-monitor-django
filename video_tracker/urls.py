from django.urls import path, re_path
from .views import list_video

urlpatterns = [
    path("list/", list_video),
]
