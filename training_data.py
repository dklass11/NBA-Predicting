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


# generate a random date to retreive games from
def date_generator():
    # generate a random month
    chance = rand.randint(1, 6)

    if chance <= 4:
        month = '0' + str(rand.randint(1, 4))

    elif chance >= 5:
        month = str(rand.randint(11, 12))
    
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

    elif month == '04':
        day = '0' + str(rand.randint(1, 9)) # limit because of the playoffs

    else:
        day = rand.randint(1, 30)

        if day in range(1, 10):
            day = '0' + str(day)
        else:
            day = str(day)
    
    if month == '11' or month == '12':
        global boxscore_year
        boxscore_year = str(int(year) - 1)

    else:
        boxscore_year = year

    # assign the random date from previous findings
    global random_date
    random_date = boxscore_year + '-' + month + '-' + day
    
    # retreive training date pickle and check if the same random date had been generated before
    try:
        date_pickle_file = open('training_date_pickles\\' + year + '_training_date_pickle.txt', 'rb')
        random_date_list = pickle.load(date_pickle_file)
        date_pickle_file.close()

    except:
        date_pickle_file = open('training_date_pickles\\' + year + '_training_date_pickle.txt', 'wb')
        date_pickle_file.close()

        random_date_list = list()

    if random_date not in random_date_list:
        random_date_list.append(random_date)

    else:
        date_generator()

    date_pickle_file = open('training_date_pickles\\' + year + '_training_date_pickle.txt', 'wb')
    pickle.dump(random_date_list, date_pickle_file)
    date_pickle_file.close()
    
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

    print('Generated random date: ' + random_date)
        

class Team():

    '''Creates a Team class that stores the schedule of games and boxscore indexes of each selected team for the given year. '''

    def __init__(self, team):
        self.team = team
        date_generator()
        
    # gather dataframes from previous specified number of games and year
    def gatherdf(self, year, n_games):
        self.year = year
        self.n_games = n_games + 1
        self.schedule = Schedule(self.team, year=year)

        print('Acquired ' + self.team + "'s " + 'schdeule.')
        
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

        # compare dates and find previous specified numnber of game dates
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

        print('Found last ' + str(self.n_games - 1) + ' boxscore indexes of ' + self.team + '.')
        
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

        # seperate the points scored (target data) into seperate dataframes
        target_points_df = pd.DataFrame()
        df_columns = pd.DataFrame()
        
        df_columns = training_games_df[['home_points' + str(self.n_games - 1), 'away_points' + str(self.n_games - 1)]]
        target_points_df = target_points_df.append(df_columns, ignore_index=True, sort=False)
        self.target_points = target_points_df

        # filter out the most recent (target) game from the training data
        training_games_df = training_games_df.filter(regex=r'.*(?<!' + str(self.n_games - 1) + ')$')
        self.training_games = training_games_df

        print('Seperated points scored from ' + self.team + "'s dataframe.")
        
        # retreive training games pickle and add acquired dataframes to it
        loaded_games_df = pd.DataFrame()

        try:
            games_pickle_file = open('training_games_pickles\\' + self.team + random_date + '_games_pickle.txt', 'rb')
            loaded_games_df = pickle.load(games_pickle_file)
            games_pickle_file.close()

        except:
            games_pickle_file = open('training_games_pickles\\' + self.team + random_date + '_games_pickle.txt', 'wb')
            games_pickle_file.close()

        loaded_games_df = loaded_games_df.append(training_games_df, ignore_index=True, sort=False)

        games_pickle_file = open('training_games_pickles\\' + self.team + random_date + '_games_pickle.txt', 'wb')
        pickle.dump(loaded_games_df, games_pickle_file)
        games_pickle_file.close()


# initial conditions to capture NBA data
team_abbrev = list(['ATL', 'BOS', 'BRK', 'CHI', 'CHO', 'CLE', 'DAL', 'DEN', 'DET', 'GSW', 'HOU', 'IND', 'LAC',
            'LAL', 'MEM', 'MIA', 'MIN', 'NOP', 'NYK', 'OKC', 'PHI', 'PHO', 'SAC', 'SAS', 'TOR', 'UTA', 'WAS'])

year = '2019' # ex: 2020 as in the 2019-2020 season
n_games = 10

# gather multiple dataframes for different teams in same year
for i in range(10):
    for team in team_abbrev:
        team = Team(team)
        team.gatherdf(year, n_games)
        print(team.training_games)