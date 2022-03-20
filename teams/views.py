from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseForbidden
from accounts.models import User
from fixtures.models import Game
from .models import Team
from django.shortcuts import get_object_or_404, render


@login_required
def team_list_view(request):
    user = User.objects.get(id=request.user.id)
    if user.user_type == User.Admin:
        teams = Team.objects.all()
        return render(request, 'teams/team_list.html', {'teams': teams})
    else:
        return HttpResponseForbidden()


@login_required
def team_view(request, code):
    user = User.objects.get(id=request.user.id)
    if user.user_type != User.Player:
        team = get_object_or_404(Team, short_code=code)
        players = team.player.all()
        games_played = Game.objects.filter(Q(home_team=team) | Q(away_team=team))
        details = {'team': team, 'players': players, 'avg': calculate_avg_score(team, games_played)}
        return render(request, 'teams/team.html', details)
    else:
        return HttpResponseForbidden()


def calculate_avg_score(team, games_played):
    """
    This method will calculate the average score for a team
    @param games_played:
    @param team: Team
    @return: float average
    """

    total_points = 0
    total_games = 0
    average_score = 0
    for game in games_played:
        if game.home_team == team:
            total_points += game.home_team_score
        else:
            total_points += game.away_team_score
        total_games += 1

    if total_games > 0:
        average_score = total_points/total_games
    return average_score

