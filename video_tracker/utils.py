import os
from tzlocal import get_localzone
from datetime import datetime, timedelta
from pathlib import Path
from .models import VideoModel
from lab_monitor.settings import VIDEO_STORAGE, STALE_LIMIT


def time_diff(time0, time1, tz=None):
    tz = get_localzone()
    return time1 - time0


def scan_new_video_files(directory=VIDEO_STORAGE):
    print("SCANNING")
    queryset = VideoModel.objects.all()
    new_file_list = scan_directory_file(directory=directory)

    new_files = set(list(new_file_list)) - set(
        [list(_)[0] for _ in queryset.values_list("name")]
    )

    if new_files is not None:
        for f in new_files:
            file_path = Path(directory) / f
            create_time = datetime.fromtimestamp(
                os.stat(file_path).st_ctime, tz=get_localzone()
            )

            new_vm = VideoModel(name=f, file=file_path, time=create_time)
            new_vm.save()


def scan_directory_file(directory=VIDEO_STORAGE, extension=".mp4"):
    target_list = {}

    with os.scandir(directory) as dir_contents:
        for entry in dir_contents:
            if entry.name.endswith(extension):
                target_list[entry.name] = os.stat(entry).st_mtime

    return target_list


def remote_stale_videos(directory=VIDEO_STORAGE):
    with os.scandir(directory) as dir_contents:
        for entry in dir_contents:
            delta = time_diff(
                datetime.fromtimestamp(os.stat(entry).st_mtime, tz=get_localzone()),
                datetime.now(tz=get_localzone()),
            )
            if delta > STALE_LIMIT:
                os.remove(entry)


def remove_phantom_files(directory=VIDEO_STORAGE):
    phantom_list = []

    db_list = [_[0] for _ in VideoModel.objects.all().values_list("name")]

    with os.scandir(directory) as dir_contents:
        existing_list = [_.name for _ in dir_contents]
        for _ in db_list:
            if _ not in existing_list:
                phantom_list.append(_)

    phantoms_query = VideoModel.objects.filter(name__in=phantom_list)
    phantoms_query.delete()


def delete_video_file(filename, directory=VIDEO_STORAGE):
    p = Path(directory)
    delete_file = p / filename
    if delete_file.exists():
        delete_file.unlink(missing_ok=True)
    pass
