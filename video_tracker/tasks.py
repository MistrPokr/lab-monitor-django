from background_task import background
from lab_monitor.settings import VIDEO_STORAGE

from .utils import scan_directory_file
from .models import VideoModel


# @background
# def scan_new_video():
#     queryset = VideoModel.objects.all()
#     scanned_file_list = scan_directory_file(directory=VIDEO_STORAGE)
#     new_files = set(queryset.values_list("name")) ^ set(scanned_file_list.keys)
#
#     if new_files is not None:
#         for f in new_files:
#             new_vm = VideoModel(name=f, file=f)
