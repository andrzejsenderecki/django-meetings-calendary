from django.shortcuts import render
from .models import Meeting, DateMeeting, DateRangeMeeting, FindMeeting
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import MeetingForm, DateMeetingForm, DateRangeMeetingForm, FindMeetingForm, SendMeetingForm
from django.http import HttpResponseRedirect
from django.utils import timezone
import datetime
from django.core.mail import send_mail

@login_required
def meetings(request):
    current_user = User.objects.get(username=request.user)
    meetings_user = Meeting.objects.filter(leader__username=current_user)
    return render(request, 'meetings/meetings_all.html', {'current_user': current_user,
                                                          'meetings_user': meetings_user},)

@login_required
def meeting(request, meeting_id):
    current_user = User.objects.get(username=request.user)

    return render(request, 'meetings/meeting.html', {'meeting': Meeting.objects.get(id=meeting_id),
                                                     'current_user': current_user,})

@login_required
def today_meetings(request):
    current_user = User.objects.get(username=request.user)
    start_date = datetime.date.today()
    end_date = datetime.date.today()
    meetings_user = Meeting.objects.filter(leader__username=current_user, date__range=(start_date, end_date))

    return render(request, 'meetings/meetings_all.html', {'current_user': current_user,
                                                          'meetings_user': meetings_user})

@login_required
def date_meetings(request):
    current_user = User.objects.get(username=request.user)
    DateMeeting.objects.filter(leader__username=current_user).delete()
    if request.method == 'POST':
        date_meeting_form = DateMeetingForm(request.POST)
        if date_meeting_form.is_valid():
            date_meeting = date_meeting_form.save(commit=False)
            date_meeting.leader = request.user
            date_meeting.save()
            return HttpResponseRedirect('/date_meetings_all')
    else:
        date_meeting_form = DateMeetingForm()

    return render(request, 'meetings/date_meeting.html', {'date_meeting_form': date_meeting_form,
                                                          'current_user': current_user,})

@login_required
def date_meetings_all(request):
    current_user = User.objects.get(username=request.user)
    date_user = DateMeeting.objects.get(leader__username=current_user)
    date_meetings_user = Meeting.objects.filter(leader__username=current_user, date=date_user)

    return render(request, 'meetings/date_meetings_all.html', {'current_user': current_user,
                                                               'date_meetings_user': date_meetings_user,})

@login_required
def date_range_meetings(request):
    current_user = User.objects.get(username=request.user)
    DateRangeMeeting.objects.filter(leader__username=current_user).delete()
    if request.method == 'POST':
        date_range_meeting_form = DateRangeMeetingForm(request.POST)
        if date_range_meeting_form.is_valid():
            date_range_meeting = date_range_meeting_form.save(commit=False)
            date_range_meeting.leader = request.user
            date_range_meeting.save()
            return HttpResponseRedirect('/date_range_meetings_all')
    else:
        date_range_meeting_form = DateRangeMeetingForm()

    return render(request, 'meetings/date_range_meeting.html', {'date_range_meeting_form': date_range_meeting_form,
                                                          'current_user': current_user,})

@login_required
def date_range_meetings_all(request):
    current_user = User.objects.get(username=request.user)
    date_user = DateRangeMeeting.objects.get(leader__username=current_user)
    start_date = date_user.date_meeting_start
    end_date = date_user.date_meeting_end
    date_meetings_user = Meeting.objects.filter(leader__username=current_user, date__range=(start_date, end_date))

    return render(request, 'meetings/date_range_meetings_all.html', {'current_user': current_user,
                                                               'date_meetings_user': date_meetings_user,})

@login_required
def find_meetings(request):
    current_user = User.objects.get(username=request.user)
    FindMeeting.objects.filter(leader__username=current_user).delete()
    if request.method == 'POST':
        find_meeting_form = FindMeetingForm(request.POST)
        if find_meeting_form.is_valid():
            find_meeting = find_meeting_form.save(commit=False)
            find_meeting.leader = request.user
            find_meeting.save()
            return HttpResponseRedirect('/find_meetings_all')
    else:
        find_meeting_form = FindMeetingForm()

    return render(request, 'meetings/find_meetings.html', {'find_meeting_form': find_meeting_form,
                                                          'current_user': current_user,})

