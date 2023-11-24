from django.db import models

class Absentee(models.Model):
    name = models.CharField(max_length=255)
    index_number = models.PositiveIntegerField()
    date = models.DateField(auto_now_add=True)
