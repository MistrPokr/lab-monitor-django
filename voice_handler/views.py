from django.shortcuts import render
from django.http import JsonResponse
from django.core.files import File
from django.core.files.base import ContentFile
from django.conf import settings

from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

from voice_handler import models
from voice_handler.audio import synth, playback


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
        req_text = request.data["text"]
        req_play = request.data["play"]

        # if text in new request matches existing ones
        existing_voice_querylist = models.VoiceFile.objects.filter(text__exact=req_text)

        if len(existing_voice_querylist) > 0:
            if req_play:
                playback.play_audio(existing_voice_querylist[0].voice_file.path)
            return Response(status=204)

        else:
            result = synth.tts(synth_text=req_text)

            file_obj = ContentFile(result)
            file_obj.name = "audio.mp3"

            file = File(file_obj)

            new_voice_obj = models.VoiceFile(
                text=req_text,
                voice_file=file,
                synthesized=True,
            )
            new_voice_obj.save()

            if req_play:
                playback.play_audio(new_voice_obj.voice_file.path)

            return Response(status=204)


@api_view(["GET"])
def voice_list_handler(request):
    if request.method == "GET":
        queryset = models.VoiceFile.objects.all()
        values = queryset.values("id", "text")
        return JsonResponse(list(values), safe=False)


@api_view(["POST", "DELETE"])
def voice_file_handler(request, pk):
    voice_id = int(pk)
    voice_obj = models.VoiceFile.objects.get(pk=voice_id)
    if request.method == "POST":
        playback.play_audio(voice_obj.voice_file.path)
        return Response(status=200)
    if request.method == "DELETE":
        voice_obj.voice_file.delete()
        voice_obj.delete()
        return Response(status=200)
