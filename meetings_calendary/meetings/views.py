from django.shortcuts import render
from .models import Meeting
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import MeetingForm
from django.http import HttpResponseRedirect

@login_required
def meetings(request):
    current_user = User.objects.get(username=request.user)
    meetings_user = Meeting.objects.filter(leader__username=current_user)
    return render(request, 'meetings/meetings_all.html', {'meetings': Meeting.objects.all(),
                                                          'current_user': current_user,
                                                          'meetings_user': meetings_user},)

@login_required
def meeting(request, meeting_id):
    current_user = User.objects.get(username=request.user)
    meeting_user = Meeting.objects.filter(leader__username=current_user)
    return render(request, 'meetings/meeting.html', {'meeting': Meeting.objects.get(id=meeting_id),
                                                     'current_user': current_user,
                                                     'meeting_user': meeting_user},)

@login_required
def new_meeting(request):
    current_user = User.objects.get(username=request.user)
    if request.method == 'POST':
        meeting_form = MeetingForm(request.POST, request.FILES)
        if meeting_form.is_valid():
            new_meeting = meeting_form.save(commit=False)
            new_meeting.leader = request.user
            new_meeting.save()
            return HttpResponseRedirect('/dashboard')
    else:
        meeting_form = MeetingForm()
    return render(request, 'meetings/new_meeting.html', {'meeting_form': meeting_form, 'current_user': current_user})

def home(request):
    return render(request, 'meetings/home.html')