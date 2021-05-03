from django.shortcuts import render
from django.http.response import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status

from monitor_app import tasks
from monitor_app.video_process import stream


# Create your views here.
@api_view(["GET", "POST"])
def stream_request(request):
    """
    GET: Start stream asynchronously

    POST: Stop stream asynchronously
    :param request:
    :return:
    """
    if request.method == "GET":
        pid = 0
        if not stream.vs.process:
            stream.vs.start_stream()
            pid = stream.vs.get_pid()
            return JsonResponse(
                {"message": "Video streaming started. ", "pid": str(pid)}
            )
        else:
            return JsonResponse(
                {"message": "A stream process is already running! ", "pid": str(pid)}
            )

    if request.method == "POST":
        stream.vs.stop_stream()
        stream.vs.process = None

        # TODO Handle ValueError write to closed file
        return JsonResponse({"message": "Video streaming stopped. ", "pid": None})
