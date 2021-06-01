import os


def scan_directory_file(directory, extension=".mp4"):
    target_list = []

    with os.scandir(directory) as dir_contents:
        for entry in dir_contents:
            if entry.name.endswith(extension):
                target_list.append({entry.name: os.stat(entry).st_mtime})

    return target_list
