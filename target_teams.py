# import array and datframe modules
import numpy as np
import pandas as pd

# import neural network model
from keras.models import Sequential
from keras.layers import Dense

# import nba data fetching module
import datetime
from sportsreference.nba.boxscore import Boxscore
from sportsreference.nba.schedule import Schedule

# get target1 team's full schedule and boxscore indexes
target1_team = 'PHI'
target1_team_schedule = Schedule(target1_team)
target1_team_indexes = list()

print('Acquired team 1 schedule.')

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

# compare dates and find previous ten game dates
target1_index_counter = 0

for count in target1_team_index_counts:
    if target1_index_counter == 0:
        if current_date_count <= count:
            position = target1_team_index_counts.index(count)

            # use index counts to find positions of Boxscore indexes
            target1_team_ten_index_counts = target1_team_index_counts[::-1]
            target1_team_ten_index_counts = target1_team_ten_index_counts[(82-position):((82-position)+10)]

            target1_index_counter = 1

# use index counts to find positions of Boxscore indexes
target1_team_ten_pos = list()
target1_team_ten_indexes = list()

for index_count in target1_team_ten_index_counts:
    target1_team_ten_pos.append(target1_team_index_counts.index(index_count))

for position in target1_team_ten_pos:
    target1_team_ten_indexes.append(target1_team_indexes[position])

print('Found boxscore indexes of team 1.')

# store each Boxscore
first_game = Boxscore(target1_team_ten_indexes[0])
second_game = Boxscore(target1_team_ten_indexes[1])
third_game = Boxscore(target1_team_ten_indexes[2])
fourth_game = Boxscore(target1_team_ten_indexes[3])
fifth_game = Boxscore(target1_team_ten_indexes[4])
sixth_game = Boxscore(target1_team_ten_indexes[5])
seventh_game = Boxscore(target1_team_ten_indexes[6])
eighth_game = Boxscore(target1_team_ten_indexes[7])
ninth_game = Boxscore(target1_team_ten_indexes[8])
tenth_game = Boxscore(target1_team_ten_indexes[9])

# create boolean list to show if target1 team is home
home_list = list([False, False, False, False, False, False, False, False, False, False])

for index in target1_team_ten_indexes:
    if target1_team in index:
        home_list[target1_team_ten_indexes.index(index)] = True

first_game_df = pd.DataFrame()
second_game_df = pd.DataFrame()
third_game_df = pd.DataFrame()
fourth_game_df = pd.DataFrame()
fifth_game_df = pd.DataFrame()
sixth_game_df = pd.DataFrame()
seventh_game_df = pd.DataFrame()
eighth_game_df = pd.DataFrame()
ninth_game_df = pd.DataFrame()
tenth_game_df = pd.DataFrame()

first_game_df = first_game.dataframe
second_game_df = second_game.dataframe
third_game_df = third_game.dataframe
fourth_game_df = fourth_game.dataframe
fifth_game_df = fifth_game.dataframe
sixth_game_df = sixth_game.dataframe
seventh_game_df = seventh_game.dataframe
eighth_game_df = eighth_game.dataframe
ninth_game_df = ninth_game.dataframe
tenth_game_df = tenth_game.dataframe

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

sixth_game_df = sixth_game_df.drop(columns=['winning_name', 'winning_abbr', 'winner',
                                'losing_name', 'losing_abbr', 'home_wins', 'away_wins',
                                'date', 'location'])

seventh_game_df = seventh_game_df.drop(columns=['winning_name', 'winning_abbr', 'winner',
                                'losing_name', 'losing_abbr', 'home_wins', 'away_wins',
                                'date', 'location'])

eighth_game_df = eighth_game_df.drop(columns=['winning_name', 'winning_abbr', 'winner',
                                'losing_name', 'losing_abbr', 'home_wins', 'away_wins',
                                'date', 'location'])

ninth_game_df = ninth_game_df.drop(columns=['winning_name', 'winning_abbr', 'winner',
                                'losing_name', 'losing_abbr', 'home_wins', 'away_wins',
                                'date', 'location'])

