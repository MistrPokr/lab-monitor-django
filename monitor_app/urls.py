from django.urls import path, re_path

from monitor_app import views

urlpatterns = [
    path("servo/", views.servo_control),
    re_path(r"^servo/(?P<angle>[0-9]+)/$", views.servo_control),
]
