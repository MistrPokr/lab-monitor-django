from background_task import background
from monitor_app.serials.utils import ser


@background
def read_from_serial_task():
    ser.read_data()
