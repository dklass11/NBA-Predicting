from sportsreference.nba.teams import Teams
from sportsreference.nba.boxscore import Boxscore
from sportsreference.nba.boxscore import Boxscores
from datetime import datetime

teams = Teams()
print('\nnew run\n')

for team in teams:
    print(team.name)
    print(team.games_played)

games_today = Boxscores(datetime(2020, 1, 5))
print(games_today.games)