
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import re_path
from django.views.generic import RedirectView

from . import views
from django.conf.urls import include


urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'^teams/', include('teams.urls')),
    re_path(r'^coaches/', include('coachesv2.urls')),
    re_path(r'^players/', include('players.urls')),
    re_path(r'^fixtures/', include('fixtures.urls')),
    re_path(r'^$', RedirectView.as_view(url='fixtures/scorecard'), name='index')
]

urlpatterns += staticfiles_urlpatterns()