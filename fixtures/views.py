from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

from fixtures.models import Game


@login_required
def game_view(game_id):
    game = Game.objects.filter(id=game_id)
    game_json = {'home_team': game[0].home_team.name, 'away_team': game[0].away_team.name, 'winner': game[0].winner.name}
    game_json.update(game.values('home_team_score', 'away_team_score', 'round', 'date')[0])
    return JsonResponse({'game': game_json})


@login_required
def scorecard_view(request):
    fr_games = Game.objects.filter(round=Game.FR)       # fetch first round
    qf_games = Game.objects.filter(round=Game.QF)       # fetch quarter finals
    sf_games = Game.objects.filter(round=Game.SF)       # fetch semi finals
    final = Game.objects.filter(round=Game.FI)          # fetch final game

    scorecard = {'FR': fr_games, 'QF': qf_games, 'SF': sf_games, 'FI': final}
    return render(request, 'fixtures/scorecard.html', scorecard)
