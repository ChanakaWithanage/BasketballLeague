
from django.urls import re_path
from . import views

app_name = 'fixtures'


urlpatterns = [
    re_path(r'^game=(?P<game_id>[\w-]+)/$', views.game_view, name="game"),
    re_path(r'^scorecard/$', views.scorecard_view, name="scoreboard"),
]
