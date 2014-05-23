from django.conf.urls import patterns, include, url
from django.contrib import admin
from app_projects.views import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'app_projects.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^projects/', include('projects.urls', namespace="projects")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/login'}),
    url(r'^permission/$', permission ,name='permission'),
    url(r'^createuser/user$', createUser ,name='createUser'),
    url(r'^createuser/$', user ,name='user'),
) 