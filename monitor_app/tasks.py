import time

from celery import shared_task
from monitor_app.video_process import stream

vs = stream.VideoStream()


@shared_task
def stream_test():
    v = stream.VideoStream()
    v.start_stream()
    time.sleep(7)
    v.stop_stream()


@shared_task
def start_stream():
    # TODO if already running? 1. Raise exception 2. Check somehow
    # TODO Fetch stdout errors
    vs.start_stream()


@shared_task
def stop_stream():
    vs.stop_stream()
