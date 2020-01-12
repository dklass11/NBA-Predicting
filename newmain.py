# import array and datframe modules
import numpy as np
import pandas as pd

# import neural network model
from keras.models import Sequential
from keras.layers import Dense

# import nba data fetching module
import datetime
from sportsreference.nba.teams import Teams
from sportsreference.nba.boxscore import Boxscore
from sportsreference.nba.schedule import Schedule

# get target1 team's full schedule and boxscore indexes
target1_team = 'TOR'
target1_team_schedule = Schedule(target1_team)
target1_team_indexes = list()

print('Acquired team 1 schdeule.')

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

print('Converted current date.')

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

print('Found boxscore indexes of team 1.')

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

print('Acquired team 2 schdeule.')

for game in target2_team_schedule:
    target2_team_indexes.append(game.boxscore_index)

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

print('Found boxscore indexes of team 2.')

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

first_game_df = pd.DataFrame()
second_game_df = pd.DataFrame()
third_game_df = pd.DataFrame()
fourth_game_df = pd.DataFrame()
fifth_game_df = pd.DataFrame()

first_game_df = first_game.dataframe
second_game_df = second_game.dataframe
third_game_df = third_game.dataframe
fourth_game_df = fourth_game.dataframe
fifth_game_df = fifth_game.dataframe

first_game_df = first_game_df.drop(columns=['winning_name', 'winning_abbr', 'winner',
                                'losing_name', 'losing_abbr', 'home_wins', 'away_wins',
                                'date', 'location'])
                                
second_game_df = second_game_df.drop(columns=['winning_name', 'winning_abbr', 'winner',
                                'losing_name', 'losing_abbr', 'home_wins', 'away_wins',
                                'date', 'location'])
                                
third_game_df = third_game_df.drop(columns=['winning_name', 'winning_abbr', 'winner',
                                'losing_name', 'losing_abbr', 'home_wins', 'away_wins',
                                'date', 'location'])

fourth_game_df = fourth_game_df.drop(columns=['winning_name', 'winning_abbr', 'winner',
                                'losing_name', 'losing_abbr', 'home_wins', 'away_wins',
                                'date', 'location'])

fifth_game_df = fifth_game_df.drop(columns=['winning_name', 'winning_abbr', 'winner',
                                'losing_name', 'losing_abbr', 'home_wins', 'away_wins',
                                'date', 'location'])

target1_five_games_df = first_game_df
target1_five_games_df = target1_five_games_df.append(second_game_df, ignore_index=True)
target1_five_games_df = target1_five_games_df.append(third_game_df, ignore_index=True)
target1_five_games_df = target1_five_games_df.append(fourth_game_df, ignore_index=True)
target1_five_games_df = target1_five_games_df.append(fifth_game_df, ignore_index=True)

target1_five_games_df_w = first_game.dataframe[['winning_abbr']]
target1_five_games_df_w = target1_five_games_df_w.append(second_game.dataframe[['winning_abbr']], ignore_index=True)
target1_five_games_df_w = target1_five_games_df_w.append(third_game.dataframe[['winning_abbr']], ignore_index=True)
target1_five_games_df_w = target1_five_games_df_w.append(fourth_game.dataframe[['winning_abbr']], ignore_index=True)
target1_five_games_df_w = target1_five_games_df_w.append(fifth_game.dataframe[['winning_abbr']], ignore_index=True)

first_game_df_2 = pd.DataFrame()
second_game_df_2 = pd.DataFrame()
third_game_df_2 = pd.DataFrame()
fourth_game_df_2 = pd.DataFrame()
fifth_game_df_2 = pd.DataFrame()

first_game_df_2 = first_game_2.dataframe
second_game_df_2 = second_game_2.dataframe
third_game_df_2 = third_game_2.dataframe
fourth_game_df_2 = fourth_game_2.dataframe
fifth_game_df_2 = fifth_game_2.dataframe

first_game_df_2 = first_game_df_2.drop(columns=['winning_name', 'winning_abbr', 'winner',
                                'losing_name', 'losing_abbr', 'home_wins', 'away_wins',
                                'date', 'location'])

second_game_df_2 = second_game_df_2.drop(columns=['winning_name', 'winning_abbr', 'winner',
                                'losing_name', 'losing_abbr', 'home_wins', 'away_wins',
                                'date', 'location'])

