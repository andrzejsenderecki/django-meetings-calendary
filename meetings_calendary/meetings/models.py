from django.db import models
from django.conf import settings

class Meeting(models.Model):
    client = models.CharField(max_length=150)
    place = models.CharField(max_length=150)
    date = models.CharField(max_length=50)
    hour = models.CharField(max_length=50)
    topic = models.CharField(max_length=150)
    description = models.TextField()
    leader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.client

class DateMeeting(models.Model):
    date_meeting = models.CharField(max_length=50)
    leader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.date_meeting

class DateRangeMeeting(models.Model):
    date_meeting_start = models.CharField(max_length=50)
    date_meeting_end = models.CharField(max_length=50)
    leader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.date_meeting_start


