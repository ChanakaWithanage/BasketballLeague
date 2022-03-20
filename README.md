# BasketballLeague

This is a Django application to manage a basketball league.
The system can have 3 types of users: the league admin(superuser), coaches, and players.

Dummy data for the application has been provided in createdata.py management command

Superuser/Admin username = "TestAdmin"
Superuser/Admin password = "test4321"

# Installation

`git clone https://github.com/ChanakaWithanage/BasketballLeague.git`

`$ cd basketballleagueV1`

`$ python manage.py makemigrations`

`$ python manage.py migrate`

`$ python manage.py createdata`

`$ python manage.py runserver`

# APIs

Followings are some of the exposed APIs in the application

http://127.0.0.1:8000/ - homepage(scoreboard) - Can be accessed by all 3 types of users. This will display all the results, will display all games and final scores, and will reflect how the competition progressed and who won.

http://127.0.0.1:8000/teams/<team_code>/ - This will display the list of the players on the team, and the average score of the team. The players can be selected to view the player profile.

http://127.0.0.1:8000/players/<player_id>/ - This will display the player profile including - player’s name, height, average score, and the number of games he participated in.

http://127.0.0.1:8000/players/filter/team=<team_code>/ - This will filter the players to see only the ones whose average score is in the 90 percentile across the team.
The system also accepts an additional parameter which specify the percentile to filter.
ex:- http://127.0.0.1:8000/players/filter/team=FIT&filter=75 - This will filter the players of FIT team whose average score is in the 75 percentile

http://127.0.0.1:8000/stats/ - The admin can user this usrl to view the number of times each user logged into the system, the total amount of time each user spent on the site, and who is currently online

http://127.0.0.1:8000/teams/ - The admin can view all teams details - their average scores, their list of players, and players details.

# Notes

Please note that since this is a backend development, basic HTML templates were used to display the data.


