from django.db import models

class Washing_Payment(models.Model):
    name = models.CharField(max_length=256)
    address = models.TextField()
    pincode = models.CharField(max_length=6)
    amount = models.FloatField(max_length=256)
