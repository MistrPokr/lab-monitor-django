from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from lab_monitor.settings import VIDEO_STORAGE
from .models import VideoModel
from .utils import scan_directory_file


@api_view(["GET"])
def list_video(request):
    if request.method == "GET":
        queryset = VideoModel.objects.all()
        return JsonResponse(list(queryset.values_list("name")), safe=False)
