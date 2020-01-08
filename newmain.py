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

# get target1 team's full schedule and boxscore indexes
target1_team = 'PHI'
target1_team_schedule = Schedule(target1_team)
target1_team_indexes = list()

for game in target1_team_schedule:
    target1_team_indexes.append(game.boxscore_index)

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
target1_team_index_counts = list()

for i in target1_team_indexes:
    target1_team_index_counts.append(indexconverter(i))

# compare dates and find previous five game dates
target1_index_counter = 0

for count in target1_team_index_counts:
    if target1_index_counter == 0:
        if current_date_count <= count:
            position = target1_team_index_counts.index(count)

            # use index counts to find positions of Boxscore indexes

            target1_team_five_index_counts = target1_team_index_counts[::-1]
            target1_team_five_index_counts = target1_team_five_index_counts[(82-position):((82-position)+5)]

            target1_index_counter = 1

# use index counts to find positions of Boxscore indexes
target1_team_five_pos = list()
target1_team_five_indexes = list()

for index_count in target1_team_five_index_counts:
    target1_team_five_pos.append(target1_team_index_counts.index(index_count))

for position in target1_team_five_pos:
    target1_team_five_indexes.append(target1_team_indexes[position])

# store each Boxscore
first_game = Boxscore(target1_team_five_indexes[0])
second_game = Boxscore(target1_team_five_indexes[1])
third_game = Boxscore(target1_team_five_indexes[2])
fourth_game = Boxscore(target1_team_five_indexes[3])
fifth_game = Boxscore(target1_team_five_indexes[4])

# create boolean list to show if target1 team is home
home_list = list([False, False, False, False, False])

for index in target1_team_five_indexes:
    if target1_team in index:
        home_list[target1_team_five_indexes.index(index)] = True


# rerun the same code for target2
target2_team = 'LAL'
target2_team_schedule = Schedule(target2_team)
target2_team_indexes = list()

for game in target2_team_schedule:
    target2_team_indexes.append(game.boxscore_index)

# convert current date to count
def dateconverter_2(date):
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
current_date_count_2 = dateconverter_2(str(datetime.date.today()))

def indexconverter_2(index):
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
target2_team_index_counts = list()

for i in target2_team_indexes:
    target2_team_index_counts.append(indexconverter(i))

# compare dates and find previous five game dates
target2_index_counter = 0

for count in target2_team_index_counts:
    if target2_index_counter == 0:
        if current_date_count <= count:
            position = target2_team_index_counts.index(count)

            # use index counts to find positions of Boxscore indexes

            target2_team_five_index_counts = target2_team_index_counts[::-1]
            target2_team_five_index_counts = target2_team_five_index_counts[(82-position):((82-position)+5)]

            target2_index_counter = 1

# use index counts to find positions of Boxscore indexes
target2_team_five_pos = list()
target2_team_five_indexes = list()

for index_count in target2_team_five_index_counts:
    target2_team_five_pos.append(target2_team_index_counts.index(index_count))

for position in target2_team_five_pos:
    target2_team_five_indexes.append(target2_team_indexes[position])

# store each Boxscore
first_game_2 = Boxscore(target2_team_five_indexes[0])
second_game_2 = Boxscore(target2_team_five_indexes[1])
third_game_2 = Boxscore(target2_team_five_indexes[2])
fourth_game_2 = Boxscore(target2_team_five_indexes[3])
fifth_game_2 = Boxscore(target2_team_five_indexes[4])

# create boolean list to show if target2 team is home
home_list_2 = list([False, False, False, False, False])

for index in target2_team_five_indexes:
    if target2_team in index:
        home_list[target2_team_five_indexes.index(index)] = True