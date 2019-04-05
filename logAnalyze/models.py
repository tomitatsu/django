from django.db import models

class Log(models.Model):
    url = models.CharField(max_length=40)
    STATUS_CHOICE = ((1, 'ON'), (2, 'OFF'))
    status = models.IntegerField(choices=STATUS_CHOICE)
