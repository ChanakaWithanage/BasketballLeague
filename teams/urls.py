
from django.urls import re_path
from . import views


urlpatterns = [
    re_path(r'^$', views.team_list_view, name="team_list"),
    re_path(r'^(?P<code>[\w-]+)/$', views.team_view, name="team_details"),
]
