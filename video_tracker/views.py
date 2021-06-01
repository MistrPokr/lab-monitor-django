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
        return JsonResponse(list(queryset.values_list('name')), safe=False)



@api_view(["GET"])
def scan_new_video(request):
    if request.method == "GET":
        queryset = VideoModel.objects.all()
        new_file_list = scan_directory_file(directory=VIDEO_STORAGE)

        new_files = set([list(_)[0] for _ in queryset.values_list("name")]) ^ set(
            list(new_file_list)
        )

        if new_files is not None:
            for f in new_files:
                file_path = VIDEO_STORAGE + f
                new_vm = VideoModel(name=f, file=file_path)
                new_vm.save()

    return Response(status=200)
