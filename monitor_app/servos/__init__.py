from django.core.cache import cache, caches
from .servo import Servo

s = Servo()
s.start()
# servo_obj_cache = cache.set("servo", servo, None)
