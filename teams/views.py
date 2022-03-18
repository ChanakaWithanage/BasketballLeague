from http import HTTPStatus

from django.http import JsonResponse
from .models import Team
from django.shortcuts import get_object_or_404


def team_list_view(request):
    teams = Team.objects.all().values()
    return JsonResponse({'teams': list(teams)}, status=HTTPStatus.OK)


def team_view(request, code):
    # team = Team.objects.filter(short_code=code)
    team = get_object_or_404(Team, short_code=code)
    print(team)
    players = team.player.all().values()
    print(players)
    team_json = Team.objects.filter(short_code=code).values('name', 'short_code')

    # team_values = team.values()
    # str_data = serialize('json', [team])
    return JsonResponse({'team': list(team_json), 'players': list(players)}, status=HTTPStatus.OK)
