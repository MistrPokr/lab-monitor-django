import os
from pathlib import Path
from .models import VideoModel
from lab_monitor.settings import VIDEO_STORAGE


def scan_new_video_files(directory=VIDEO_STORAGE):
    print("SCANNING")
    queryset = VideoModel.objects.all()
    new_file_list = scan_directory_file(directory=directory)

    new_files = set([list(_)[0] for _ in queryset.values_list("name")]) ^ set(
        list(new_file_list)
    )

    if new_files is not None:
        for f in new_files:
            file_path = VIDEO_STORAGE + f
            new_vm = VideoModel(name=f, file=file_path)
            new_vm.save()


def scan_directory_file(directory=VIDEO_STORAGE, extension=".mp4"):
    target_list = {}

    with os.scandir(directory) as dir_contents:
        for entry in dir_contents:
            if entry.name.endswith(extension):
                target_list[entry.name] = os.stat(entry).st_mtime

    return target_list


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
