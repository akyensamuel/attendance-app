from django.db import models

class Absentee(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.PositiveIntegerField()
    residential_address = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
