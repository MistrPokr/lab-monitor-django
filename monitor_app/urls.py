from django.urls import path, re_path

from monitor_app import views

urlpatterns = [
    path("servo/<int:angle>", views.servo_control),
]
