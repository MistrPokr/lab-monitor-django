import subprocess

from monitor_app.servos import servo
from django.shortcuts import render
from django.http.response import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status

from monitor_app import servos
from monitor_app.serials.utils import ser
from monitor_app.models import DHTDataModel

# Create your views here.


@api_view(["GET", "POST"])
def servo_control(request, angle=None):
    if request.method == "GET":
        # angle = servos.servo.get_servo_angle()
        angle = servos.s.angle
        return JsonResponse({"angle": angle})

    if request.method == "POST":
        angle = int(angle)
        # servos.servo.set_servo_angle(angle)
        servos.s.spin(angle)
        return JsonResponse({"message": f"Servo angle set to {angle}"})


@api_view(["GET"])
def dht11_view(request):
    queryset = DHTDataModel.objects.all().order_by("-time")
    last_dht_reading = queryset[0]
    if request.method == "GET":
        return JsonResponse(
            {
                "temperature": last_dht_reading.temperature,
                "humidity": last_dht_reading.humidity,
                "time": last_dht_reading.time,
                "id": last_dht_reading.id,
            }
        )


@api_view(["GET", "POST"])
def live_control_view(request):
    if request.method == "GET":
        task = subprocess.run(
            [
                "systemctl",
                "is-active",
                "motion.service",
            ],
            capture_output=True,
        )
        encoding = "utf-8"
        output_info = {
            "stdout": task.stdout.decode(encoding).strip("\n"),
            "stderr": task.stderr.decode(encoding).strip("\n"),
        }

        status = 0
        if output_info["stdout"] == "active":
            status = 1

        return JsonResponse({"status": status})

    if request.method == "POST":
        task = subprocess.run(
            [
                "sudo",
                "systemctl",
                "restart",
                "motion.service",
            ],
            capture_output=True,
        )

        encoding = "utf-8"
        output_info = {
            "stdout": task.stdout.decode(encoding),
            "stderr": task.stderr.decode(encoding).strip("\n"),
        }

        return JsonResponse(output_info)
