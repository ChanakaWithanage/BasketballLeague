from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Q
from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.utils import timezone

from accounts.models import User
from fixtures.models import PlayerScore
from sitestats.models import Stat


@login_required
def stats_view(request):
    user = User.objects.get(id=request.user.id)
    if user.user_type == User.Admin:
        online_users = Stat.objects.filter(Q(user=user) & Q(logout_time=None))

        stats = Stat.objects.all()
        stat_dict = {}
        for stat in stats:
            if stat.user in stat_dict:
                stat_dict[stat.user].append(stat)
            else:
                stat_dict[stat.user] = [stat]

        stats_summary = prepare_user_stats(stat_dict)

        stats = {
            'stats': stats_summary,
            'online_users': online_users,
        }
        return render(request, 'sitestats/stats.html', stats)
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


def prepare_user_stats(stat_dict):
    """
    This method will prepare a user wise summary
    @param stat:
    @param stat_dict:
    @return:
    """
    stats_summary = []
    for key in stat_dict:
        user_stat = Stat()
        user_login_count = 0
        user_online_time = 0
        print(key)
        for stat in stat_dict[key]:
            user_login_count += 1
            if stat.logout_time is not None:
                user_online_time += (stat.logout_time - stat.login_time).total_seconds()
            else:
                user_online_time += (timezone.now() - stat.login_time).total_seconds()
        user_stat.login_count = user_login_count
        user_stat.total_online_time = round(user_online_time / 60, 2)  # total online time by minutes
        user_stat.user = stat.user
        stats_summary.append(user_stat)
    return stats_summary
