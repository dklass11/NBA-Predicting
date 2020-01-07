# import array and datframe modules
import numpy as np
import pandas as pd
'''
# import neural network model
from keras.models import Sequential
from keras.layers import Dense
'''
# import nba data fetching module
import datetime
from sportsreference.nba.teams import Teams
from sportsreference.nba.boxscore import Boxscore
from sportsreference.nba.boxscore import Boxscores
from sportsreference.nba.schedule import Schedule

# get home team's metrics
home_team = "LAL"
home_team_schedule = Schedule(home_team)
home_team_dates = list()

for game in home_team_schedule:
    home_team_dates.append(game.date)

# convert schedule dates to count
def dateconverter1(date):
    count = 0

    if 'Oct' in date:
        count = 0
    elif 'Nov' in date:
        count = 31
    elif 'Dec' in date:
        count = 61
    elif 'Jan' in date:
        count = 92
    elif 'Feb' in date:
        count = 123
    elif 'Mar' in date:
        count = 152 # for leap year only
    elif 'Apr' in date:
        count = 183
 
    if date[10] is not ',':
        count += int(date[9:11])
    else:
        count += int(date[9])

    return count

# convert current date to count
def dateconverter2(date):
    count = 0

    if date[5:7] == '10':
        count = 0
    elif date[5:7] == '11':
        count = 31
    elif date[5:7] == '12':
        count = 61
    elif date[5:7] == '01':
        count = 92
    elif date[5:7] == '02':
        count = 123
    elif date[5:7] == '03':
        count = 152
    elif date[5:7] == '04':
        count = 183

    count += int(date[8:10])

    return count

# run schedulate dates through converter
schedule_date_counts = list()

for date in home_team_dates:
    schedule_date_counts.append(dateconverter1(date))

# run current date through converter
current_date_count = dateconverter2(str(datetime.date.today()))

# compare dates and find previous five game dates
date_counter = 0
home_game_date_list = list()

for date in schedule_date_counts:
    if date_counter == 0:
        if current_date_count <= date:
            position = schedule_date_counts.index(date)

            home_game_date_list = home_team_dates[::-1]
            home_game_date_list = home_game_date_list[(82-position):((82-position)+5)]

            date_counter = 1