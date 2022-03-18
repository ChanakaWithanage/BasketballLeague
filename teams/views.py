from http import HTTPStatus

from django.http import JsonResponse
from .models import Team
from django.shortcuts import get_object_or_404


def team_list_view(request):
    teams = Team.objects.all().values()
    return JsonResponse({'teams': list(teams)})


def team_view(request, code):
    team = get_object_or_404(Team, short_code=code)
    players = team.player.all().values('id', 'first_name', 'last_name')
    team_json = Team.objects.filter(short_code=code).values('name', 'short_code')
    return JsonResponse({'team': list(team_json), 'players': list(players)})
