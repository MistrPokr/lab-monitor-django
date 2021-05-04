from django.core.cache import cache, caches
import RPi.GPIO as GPIO
import monitor_app.servos


class Servo:
    def __init__(self):
        self.angle = 90

        GPIO.cleanup()
        self.servopin = 18
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.servopin, GPIO.OUT, initial=False)
        self.pwm = GPIO.PWM(self.servopin, 50)  # 50HZ

    def __del__(self):
        self.pwm.stop()
        GPIO.cleanup()
        print("Cleanup ran")

    def start(self):
        # Initiates at 180 degrees
        # HAS TO RUN pwm.start()
        self.pwm.start(map_to_cycle(180))

    def spin(self, angle):
        self.angle = angle
        cycle = map_to_cycle(angle)
        self.pwm.ChangeDutyCycle(cycle)


def map_to_cycle(degree):
    """
    0~180 degrees
    :return: 5~12.5
    """
    degree = 180 - degree
    cycle_max = 12.5
    cycle_min = 5
    cycle = cycle_min + (cycle_max - cycle_min) / 180 * degree
    return cycle


def get_servo_angle():
    # s = cache.get("servo")
    return s.angle


def set_servo_angle(angle):
    # s = cache.get("servo")
    s.spin(angle)
    # cache.set("servo", s, None)
