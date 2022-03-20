from django.core.management.base import BaseCommand, CommandError
from faker import Faker
from accounts.models import User
from coachesv2.models import Coach
from fixtures.models import Game, PlayerScore
from players.models import Player
from teams.models import Team


class Command(BaseCommand):

    @staticmethod
    def populate_users(fake):
        admin_created = False
        coaches_count = 0
        players_count = 0
        generated_name = []
        for i in range(97):  # 80 players + 16 coaches + 1 admin
            username = fake.user_name()
            while username in generated_name:
                username = fake.user_name()

            generated_name.append(username)
            password = 'test4321'
            user = User.objects.create_user(username=username, password=password,
                                            first_name=fake.first_name(), last_name=fake.last_name())
            if admin_created:
                if coaches_count < 16:
                    user.user_type = User.Coach
                    coaches_count += 1
                else:
                    user.user_type = User.Player
                    players_count += 1
            else:
                user.user_type = User.Admin
                user.username = 'TestAdmin'
                user.is_staff = True
                user.is_superuser = True
                admin_created = True
            user.save()
        print('User creation completed!')

    @staticmethod
    def populate_coaches(fake):
        users = User.objects.filter(user_type=User.Coach)

        for user in users:
            coach = Coach()
            coach.first_name = user.first_name
            coach.last_name = user.last_name
            coach.user = user
            coach.save()
        print('Coaches creation completed!')

    @staticmethod
    def populate_team(fake):
        coaches = Coach.objects.all()
        for i in range(16):
            team = Team()
            team.name = fake.slug()
            team.short_code = fake.lexify(text='???', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ')
            team.coach = coaches[i]
            team.save()
        print('Teams creation completed!')

    @staticmethod
    def populate_players(fake):
        teams = Team.objects.all()
        users = User.objects.filter(user_type=User.Player)

        player_count = 0
        team_count = 0
        for user in users:
            player = Player()
            player.first_name = user.first_name
            player.last_name = user.last_name
            player.user = user
            player.height = fake.random_int(min=150, max=300, step=1)
            player.weight = fake.random_int(min=50, max=100, step=1)
            player.team = teams[team_count]
            player.date_of_birth = fake.date_time_this_decade()
            player.save()
            player_count += 1
            if player_count == 5:
                team_count += 1
                player_count = 0
        print('Players creation completed!')

    @staticmethod
    def populate_games(fake):
        teams = Team.objects.all()
        host_teams = teams[:8]
        away_teams = teams[8:]
        first_winners = []
        qf_winners = []
        sf_winners = []

        for i in range(8):
            host_score = fake.random_int(min=5, max=100, step=1)
            away_score = fake.random_int(min=5, max=100, step=1)
            winner = host_teams[i] if host_score > away_score else away_teams[i]
            first_winners.append(winner)
            game = Game()
            game.home_team = host_teams[i]
            game.away_team = away_teams[i]
            game.winner = winner
            game.home_team_score = host_score
            game.away_team_score = away_score
            game.date = fake.date_time_this_decade()
            game.round = Game.FR
            game.save()
            Command.populate_player_stats(fake, game)

        host_teams = first_winners[:4]
        away_teams = first_winners[4:]
        for i in range(4):
            host_score = fake.random_int(min=5, max=100, step=1)
            away_score = fake.random_int(min=5, max=100, step=1)
            winner = host_teams[i] if host_score > away_score else away_teams[i]
            qf_winners.append(winner)
            game = Game()
            game.home_team = host_teams[i]
            game.away_team = away_teams[i]
            game.winner = winner
            game.home_team_score = host_score
            game.away_team_score = away_score
            game.date = fake.date_time_this_decade()
            game.round = Game.QF
            game.save()
            Command.populate_player_stats(fake, game)

        host_teams = qf_winners[:2]
        away_teams = qf_winners[2:]
        for i in range(2):
            host_score = fake.random_int(min=5, max=100, step=1)
            away_score = fake.random_int(min=5, max=100, step=1)
            winner = host_teams[i] if host_score > away_score else away_teams[i]
            sf_winners.append(winner)
            game = Game()
            game.home_team = host_teams[i]
            game.away_team = away_teams[i]
            game.winner = winner
            game.home_team_score = host_score
            game.away_team_score = away_score
            game.date = fake.date_time_this_decade()
            game.round = Game.SF
            game.save()
            Command.populate_player_stats(fake, game)

        host_score = fake.random_int(min=5, max=100, step=1)
        away_score = fake.random_int(min=5, max=100, step=1)
        winner = sf_winners[0] if host_score > away_score else sf_winners[1]
        game = Game()
        game.home_team = sf_winners[0]
        game.away_team = sf_winners[1]
        game.winner = winner
        game.home_team_score = host_score
        game.away_team_score = away_score
        game.date = fake.date_time_this_decade()
        game.round = Game.FI
        game.save()
        Command.populate_player_stats(fake, game)
        print('Games creation completed!')

    @staticmethod
    def populate_player_stats(fake, game):
        home_players = Player.objects.filter(team=game.home_team)
        score_limit = game.home_team_score
        for player in home_players:
            score = PlayerScore()
            score.player = player
            score.game = game
            score.score = fake.random_int(min=0, max=score_limit, step=1)
            score_limit -= score.score
            score.save()
        away_players = Player.objects.filter(team=game.away_team)
        score_limit = game.away_team_score
        for player in away_players:
            score = PlayerScore()
            score.player = player
            score.game = game
            score.score = fake.random_int(min=0, max=score_limit, step=1)
            score_limit -= score.score
            score.save()

    def handle(self, *args, **options):
        fake = Faker()
        self.populate_users(fake)
        self.populate_coaches(fake)
        self.populate_team(fake)
        self.populate_players(fake)
        self.populate_games(fake)

