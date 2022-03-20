import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "basketballleagueV1.settings")
django.setup()
import unittest
from players.models import Player
from players.views import get_filtered_players


class TestTeamCalc(unittest.TestCase):

    def test_get_filtered_players(self):

        percentile = 50

        score_list = [10, 20]
        player1 = Player()
        player1.id = 1
        player1.name = 'Test1'

        player2 = Player()
        player2.id = 2
        player2.name = 'Test2'

        avg_scores = { player1: 10, player2: 20}

        self.assertListEqual(get_filtered_players(avg_scores, percentile, score_list), [(player2, 20)])


if __name__ == '__main__':
    unittest.main()