third_game_df_2 = third_game_df_2.drop(columns=['winning_name', 'winning_abbr', 'winner',
                                'losing_name', 'losing_abbr', 'home_wins', 'away_wins',
                                'date', 'location'])

fourth_game_df_2 = fourth_game_df_2.drop(columns=['winning_name', 'winning_abbr', 'winner',
                                'losing_name', 'losing_abbr', 'home_wins', 'away_wins',
                                'date', 'location'])

fifth_game_df_2 = fifth_game_df_2.drop(columns=['winning_name', 'winning_abbr', 'winner',
                                'losing_name', 'losing_abbr', 'home_wins', 'away_wins',
                                'date', 'location'])

target2_five_games_df = first_game_df_2
target2_five_games_df = target2_five_games_df.append(second_game_df_2, ignore_index=True)
target2_five_games_df = target2_five_games_df.append(third_game_df_2, ignore_index=True)
target2_five_games_df = target2_five_games_df.append(fourth_game_df_2, ignore_index=True)
target2_five_games_df = target2_five_games_df.append(fifth_game_df_2, ignore_index=True)

target2_five_games_df_w = first_game_2.dataframe[['winning_abbr']]
target2_five_games_df_w = target2_five_games_df_w.append(second_game_2.dataframe[['winning_abbr']], ignore_index=True)
target2_five_games_df_w = target2_five_games_df_w.append(third_game_2.dataframe[['winning_abbr']], ignore_index=True)
target2_five_games_df_w = target2_five_games_df_w.append(fourth_game_2.dataframe[['winning_abbr']], ignore_index=True)
target2_five_games_df_w = target2_five_games_df_w.append(fifth_game_2.dataframe[['winning_abbr']], ignore_index=True)

print('Gathered both data sets.')

team_abbrev = {'ATL': 1, 'BKN': 2, 'BOS': 3, 'CHA': 4, 'CHI': 5, 'CLE': 6, 'DAL': 7, 'DEN': 8, 'DET': 9, 'GSW': 10,
            'HOU': 11, 'IND': 12, 'LAC': 13, 'LAL': 14, 'MEM': 15, 'MIA': 16, 'MIL': 17,  'MIN': 18, 'NOP': 19, 'NYK': 20,
            'OKC': 21, 'ORL': 22, 'PHI': 23, 'PHX': 24, 'POR': 25, 'SAC': 26, 'SAS': 27, 'TOR': 28, 'UTA': 29, 'WAS': 30}

target1_converted_abbr_in = target1_five_games_df_w.values.tolist()

target1_converted_abbr = list()

def abbreviation_converter(abbreviations):
    for i in abbreviations:
        for abbrev in i:
            pos = team_abbrev[abbrev]
            target1_converted_abbr.append(pos)

abbreviation_converter(target1_converted_abbr_in)

target1_converted_abbr_df = pd.DataFrame(target1_converted_abbr)

target1_converted_abbr_df.columns = ['winning_abbr']

target2_converted_abbr_in = target2_five_games_df_w.values.tolist()

target2_converted_abbr = list()

def abbreviation_converter_2(abbreviations):
    for i in abbreviations:
        for abbrev in i:
            pos = team_abbrev[abbrev]
            target2_converted_abbr.append(pos)

abbreviation_converter_2(target2_converted_abbr_in)

target2_converted_abbr_df = pd.DataFrame(target2_converted_abbr)

target2_converted_abbr_df.columns = ['winning_abbr']

print('Running neural network.')

model_target1 = Sequential()

model_target1.add(Dense(74, activation='relu', input_dim=73))
model_target1.add(Dense(200, activation='relu'))
model_target1.add(Dense(200, activation='relu'))
model_target1.add(Dense(200, activation='relu'))
model_target1.add(Dense(200, activation='relu'))
model_target1.add(Dense(200, activation='relu'))
model_target1.add(Dense(1))

model_target1.compile(optimizer='adam', loss='mean_squared_error')

model = model_target1.fit(target1_five_games_df, target1_converted_abbr_df, validation_split=0.1, epochs=1000, shuffle=True)

predictedwins = model_target1.predict(target2_five_games_df)

print(predictedwins)