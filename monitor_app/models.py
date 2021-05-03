from django.db import models


# Create your models here.
class Servo(models.Model):
    angle = models.IntegerField(verbose_name="current servo angle", primary_key=True)

    def __str__(self):
        return f"{str(self.angle)}"
