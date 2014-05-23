from django.conf.urls import patterns, url
from projects import views

urlpatterns = patterns('',
    url(r'^$', views.projectsInProgress, name='projectsInProgress'),
    url(r'^completed$', views.projectsCompleted, name='projectsCompleted'),
    url(r'^(?P<project_id>\d+)/$', views.tasks, name='tasks'),
    url(r'^(?P<project_id>\d+)/(?P<task_id>\d+)/$', views.taskCompleted, name='taskCompleted'),
    url(r'^(?P<project_id>\d+)/addtask$', views.addTask, name='addTask'),
    url(r'^addproject$', views.addProject, name='addProject'),
    url(r'^completed/(?P<project_id>\d+)/$', views.projectCompleted, name='projectCompleted'),
    url(r'^(?P<project_id>\d+)/(?P<task_id>\d+)/start$', views.start, name='start'),
    url(r'^(?P<project_id>\d+)/(?P<task_id>\d+)/pause$', views.pause, name='pause'),
)
