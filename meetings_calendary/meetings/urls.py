from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^meetings/$', views.meetings, name='meetings'),
    url(r'^today_meetings/$', views.today_meetings, name='today_meetings'),
    url(r'^date_meetings/$', views.date_meetings, name='date_meetings'),
    url(r'^date_meetings_all/$', views.date_meetings_all, name='date_meetings_all'),
    url(r'^date_range_meetings/$', views.date_range_meetings, name='date_range_meetings'),
    url(r'^date_range_meetings_all/$', views.date_range_meetings_all, name='date_range_meetings_all'),
    url(r'^find_meetings/$', views.find_meetings, name='find_meetings'),
    url(r'^find_meetings_all/$', views.find_meetings_all, name='find_meetings_all'),
    url(r'^(?P<meeting_id>\d+)/send_meeting/$', views.send_meeting, name='send_meeting'),
    url(r'^add_meeting/$', views.new_meeting, name='new_meeting'),
    url(r'^(?P<meeting_id>\d+)/edit_meeting/$', views.edit_meeting, name='edit_meeting'),
    url(r'^(?P<meeting_id>\d+)/delete_meeting/$', views.delete_meeting, name='delete_meeting'),
    url(r'^(?P<meeting_id>\d+)/$', views.meeting, name='meeting'),
    url(r'^home/$', views.home, name='home'),
]