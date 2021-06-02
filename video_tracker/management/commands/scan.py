from django.core.management.base import BaseCommand, CommandError
from ...utils import scan_new_video_files, remove_phantom_files


class Command(BaseCommand):
    help = "Instantly run a video scan job"

    def handle(self, *args, **options):
        scan_new_video_files()
        remove_phantom_files()
        self.stdout.write(self.style.SUCCESS("SCAN RAN"))
