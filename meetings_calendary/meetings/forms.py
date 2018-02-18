from django import forms
from .models import Meeting, DateMeeting, DateRangeMeeting, FindMeeting
from django.forms.fields import DateField
from django.contrib.admin.widgets import AdminDateWidget

class MeetingForm(forms.ModelForm):
    date = forms.DateField(widget=forms.SelectDateWidget())
    class Meta:
        model = Meeting
        fields = ('client', 'place', 'date', 'hour', 'topic', 'description', 'attachment')

class DateMeetingForm(forms.ModelForm):
    date_meeting = forms.DateField(widget=forms.SelectDateWidget())
    class Meta:
        model = DateMeeting
        fields = ('date_meeting',)

class DateRangeMeetingForm(forms.ModelForm):
    date_meeting_start = forms.DateField(widget=forms.SelectDateWidget())
    date_meeting_end = forms.DateField(widget=forms.SelectDateWidget())
    class Meta:
        model = DateRangeMeeting
        fields = ('date_meeting_start', 'date_meeting_end',)

class FindMeetingForm(forms.ModelForm):
    class Meta:
        model = FindMeeting
        fields = ('find_meeting',)

class SendMeetingForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = Meeting
        fields = ('email', 'client', 'place', 'date', 'hour', 'topic', 'description')

