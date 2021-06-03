from django.shortcuts import render
from django.http import JsonResponse, FileResponse, StreamingHttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from lab_monitor.settings import VIDEO_STORAGE
from .models import VideoModel
from .utils import scan_directory_file


@api_view(["GET"])
def list_video(request):
    if request.method == "GET":
        queryset = VideoModel.objects.all().order_by("-time")
        name_list = list(queryset.values_list("name", "time"))
        return JsonResponse(
            [{"name": _[0], "time": _[1]} for _ in name_list], safe=False
        )


@api_view(["GET"])
def download_video(request, filename):
    if request.method == "GET":
        target_obj = VideoModel.objects.get(name=filename)

        file_handle = open(target_obj.file, "rb")
        # file_handle.close()

        response = FileResponse(
            open(target_obj.file, "rb"), as_attachment=True, content_type="video/mp4"
        )

        # response = StreamingHttpResponse(
        #     streaming_content=file_handle
        # )

        return response
