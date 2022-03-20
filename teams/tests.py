import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "basketballleagueV1.settings")
django.setup()

from fixtures.models import Game
from teams.models import Team
import unittest
from teams.views import calculate_avg_score


class TestTeamCalc(unittest.TestCase):

    def test_calculate_avg_score(self):
        team1 = Team()
        team1.name = 'Test1'

        team2 = Team()
        team2.name = 'Test2'

        game1 = Game()
        game1.home_team = team1
        game1.home_team_score = 5
        game1.away_team = team2
        game1.away_team_score = 2

        game2 = Game()
        game2.home_team = team2
        game2.home_team_score = 50
        game2.away_team = team1
        game2.away_team_score = 20

        game3 = Game()
        game3.away_team = team1
        game3.away_team_score = 20
        game3.home_team = team2
        game3.home_team_score = 15
        games_played = [game1, game2, game3]

        self.assertEqual(calculate_avg_score(team1, games_played), 15)


if __name__ == '__main__':
    unittest.main()
