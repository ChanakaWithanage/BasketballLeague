from operator import itemgetter

from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404

from accounts.models import User
from fixtures.models import PlayerScore
from players.models import Player
from teams.models import Team
import numpy as np
from django.template.defaultfilters import register


@login_required
def player_view(request, player_id):
    user = User.objects.get(id=request.user.id)
    if user.user_type != User.Player:
        player = get_object_or_404(Player, id=player_id)
        average = calculate_avg(player)
        games = PlayerScore.objects.filter(player=player).count()
        return render(request, 'players/player.html', {'player': player, 'average': average, 'game_count': games})
    else:
        return HttpResponseForbidden()


def calculate_avg(player):
    """
    This method will calculate the average score for the player
    @param player: Player
    @return: float
    """
    games_played = PlayerScore.objects.filter(player=player)
    return games_played.aggregate(Avg('score', default=0))['score__avg']


@login_required
def filter_view(request, team_code, percentile=90):
    """
    This function will filter the players based on avg score.
    @param request:
    @param team_code: short_code of the team
    @param percentile: filter percentile(default filter - 90th percentile)
    @return:
    """
    user = User.objects.get(id=request.user.id)
    if user.user_type != User.Player:
        team = get_object_or_404(Team, short_code=team_code)
        players = team.player.all()
        avg_scores = {}
        score_list = []
        for player in players:
            average = calculate_avg(player)
            avg_scores[player] = average
            score_list.append(average)
        print(avg_scores)
        percentile_score = np.percentile(score_list, float(percentile))
        print(percentile_score)
        filtered_players = sorted({k: v for (k, v) in avg_scores.items() if v >= percentile_score}.items()
                                  , key=itemgetter(1), reverse=True)
        print(filtered_players)
        return render(request, 'players/top_players.html', {'players': filtered_players})
    else:
        return HttpResponseForbidden()


@register.filter(name='dict_key')
def dict_key(d, k):
    """Returns the given key from a dictionary."""
    return d[k]