tenth_game_df = tenth_game_df.drop(columns=['winning_name', 'winning_abbr', 'winner',
                                'losing_name', 'losing_abbr', 'home_wins', 'away_wins',
                                'date', 'location'])


target1_ten_games_df = first_game_df
target1_ten_games_df = target1_ten_games_df.append(second_game_df, ignore_index=True)
target1_ten_games_df = target1_ten_games_df.append(third_game_df, ignore_index=True)
target1_ten_games_df = target1_ten_games_df.append(fourth_game_df, ignore_index=True)
target1_ten_games_df = target1_ten_games_df.append(fifth_game_df, ignore_index=True)
target1_ten_games_df = target1_ten_games_df.append(sixth_game_df, ignore_index=True)
target1_ten_games_df = target1_ten_games_df.append(seventh_game_df, ignore_index=True)
target1_ten_games_df = target1_ten_games_df.append(eighth_game_df, ignore_index=True)
target1_ten_games_df = target1_ten_games_df.append(ninth_game_df, ignore_index=True)
target1_ten_games_df = target1_ten_games_df.append(tenth_game_df, ignore_index=True)

for_game_list = list([first_game, second_game, third_game, fourth_game, fifth_game, sixth_game, seventh_game, eighth_game, ninth_game, tenth_game])
target1_ten_games_points_df = pd.DataFrame()

for game in for_game_list:
    target1_ten_games_points_df = target1_ten_games_points_df.append(game.dataframe[['home_points', 'away_points']], ignore_index=True)

print('Gathered past 10 game stats and seperated points of team 1.')


# rerun the same code for target2
target2_team = 'BOS'
target2_team_schedule = Schedule(target2_team)
target2_team_indexes = list()

print('Acquired team 2 schedule.')

for game in target2_team_schedule:
    target2_team_indexes.append(game.boxscore_index)

# run indexes through converter
target2_team_index_counts = list()

for i in target2_team_indexes:
    target2_team_index_counts.append(indexconverter(i))

# compare dates and find previous ten game dates
target2_index_counter = 0

for count in target2_team_index_counts:
    if target2_index_counter == 0:
        if current_date_count <= count:
            position = target2_team_index_counts.index(count)

            # use index counts to find positions of Boxscore indexes
            target2_team_ten_index_counts = target2_team_index_counts[::-1]
            target2_team_ten_index_counts = target2_team_ten_index_counts[(82-position):((82-position)+10)]

            target2_index_counter = 1

# use index counts to find positions of Boxscore indexes
target2_team_ten_pos = list()
target2_team_ten_indexes = list()

for index_count in target2_team_ten_index_counts:
    target2_team_ten_pos.append(target2_team_index_counts.index(index_count))

for position in target2_team_ten_pos:
    target2_team_ten_indexes.append(target2_team_indexes[position])

print('Found boxscore indexes of team 2.')

# store each Boxscore
first_game_2 = Boxscore(target2_team_ten_indexes[0])
second_game_2 = Boxscore(target2_team_ten_indexes[1])
third_game_2 = Boxscore(target2_team_ten_indexes[2])
fourth_game_2 = Boxscore(target2_team_ten_indexes[3])
fifth_game_2 = Boxscore(target2_team_ten_indexes[4])
sixth_game_2 = Boxscore(target2_team_ten_indexes[5])
seventh_game_2 = Boxscore(target2_team_ten_indexes[6])
eighth_game_2 = Boxscore(target2_team_ten_indexes[7])
ninth_game_2 = Boxscore(target2_team_ten_indexes[8])
tenth_game_2 = Boxscore(target2_team_ten_indexes[9])


# create boolean list to show if target2 team is home
home_list_2 = list([False, False, False, False, False, False, False, False, False, False])

for index in target2_team_ten_indexes:
    if target2_team in index:
        home_list[target2_team_ten_indexes.index(index)] = True

first_game_df_2 = pd.DataFrame()
second_game_df_2 = pd.DataFrame()
third_game_df_2 = pd.DataFrame()
fourth_game_df_2 = pd.DataFrame()
fifth_game_df_2 = pd.DataFrame()
sixth_game_df_2 = pd.DataFrame()
seventh_game_df_2 = pd.DataFrame()
eighth_game_df_2 = pd.DataFrame()
ninth_game_df_2 = pd.DataFrame()
tenth_game_df_2 = pd.DataFrame()

