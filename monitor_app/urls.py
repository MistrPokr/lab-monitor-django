from django.urls import path, re_path

from monitor_app import views

urlpatterns = [
    path("stream", views.stream_request),
]
