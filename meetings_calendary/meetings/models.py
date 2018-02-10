from django.db import models
from django.conf import settings

class Meeting(models.Model):
    client = models.CharField(max_length=150)
    place = models.CharField(max_length=150)
    date = models.CharField(max_length=10)
    topic = models.CharField(max_length=150)
    description = models.TextField()
    leader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.client


