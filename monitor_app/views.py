from django.shortcuts import render
from django.http.response import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status

from monitor_app import tasks
from monitor_app.servos import servos

# Create your views here.


@api_view(["GET", "POST"])
def servo_control(request, angle):
    if request.method == "GET":
        angle = servos.get_servo_angle()
        return JsonResponse({"angle": angle})

    if request.method == "POST":
        servos.set_servo_angle(angle)
        return JsonResponse({"message": f"Servo angle set to {angle}"})
