from django import forms
from .models import Meeting
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField

class MeetingForm(forms.ModelForm):
    date = forms.DateField(widget=forms.SelectDateWidget())
    class Meta:
        model = Meeting
        fields = ('client', 'place', 'date', 'topic', 'description',)