@login_required
def find_meetings_all(request):
    current_user = User.objects.get(username=request.user)
    find_user = FindMeeting.objects.get(leader__username=current_user)
    find_meetings_user_client = Meeting.objects.filter(leader__username=current_user, client__contains=find_user)
    find_meetings_user_place = Meeting.objects.filter(leader__username=current_user, place__contains=find_user)
    find_meetings_user_date = Meeting.objects.filter(leader__username=current_user, date__contains=find_user)
    find_meetings_user_hour = Meeting.objects.filter(leader__username=current_user, hour__contains=find_user)
    find_meetings_user_topic = Meeting.objects.filter(leader__username=current_user, topic__contains=find_user)
    find_meetings_user_description = Meeting.objects.filter(leader__username=current_user, description__contains=find_user)

    return render(request, 'meetings/find_meetings_all.html', {'current_user': current_user,
                                                               'find_meetings_user_client': find_meetings_user_client,
                                                               'find_meetings_user_place': find_meetings_user_place,
                                                               'find_meetings_user_date': find_meetings_user_date,
                                                               'find_meetings_user_hour': find_meetings_user_hour,
                                                               'find_meetings_user_topic': find_meetings_user_topic,
                                                               'find_meetings_user_description': find_meetings_user_description})

@login_required
def new_meeting(request):
    current_user = User.objects.get(username=request.user)
    if request.method == 'POST':
        meeting_form = MeetingForm(request.POST, request.FILES)
        if meeting_form.is_valid():
            new_meeting = meeting_form.save(commit=False)
            new_meeting.leader = request.user
            new_meeting.save()
            return HttpResponseRedirect('/meetings')
    else:
        meeting_form = MeetingForm()

    return render(request, 'meetings/new_meeting.html', {'meeting_form': meeting_form, 'current_user': current_user})

@login_required
def edit_meeting(request, meeting_id):
    current_user = User.objects.get(username=request.user)
    edit_meeting = Meeting.objects.get(id=meeting_id)
    edit_meeting_form = MeetingForm(initial={'client': edit_meeting.client, 'place': edit_meeting.place,
                                             'date': edit_meeting.date, 'hour': edit_meeting.hour,
                                             'topic': edit_meeting.topic, 'description': edit_meeting.description,
                                             'attachment': edit_meeting.attachment})

    if request.method == 'POST':
        edit_meeting = Meeting.objects.get(id=meeting_id)
        edit_meeting_form = MeetingForm(instance=edit_meeting, data=request.POST, files = request.FILES, initial={'client': edit_meeting.client,
                                                                                           'place': edit_meeting.place,
                                                                                           'date': edit_meeting.date,
                                                                                           'hour': edit_meeting.hour,
                                                                                           'topic': edit_meeting.topic,
                                                                                           'description': edit_meeting.description,
                                                                                           'attachment': edit_meeting.attachment,})
        if edit_meeting_form.is_valid():
            new_meeting = edit_meeting_form.save(commit=False)
            new_meeting.leader = request.user
            new_meeting.save()
            return HttpResponseRedirect('/dashboard')
        else:
            edit_meeting_form = MeetingForm()

    return render(request, 'meetings/edit_meeting.html', {'edit_meeting_form': edit_meeting_form,
                                                          'current_user': current_user})

@login_required
def send_meeting(request, meeting_id):
    current_user = User.objects.get(username=request.user)
    send_meeting = Meeting.objects.get(id=meeting_id)
    send_meeting_form = SendMeetingForm(initial={'client': send_meeting.client, 'place': send_meeting.place,
                                             'date': send_meeting.date, 'hour': send_meeting.hour,
                                             'topic': send_meeting.topic, 'description': send_meeting.description,})

    content = [send_meeting.client, send_meeting.place, send_meeting.date, send_meeting.hour, send_meeting.topic,
            send_meeting.description]
    message_content = str(content)

    if request.method == 'POST':
        send_meeting = Meeting.objects.get(id=meeting_id)
        send_meeting_form = SendMeetingForm(instance=send_meeting, data=request.POST, files = request.FILES, initial={'client': send_meeting.client,
                                                                                           'place': send_meeting.place,
                                                                                           'date': send_meeting.date,
                                                                                           'hour': send_meeting.hour,
                                                                                           'topic': send_meeting.topic,
                                                                                           'description': send_meeting.description,})
        if send_meeting_form.is_valid():
            cd = send_meeting_form.cleaned_data
            subject = send_meeting.client
            message = message_content
            send_mail(subject, message, current_user.email, [cd['email']])
            sent = True
            return HttpResponseRedirect('/dashboard')
        else:
            send_meeting_form = SendMeetingForm()

    return render(request, 'meetings/send_meeting.html', {'send_meeting_form': send_meeting_form,
                                                          'current_user': current_user})

@login_required
def delete_meeting(request, meeting_id):
    current_user = User.objects.get(username=request.user)
    edit_meeting = Meeting.objects.get(id=meeting_id).delete()
    return HttpResponseRedirect('/meetings')

def home(request):
    return render(request, 'meetings/home.html')