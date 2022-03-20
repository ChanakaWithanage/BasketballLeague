from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseForbidden
from accounts.models import User
from teams.models import Team
from django.shortcuts import get_object_or_404


@login_required
def team_view(request, code):
    user = User.objects.get(id=request.user.id)
    if user.user_type != User.Player:
        team = get_object_or_404(Team, short_code=code)
        players = team.player.all().values('id', 'first_name', 'last_name')
        team_json = Team.objects.filter(short_code=code).values('name', 'short_code')
        return JsonResponse({'team': list(team_json), 'players': list(players)})
    else:
        return HttpResponseForbidden()


