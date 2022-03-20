
from django.urls import re_path
from . import views

app_name = 'teams'

urlpatterns = [
    re_path(r'^$', views.team_list_view, name="team_list"),
    re_path(r'^(?P<code>[\w-]+)/$', views.team_view, name="team_details"),
]
