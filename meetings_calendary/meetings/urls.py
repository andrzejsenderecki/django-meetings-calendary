from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^meetings/$', views.meetings, name='meetings'),
    url(r'^add_meeting/$', views.new_meeting, name='new_meeting'),
    url(r'^(?P<meeting_id>\d+)/$', views.meeting, name='meeting'),
    url(r'^home/$', views.home, name='home'),
]