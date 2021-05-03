from django.core.cache import cache, caches


class Servo:
    def __init__(self):
        self.angle = 90

    def set_angle(self, new_angle):
        if True:
            # Upon success (judged from lower level function returns)
            self.angle = new_angle
            return True
        elif False:
            return False


def get_servo_angle():
    s = cache.get("servo")
    return s.angle


def set_servo_angle(angle):
    s = cache.get("servo")
    s.set_angle(angle)
    cache.set("servo", s, None)


servo = Servo()
servo_obj_cache = cache.set("servo", servo, None)
