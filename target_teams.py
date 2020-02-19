# import math and data storing modules
import numpy as np
import pandas as pd
import random as rand
import pickle
from datetime import date

# import neural network model
from keras.models import Sequential
from keras.layers import Dense

# import NBA data fetching module
from sportsreference.nba.boxscore import Boxscore
from sportsreference.nba.schedule import Schedule


# initialize any needed variables
boxscore_year = ''
current_team_name = ''
current_date_count = 0

if str(date.today())[5:7] == '11' or str(date.today())[5:7] == '12':
    current_year = str(int(str(date.today())[:4] + 1))

else:
    current_year = str(date.today())[:4]


# convert current date to count to be used to compare against game schedule
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
    count += int(date[8:])

    return count


class Team():

    '''Creates a Team class that stores the schedule of games and boxscore indexes of each selected team for the given year. '''

    def __init__(self, team, year):
        self.name = team
        self.year = year

    # gather dataframes from previous specified number of games and year
    def gather_df(self, n_games):
        self.n_games = n_games + 1
        self.schedule = Schedule(self.name, year=self.year)

        global current_date_count
        current_date_count = dateconverter(str(date.today()))

        indexes = list()
        for game in self.schedule:
            indexes.append(game.boxscore_index)

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
        index_counts = list()

        for index in indexes:
            index_counts.append(indexconverter(index))

        # compare dates and find previous specified number of game dates
        index_counter = 0

        for count in index_counts:
            if index_counter == 0:
                if current_date_count <= count:
                    position = index_counts.index(count)

                    # use index counts to find positions of boxscore indexes
                    multiple_index_counts = index_counts
                    multiple_index_counts = multiple_index_counts[((position) - self.n_games):(position)]
                    index_counter = 1

        # use index counts to find positions of boxscore indexes
        multiple_positions = list()
        multiple_indexes = list()

        for index_count in multiple_index_counts:
            multiple_positions.append(index_counts.index(index_count))

        for position in multiple_positions:
            multiple_indexes.append(indexes[position])

        # use boxscore indexes to retreive each game's dataframe
        boxscore_list = list()
        dataframe_list = list()

        for i in range(self.n_games):
            boxscore_list.append(Boxscore(multiple_indexes[i]))

            dataframe_list.append(boxscore_list[i].dataframe)

            dataframe_list[i] = dataframe_list[i].drop(columns=['winning_name', 'winning_abbr', 'winner',
                                        'losing_name', 'losing_abbr', 'home_wins',
                                        'away_wins', 'date', 'location'])

        # label each column by the order that the game was played in
        dataframe_column_list = list()
        dataframe_value_list = list()
        new_df_value_list = list()

        for iterable, df in enumerate(dataframe_list):
            for column in df:
                df.rename(columns={column: (str(column) + str(iterable))}, inplace=True)
                dataframe_column_list.append(str(column) + str(iterable))

        for df in dataframe_list:
            dataframe_value_list.append(df.values)

        for iterable, arr in enumerate(dataframe_value_list):
            dataframe_value_list[iterable] = arr.tolist()
            new_df_value_list.extend(dataframe_value_list[iterable][0])

        training_games_df = pd.DataFrame(columns=dataframe_column_list)

        training_games_df.loc[0] = new_df_value_list

        # separate the points scored (target data) into separate dataframes
        target_points_df = pd.DataFrame()
        df_columns = pd.DataFrame()
        df_columns = training_games_df[['home_points' + str(self.n_games - 1), 'away_points' + str(self.n_games - 1)]]
        target_points_df = target_points_df.append(df_columns, ignore_index=True, sort=False)
        self.target_points = target_points_df

        # filter out the most recent (target) game from the training data
        training_games_df = training_games_df.filter(regex=r'.*(?<!' + str(self.n_games - 1) + ')$')
        self.training_games = training_games_df

        print('Acquired last ' + str(self.n_games - 1) + ' game statistics of ' + self.name + ' in ' + str(current_year) + '.')


# initial conditions to capture NBA data
target_team_abbreviations = ['PHI', 'LAL']

n_games = 10


# gather dataframes for target teams
for target_team in target_team_abbreviations:
    # create a team class for every team and gather dataframes
    current_team = Team(target_team, str(current_year))
    current_team_name = current_team.name
    current_team.gather_df(n_games)


# neural network
model = Sequential()

model.add(Dense(74, activation='relu', input_dim=73))
model.add(Dense(200, activation='relu'))
model.add(Dense(200, activation='relu'))
model.add(Dense(200, activation='relu'))
model.add(Dense(200, activation='relu'))
model.add(Dense(200, activation='relu'))
model.add(Dense(2))

model.compile(optimizer='adam', loss='mean_squared_error')

model = model.fit(target1_ten_games_df, target1_ten_games_points_df, validation_split=0.1, epochs=1000, shuffle=True)

predictedwins = model.predict(target2_ten_games_df)

print(predictedwins)
'''