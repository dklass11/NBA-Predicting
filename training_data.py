# import math modules
import numpy as np
import pandas as pd
import random as rand
import pickle

# import neural network model
from keras.models import Sequential
from keras.layers import Dense

# import NBA data fetching module
from sportsreference.nba.boxscore import Boxscore
from sportsreference.nba.schedule import Schedule


# initialize any needed variables
boxscore_year = ''
random_date = ''
current_team_name = ''
random_date_count = 0


# retreive training date pickle file
try:
    date_pickle_file = open('pickle_files\\training_date_pickle.txt', 'rb')
    random_date_list = pickle.load(date_pickle_file)
    date_pickle_file.close()

except:
    random_date_list = list()

# retreive training games pickle file
loaded_games_df = pd.DataFrame()

try:
    games_pickle_file = open('pickle_files\\games_df_pickle.txt', 'rb')
    loaded_games_df = pickle.load(games_pickle_file)
    games_pickle_file.close()

except:
    pass

# retreive training points pickle file
loaded_points_df = pd.DataFrame()

try:
    points_pickle_file = open('pickle_files\\points_df_pickle.txt', 'rb')
    loaded_points_df = pickle.load(points_pickle_file)
    points_pickle_file.close()

except:
    pass


# generate a random date to retreive games from
def date_generator():
    # generate a random month
    chance = rand.randint(1, 4)

    if chance <= 3:
        month = '0' + str(rand.randint(1, 3))

    elif chance == 4:
        month = '12'

    # generate a random day based on month
    if month == '01' or month == '03' or month == '12':
        day = rand.randint(1, 31)

        if day in range(1, 10):
            day = '0' + str(day)

        else:
            day = str(day)

    elif month == '02':
        day = rand.randint(1, 28)

        if day in range(1, 10):
            day = '0' + str(day)
        else:
            day = str(day)

    else:
        day = rand.randint(1, 30)

        if day in range(1, 10):
            day = '0' + str(day)
        else:
            day = str(day)

    if month == '12':
        global boxscore_year
        boxscore_year = str(year - 1)

    else:
        boxscore_year = str(year)

    # assign the random date from previous findings
    global random_date
    random_date = boxscore_year + '-' + month + '-' + day
    random_date_team = current_team_name + random_date

    # check if the same random date had been generated before
    date_count = 0

    for date in random_date_list:
        if random_date_team != date:
            date_count += 1

    if date_count == len(random_date_list):
        random_date_list.append(random_date_team)

    else:
        date_generator()

    # convert random date to count
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

    # run random date through converter
    global random_date_count
    random_date_count = dateconverter(random_date)

    print('Generated new random date: ' + random_date)


class Team():

    '''Creates a Team class that stores the schedule of games and boxscore indexes of each selected team for the given year. '''

    def __init__(self, team, year):
        self.name = team
        self.year = year

    # gather dataframes from previous specified number of games and year
    def gather_df(self, n_games):
        self.n_games = n_games + 1
        self.schedule = Schedule(self.name, year=self.year)

        date_generator()

        print('Acquired ' + self.name + "'s " + 'schedule.')

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
                if random_date_count <= count:
                    position = index_counts.index(count)

                    # use index counts to find positions of boxscore indexes
                    multiple_index_counts = index_counts

                    try:
                        multiple_index_counts = multiple_index_counts[((position) - self.n_games):(position)]
                    except:
                        date_generator()

                    index_counter = 1

        # use index counts to find positions of boxscore indexes
        multiple_positions = list()
        multiple_indexes = list()

        for index_count in multiple_index_counts:
            multiple_positions.append(index_counts.index(index_count))

        for position in multiple_positions:
            multiple_indexes.append(indexes[position])

        print('Found last ' + str(self.n_games - 1) + ' boxscore indexes of ' + self.name + '.')

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

        print('Seperated points scored from ' + self.name + "'s dataframe.")

        # add acquired games and pickle dataframes to pickle dataframes
        global loaded_games_df
        loaded_games_df = loaded_games_df.append(training_games_df, ignore_index=True, sort=False)
        global loaded_points_df
        loaded_points_df = loaded_points_df.append(target_points_df, ignore_index=True, sort=False)


# initial conditions to capture NBA data
team_abbrev = ['ATL', 'BOS', 'BRK', 'CHI', 'CHO', 'CLE', 'DAL', 'DEN', 'DET', 'GSW', 'HOU', 'IND', 'LAC', 'LAL', 'MEM',
               'MIA', 'MIL', 'MIN', 'NOP', 'NYK', 'OKC', 'ORL', 'PHI', 'PHO', 'POR', 'SAC', 'SAS', 'TOR', 'UTA', 'WAS']

current_year = 2020 # as in the 2019-2020 season

starting_year = 1985 # works for 1985 and later years (reference website doesn't support all stat categories before then)

n_games = 10


# gather multiple dataframes for different teams in same year
for year in range(starting_year, (current_year + 1)):
    for team_abbr in team_abbrev:
        # adjust team abbreviations to comply with sports reference database for specified year
        if year <= 2012:
            team_abbrev[2] = 'NJN'

        else:
            team_abbrev[2] = 'BRK'

        if year <= 2014:
            team_abbrev[4] = 'CHA'

        else:
            team_abbrev[4] = 'CHO'

        if team_abbr == 'CHA' and 2003 <= year <= 2004:
            continue

        if year <= 2002:
            team_abbrev[4] = 'CHH'

        if team_abbr == 'CHH' and year <= 1988:
            continue

        if year <= 2001:
            team_abbrev[14] = 'VAN'

        else:
            team_abbrev[14] = 'MEM'

        if team_abbr == 'VAN' and year <= 1995:
            continue

        if team_abbr == 'MIA' and year <= 1998:
            continue

        if team_abbr == 'MIN' and year <= 1989:
            continue

        if year <= 2013:
            team_abbrev[18] = 'NOH'

        else:
            team_abbrev[18] = 'NOP'

        if 2006 <= year <= 2007:
            team_abbrev[18] = 'NOK'

        if team_abbr == 'NOH' and year <= 2002:
            continue

        if year <= 2008:
            team_abbrev[20] = 'SEA'

        else:
            team_abbrev[20] = 'OKC'

        if team_abbr == 'ORL' and year <= 1989:
            continue

        if year <= 1985:
            team_abbrev[25] = 'KCK'

        else:
            team_abbrev[25] = 'SAC'

        if team_abbr == 'TOR' and year <= 1995:
            continue

        if year <= 1997:
            team_abbrev[29] = 'WSB'

        else:
            team_abbrev[29] = 'WAS'

        current_team = Team(team_abbr, str(year))
        current_team_name = current_team.name
        current_team.gather_df(n_games)
        print(current_team.target_points)

    print('----------')


# add generated dates to pickle file
date_pickle_file = open('pickle_files\\training_date_pickle.txt', 'wb')
pickle.dump(random_date_list, date_pickle_file)
date_pickle_file.close()

# add acquired games dataframe to pickle file
games_pickle_file = open('pickle_files\\games_df_pickle.txt', 'wb')
pickle.dump(loaded_games_df, games_pickle_file)
games_pickle_file.close()

# dd acquired points dataframe to pickle file
points_pickle_file = open('pickle_files\\points_df_pickle.txt', 'wb')
pickle.dump(loaded_points_df, points_pickle_file)
points_pickle_file.close()


print('Gathered all specified dataframes.')