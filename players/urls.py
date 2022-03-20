
from django.urls import re_path
from . import views

app_name = 'players'

urlpatterns = [
    re_path(r'^(?P<player_id>[\w-]+)/$', views.player_view, name="player"),
    re_path(r'^filter/team=(?P<team_code>[\w-]+)(.*\&?filter=(?P<percentile>([0-9]+)).*)?/$', views.filter_view, name="filter"),
]
