import time
from django.core.cache import cache, caches
import RPi.GPIO as GPIO


class Servo:
    def __init__(self):
        self.angle = 90

        GPIO.cleanup()
        self.servopin = 18
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.servopin, GPIO.OUT, initial=False)

    def __del__(self):
        GPIO.cleanup()
        print("Cleanup ran")

    def start(self):
        # Initiates at 180 degrees
        # HAS TO RUN pwm.start()
        self.pwm.start(map_to_cycle(180))

    def spin(self, angle):
        self.pwm = GPIO.PWM(self.servopin, 50)  # 50HZ

        self.angle = angle
        self.pwm.start(map_to_cycle(self.angle))
        time.sleep(0.01)
        self.pwm.stop()
        del self.pwm


def map_to_cycle(input_degree):
    """
    0~180 degrees
    :return: 5~12.5
    """
    degree = 180 - input_degree
    cycle_max = 12.5
    cycle_min = 5
    cycle = cycle_min + (cycle_max - cycle_min) / 180 * degree

    if input_degree < 8:  # Prevents "locked" angles
        cycle = map_to_cycle(8)

    return cycle


def get_servo_angle():
    # s = cache.get("servo")
    return s.angle


def set_servo_angle(angle):
    # s = cache.get("servo")
    s.spin(angle)
    # cache.set("servo", s, None)
