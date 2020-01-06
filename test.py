from sportsreference.nba.teams import Teams
from sportsreference.nba.boxscore import Boxscore
from sportsreference.nba.boxscore import Boxscores
from sportsreference.nba.schedule import Schedule
from datetime import datetime

teams = Teams()
print('\nnew run\n')

'''
for team in teams:
    print(team.name)
    print(team.games_played)
'''

specificgame = Boxscore('202001050LAC')
print("\n" + str(specificgame.home_blocks))

phila_schedule = Schedule('PHI')

for i in phila_schedule:
    if i.date == "Tue, Nov 12, 2019":
        print(i.boxscore_index)
        print(i.dataframe)

game2018 = Boxscore('201810160BOS')

print(game2018.winner)

