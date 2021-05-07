import tempfile

from django.shortcuts import render
from django.http import JsonResponse
from django.core.files import File
from django.core.files.base import ContentFile

from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

from voice_handler import models
from voice_handler.tts import voice_synth


@api_view(["GET", "POST"])
@parser_classes([MultiPartParser])
def file_upload_handler(request, format=None):
    if request.method == "GET":
        return JsonResponse({"message": ""})

    if request.method == "POST":
        # file_uploaded = request.FILES.get("file_uploaded")
        # content_type = file_uploaded.content_type
        # return JsonResponse({"message": f"Uploaded file with type {content_type}"})
        file_obj = request.data["file"]
        file_name = request.data["filename"]

        file = File(file_obj)

        new_voice_obj = models.VoiceFile(
            text=file_name,
            voice_file=file,
            synthesized=False,
        )
        new_voice_obj.save()

        return Response(status=204)


@api_view(["POST"])
def tts_handler(request):
    if request.method == "POST":
        text = request.data["text"]

        result = voice_synth.tts(synth_text=text)

        # file_obj = tempfile.NamedTemporaryFile(mode="w+b", suffix=".mp3")
        # file_obj.write(result)

        file_obj = ContentFile(result)
        file_obj.name = 'audio.mp3'

        file = File(file_obj)

        new_voice_obj = models.VoiceFile(
            text=text,
            voice_file=file,
            synthesized=True,
        )
        new_voice_obj.save()

        return Response(status=204)
