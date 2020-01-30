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

# initial conditions to capture NBA data
team_abbrev = list(['ATL', 'BOS', 'BRK', 'CHI', 'CHO', 'CLE', 'DAL', 'DEN', 'DET', 'GSW', 'HOU', 'IND', 'LAC',
            'LAL', 'MEM', 'MIA', 'MIN', 'NOP', 'NYK', 'OKC', 'PHI', 'PHO', 'SAC', 'SAS', 'TOR', 'UTA', 'WAS'])

year = '2019'

# generate a random date to start getting games from
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
        day = '0' + str(rand.randint(1, 9))

    else:
        day = rand.randint(1, 30)

        if day in range(1, 10):
            day = '0' + str(day)
        else:
            day = str(day)

    # assign the random date from previous findings
    global random_date
    random_date = year + '-' + month + '-' + day
    '''
    # retreive training date pickle and check if the same random date had been generated before
    try:
        date_pickle_file = open('training_date_pickle_files\\' + year + '_training_date_pickle.txt', 'rb')
        random_date_list = pickle.load(date_pickle_file)
        date_pickle_file.close()

    except:
        date_pickle_file = open('training_date_pickle_files\\' + year + '_training_date_pickle.txt', 'wb')
        date_pickle_file.close()
        date_pickle_file = open('training_date_pickle_files\\' + year + '_training_date_pickle.txt', 'rb')

        try:
            random_date_list = pickle.load(date_pickle_file)
            date_pickle_file.close()

        except:
            date_pickle_file.close()
            random_date_list = list()

    if random_date not in random_date_list:
        random_date_list.append(random_date)

    else:
        date_generator()

    date_pickle_file = open('training_date_pickle_files\\' + year + '_training_date_pickle.txt', 'wb')
    pickle.dump(random_date_list, date_pickle_file)
    date_pickle_file.close()
    '''
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

date_generator()

class Team():

    '''Creates a Team class that stores the schedule of games and boxscore indexes of each selected team for the given year. '''

    def __init__(self, team):
        self.team = team
    
    # gather dataframes from previous specified number of games and year
    def gatherdf(self, year, n_games):
        self.year = year
        self.n_games = n_games
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
                    multiple_index_counts = index_counts[::-1]
                    multiple_index_counts = multiple_index_counts[(82-position):((82-position) + self.n_games)]

                    index_counter = 1

        # use index counts to find positions of boxscore indexes
        multiple_positions = list()
        self.multiple_indexes = list()

        for index_count in multiple_index_counts:
            multiple_positions.append(index_counts.index(index_count))

        for position in multiple_positions:
            self.multiple_indexes.append(indexes[position])

        print('Found last ' + str(self.n_games) + ' boxscore indexes of ' + self.team + '.')
        
        # use boxscore indexes to retreive each game's dataframe
        boxscore_list = list()
        dataframe_list = list()

        for i in range(self.n_games):
            boxscore_list.append(Boxscore(self.multiple_indexes[i]))
    
            dataframe_list.append(boxscore_list[i].dataframe)

            dataframe_list[i].drop(columns=['winning_name', 'winning_abbr', 'winner',
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

        print(new_df_value_list)
        all_games_df = pd.DataFrame(data=new_df_value_list[0], columns=dataframe_column_list, index=[0])

        print(all_games_df)

        #all_games_df.insert(0, dataframe_column_list, dataframe_list[0])

        #all_games_df = all_games_df.append(dataframe_list[0], ignore_index=True, sort=False)
        #for i in range(1, self.n_games):
        #all_games_df.loc[0] = dataframe_list[6]

        
        # seperate points scored from each game's dataframe
        all_points_df = pd.DataFrame()
        df_columns = pd.DataFrame()
        
        df_columns = all_games_df[['home_points0', 'away_points0', 'home_points1', 'away_points1', 'home_points2', 'away_points2',
                            'home_points3', 'away_points3', 'home_points4', 'away_points4', 'home_points5', 'away_points5', 'away_points7',
                            'home_points6', 'away_points6', 'home_points7', 'home_points8', 'away_points8', 'home_points9', 'away_points9']]

        all_points_df = all_points_df.append(df_columns, ignore_index=True, sort=False)
        print(all_points_df)
        print('Seperated points scored from ' + self.team + "'s dataframe.")
        '''
        # retreive training games pickle and add acquired dataframes to it
        loaded_games_df = pd.DataFrame()

        try:
            games_pickle_file = open('training_games_pickle_files\\' + random_date + '_games_pickle.txt', 'rb')
            loaded_games_df = pickle.load(games_pickle_file)
            games_pickle_file.close()

        except:
            games_pickle_file = open('training_games_pickle_files\\' + random_date + '_games_pickle.txt', 'wb')
            games_pickle_file.close()
            games_pickle_file = open('training_games_pickle_files\\' + random_date + '_games_pickle.txt', 'rb')

            try:
                loaded_games_df = pickle.load(games_pickle_file)
                games_pickle_file.close()

            except:
                games_pickle_file.close()

        loaded_games_df = loaded_games_df.append(all_games_df, ignore_index=True)

        games_pickle_file = open('training_games_pickle_files\\' + random_date + '_games_pickle.txt', 'wb')
        pickle.dump(loaded_games_df, games_pickle_file)
        games_pickle_file.close()
        '''
# test the team class using the sixers
sixers = Team('PHI')

sixers.gatherdf(year, 10)