from django.db import models


class DHTDataModel(models.Model):
    temperature = models.FloatField(default=-1.0)
    humidity = models.FloatField(default=-1.0)
