from django.db import models

# Create your models here.
class DeliveryType(models.Model):
    name=models.CharField(max_Length=32)
    description=models.TextField()
