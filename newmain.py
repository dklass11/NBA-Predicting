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
from sportsreference.nba.schedule import Schedule

# get home team's full schedule and boxscore indexes
home_team = "PHI"
home_team_schedule = Schedule(home_team)
home_team_indexes = list()

for game in home_team_schedule:
    home_team_indexes.append(game.boxscore_index)

# convert current date to count
def dateconverter(date):
    count = 0

    # convert month to number of days
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

    # add number of days to count
    count += int(date[8:10])

    return count

# run current date through converter
current_date_count = dateconverter(str(datetime.date.today()))

def indexconverter(index):
    count = 0

    # convert month to number of days
    if index[4:6] == '10':
        count = 0
    elif index[4:6] == '11':
        count = 31
    elif index[4:6] == '12':
        count = 61
    elif index[4:6] == '01':
        count = 92
    elif index[4:6] == '02':
        count = 123
    elif index[4:6] == '03':
        count = 152
    elif index[4:6] == '04':
        count = 183

    # add number of days to count
    count += int(index[6:8])

    return count

# run indexes through converter
home_team_index_counts = list()

for i in home_team_indexes:
    home_team_index_counts.append(indexconverter(i))

# compare dates and find previous five game dates
home_index_counter = 0

for count in home_team_index_counts:
    if home_index_counter == 0:
        if current_date_count <= count:
            position = home_team_index_counts.index(count)

            # use index counts to find positions of Boxscore indexes

            home_team_five_index_counts = home_team_index_counts[::-1]
            home_team_five_index_counts = home_team_five_index_counts[(82-position):((82-position)+5)]

            home_index_counter = 1

# use index counts to find positions of Boxscore indexes
home_team_five_pos = list()
home_team_five_indexes = list()

for index_count in home_team_five_index_counts:
    home_team_five_pos.append(home_team_index_counts.index(index_count))

for position in home_team_five_pos:
    home_team_five_indexes.append(home_team_indexes[position])

# store each Boxscore
first_game = Boxscore(home_team_five_indexes[0])
second_game = Boxscore(home_team_five_indexes[1])
third_game = Boxscore(home_team_five_indexes[2])
fourth_game = Boxscore(home_team_five_indexes[3])
fifth_game = Boxscore(home_team_five_indexes[4])