from django.db import models


class Game(models.Model):

    FR = 'FR'
    QF = 'QF'
    SF = 'SF'
    FI = 'FI'

    Game_Rounds = [
        ('FR', 'First  Round'),
        ('QF', 'Quarter Final'),
        ('SF', 'Semi Final'),
        ('FI', 'Final')
    ]

    home_team = models.ForeignKey(
        'teams.Team', related_name='home_game',
        verbose_name='Home team',
        on_delete=models.CASCADE
    )

    away_team = models.ForeignKey(
        'teams.Team', related_name='away_game',
        verbose_name='Away team',
        on_delete=models.CASCADE
    )

    home_team_score = models.IntegerField(
        verbose_name='home score'
    )

    away_team_score = models.IntegerField(
        verbose_name='away score'
    )

    winner = models.ForeignKey(
        'teams.Team', related_name='winner',
        verbose_name='Winner',
        null=True, blank=True,
        on_delete=models.CASCADE
    )

    date = models.DateField(
        verbose_name='Date',
    )

    round = models.CharField(
        max_length=2,
        choices=Game_Rounds,
        default='QF',
        verbose_name='game round'
    )

    def __str__(self):
        return self.home_team.name + " vs " + self.away_team.name


class PlayerScore(models.Model):
    player = models.ForeignKey(
        'players.Player', related_name='score',
        verbose_name='Player Score',
        on_delete=models.CASCADE
    )

    game = models.ForeignKey(
        'Game', related_name='player_score',
        verbose_name='Game',
        on_delete=models.CASCADE
    )

    score = models.PositiveSmallIntegerField(
        verbose_name='score',
    )

    def __str__(self):
        return self.player.__str__() + " in " + self.game.__str__() + " - " + self.score.__str__()


