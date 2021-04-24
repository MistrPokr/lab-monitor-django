from django.shortcuts import render
from django.http.response import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status

from monitor_app import tasks


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
        # tasks.stream_test.delay()
        tasks.start_stream.delay()
        return JsonResponse(
            {"message": "Video streaming started. "}
        )

    if request.method == "POST":
        tasks.stop_stream.delay()

        # TODO To reliably confirm termination?
        return JsonResponse({
            "message": "Video streaming stopped. "
        })
