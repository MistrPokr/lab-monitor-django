from background_task import background
from lab_monitor.settings import VIDEO_STORAGE

from .utils import scan_new_video_files, remove_phantom_files
from .models import VideoModel


@background()
def video_maintenance_job():
    scan_new_video_files()
    remove_phantom_files()
