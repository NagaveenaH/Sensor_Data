from django.db import models

# Create your models here.
class store_extract(models.Model):
    reading=models.FloatField()
    timestamp=models.BigIntegerField()
    sensor_type=models.CharField(max_length=100)
