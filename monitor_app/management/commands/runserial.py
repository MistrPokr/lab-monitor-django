from django.core.management.base import BaseCommand, CommandError
from monitor_app.serials.utils import ser


class Command(BaseCommand):
    help = "Start reading from serial port"

    def handle(self, *args, **options):
        ser.read_data()
