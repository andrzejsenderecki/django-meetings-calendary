from django.contrib import admin
from .models import Meeting, DateMeeting, DateRangeMeeting

admin.site.register(Meeting)
admin.site.register(DateMeeting)
admin.site.register(DateRangeMeeting)