first_game_df_2 = first_game_2.dataframe
second_game_df_2 = second_game_2.dataframe
third_game_df_2 = third_game_2.dataframe
fourth_game_df_2 = fourth_game_2.dataframe
fifth_game_df_2 = fifth_game_2.dataframe
sixth_game_df_2 = sixth_game_2.dataframe
seventh_game_df_2 = seventh_game_2.dataframe
eighth_game_df_2 = eighth_game_2.dataframe
ninth_game_df_2 = ninth_game_2.dataframe
tenth_game_df_2 = tenth_game_2.dataframe


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

sixth_game_df_2 = sixth_game_df_2.drop(columns=['winning_name', 'winning_abbr', 'winner',
                                'losing_name', 'losing_abbr', 'home_wins', 'away_wins',
                                'date', 'location'])

seventh_game_df_2 = seventh_game_df_2.drop(columns=['winning_name', 'winning_abbr', 'winner',
                                'losing_name', 'losing_abbr', 'home_wins', 'away_wins',
                                'date', 'location'])

eighth_game_df_2 = eighth_game_df_2.drop(columns=['winning_name', 'winning_abbr', 'winner',
                                'losing_name', 'losing_abbr', 'home_wins', 'away_wins',
                                'date', 'location'])

ninth_game_df_2 = ninth_game_df_2.drop(columns=['winning_name', 'winning_abbr', 'winner',
                                'losing_name', 'losing_abbr', 'home_wins', 'away_wins',
                                'date', 'location'])

tenth_game_df_2 = tenth_game_df_2.drop(columns=['winning_name', 'winning_abbr', 'winner',
                                'losing_name', 'losing_abbr', 'home_wins', 'away_wins',
                                'date', 'location'])

target2_ten_games_df = first_game_df_2
target2_ten_games_df = target2_ten_games_df.append(second_game_df_2, ignore_index=True)
target2_ten_games_df = target2_ten_games_df.append(third_game_df_2, ignore_index=True)
target2_ten_games_df = target2_ten_games_df.append(fourth_game_df_2, ignore_index=True)
target2_ten_games_df = target2_ten_games_df.append(fifth_game_df_2, ignore_index=True)
target2_ten_games_df = target2_ten_games_df.append(sixth_game_df_2, ignore_index=True)
target2_ten_games_df = target2_ten_games_df.append(seventh_game_df_2, ignore_index=True)
target2_ten_games_df = target2_ten_games_df.append(eighth_game_df_2, ignore_index=True)
target2_ten_games_df = target2_ten_games_df.append(ninth_game_df_2, ignore_index=True)
target2_ten_games_df = target2_ten_games_df.append(tenth_game_df_2, ignore_index=True)

for_game_list_2 = list([first_game_2, second_game_2, third_game_2, fourth_game_2, fifth_game_2, sixth_game_2, seventh_game_2, eighth_game_2, ninth_game_2, tenth_game_2])
target2_ten_games_points_df = pd.DataFrame()

for game in for_game_list_2:
    target2_ten_games_points_df = target2_ten_games_points_df.append(game.dataframe[['home_points', 'away_points']], ignore_index=True)

print('Gathered past 10 game stats and seperated points of team 2.')

print('Running neural network.')

model_target1 = Sequential()

model_target1.add(Dense(74, activation='relu', input_dim=73))
model_target1.add(Dense(200, activation='relu'))
model_target1.add(Dense(200, activation='relu'))
model_target1.add(Dense(200, activation='relu'))
model_target1.add(Dense(200, activation='relu'))
model_target1.add(Dense(200, activation='relu'))
model_target1.add(Dense(2))

model_target1.compile(optimizer='adam', loss='mean_squared_error')

model = model_target1.fit(target1_ten_games_df, target1_ten_games_points_df, validation_split=0.1, epochs=1000, shuffle=True)

predictedwins = model_target1.predict(target2_ten_games_df)

print(predictedwins)