from django import forms
from .models import Meeting, DateMeeting
from django.forms.fields import DateField
from django.contrib.admin.widgets import AdminDateWidget

class MeetingForm(forms.ModelForm):
    date = forms.DateField(widget=forms.SelectDateWidget())
    class Meta:
        model = Meeting
        fields = ('client', 'place', 'date', 'hour', 'topic', 'description',)

class DateMeetingForm(forms.ModelForm):
    date_meeting = forms.DateField(widget=forms.SelectDateWidget())
    class Meta:
        model = DateMeeting
        fields = ('date_meeting',)

