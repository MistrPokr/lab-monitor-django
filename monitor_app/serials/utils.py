import subprocess
import time

import serial

from monitor_app.models import DHTDataModel


class DHTSerial(serial.Serial):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.baudrate = 9600
        self.timeout = 5
        # Port subject to change
        self.port = "/dev/ttyUSB0"
        self.buffer = b""

        self.readings = {
            "temperature_c": -1.0,  # Celsius
            "humidity": -1.0,
        }
        self.open()

    def set_port(self, port):
        self.port = port

    def read_data(self):
        while True:
            for _ in range(9):
                try: 
                    self.buffer = self.readline()
                except serial.serialutil.SerialException: 
                    return
                self.interpret_readings(self.buffer)
                if _ == 8:
                    self.save_readings()
                    print(self.readings)
                    time.sleep(1)

    def interpret_readings(self, buffer_string):
        """
        Pattern:
        b'\n'
        b'\r\n'
        b'Read sensor: Checksum error\r\n'
        b'Humidity (%): 54.00\r\n'
        b'Temperature (oC): 32.00\r\n'
        b'Temperature (oF): 89.60\r\n'
        b'Temperature (K): 305.15\r\n'
        b'Dew Point (oC): 21.54\r\n'
        b'Dew PointFast (oC): 21.51\r\n'
        :param buffer_string:
        :return:
        """
        # Converts to string & remove b' prefix
        reading_string = str(buffer_string).strip("b'")
        try:
            i = reading_string.index(".")
        except ValueError:  # Not found
            return
        else:
            data = float(reading_string[i - 2 : i + 2])
            type_string = ""

            if "Humidity" in reading_string:
                type_string = "humidity"
            elif "Temperature (oC)" in reading_string:
                type_string = "temperature_c"

            self.readings[type_string] = data
            return [type_string, data]

    def save_readings(self):
        data_records = DHTDataModel.objects.count()

        if data_records > 100:
            last_record = DHTDataModel.objects.all()[0]
            last_record.delete()

        DHTDataModel.objects.create(
            temperature=self.readings["temperature_c"],
            humidity=self.readings["humidity"],
        )


def list_ports():
    task = subprocess.run(
        [
            "python",
            "-m",
            "serial.tools.list_ports",
        ],
        capture_output=True,
    )

    encoding = "utf-8"
    port_info = {
        "stdout": task.stdout.decode(encoding),
        "stderr": task.stderr.decode(encoding).strip("\n"),
    }

    return port_info


ser = DHTSerial()
