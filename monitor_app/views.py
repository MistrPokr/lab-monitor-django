from monitor_app.servos import servo
from django.shortcuts import render
from django.http.response import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status

from monitor_app import servos

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
