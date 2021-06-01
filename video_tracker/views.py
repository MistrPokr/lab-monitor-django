from django.shortcuts import render
from rest_framework.decorators import api_view
from lab_monitor.settings import VIDEO_STORAGE
from .models import VideoModel
from .utils import scan_directory_file


@api_view(["GET"])
def scan_new_video(request):
    if request.method == "GET":
        queryset = VideoModel.objects.all()
        scanned_file_list = scan_directory_file(directory=VIDEO_STORAGE)
        new_files = set(queryset.values_list("name")) ^ set(scanned_file_list.keys)

        if new_files is not None:
            for f in new_files:
                new_vm = VideoModel(name=f, file=f)
                # new_vm.save()
