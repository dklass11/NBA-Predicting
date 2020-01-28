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

# get random team's full schedule and boxscore indexes
team_abbrev = list(['ATL', 'BOS', 'BRK', 'CHI', 'CHO', 'CLE', 'DAL', 'DEN', 'DET', 'GSW', 'HOU', 'IND', 'LAC',
            'LAL', 'MEM', 'MIA', 'MIN', 'NOP', 'NYK', 'OKC', 'PHI', 'PHO', 'SAC', 'SAS', 'TOR', 'UTA', 'WAS'])

year = '2019'

# generate random date
def date_generator():
    chance = rand.randint(1, 2)

    if chance == 1:
        month = '0' + str(rand.randint(1, 4))

    else: 
        month = str(rand.randint(11, 12))
        
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
        day = '0' + str(rand.randint(1, 10))

    else:
        day = rand.randint(1, 30)

        if day in range(1, 10):
            day = '0' + str(day)
        else:
            day = str(day)

    global random_date
    random_date = year + '-' + month + '-' + day

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

    global random_date_count
    random_date_count = dateconverter(random_date)

    print('Generated random date: ' + random_date)

date_generator()




class Team():

    '''Creates a Team class that stores the schedule of games and boxscore indexes of each selected team for the given year. '''

    def __init__(self, team, year, n_games):
        self.team = team
        self.year = year
        self.schedule = Schedule(self.team, year=year) #target_team_schedule
        self.n_games = n_games

        print('Acquired ' + self.team + "'s " + 'schdeule.')

        indexes = list() #target_team_indexes
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
        index_counts = list() #target_team_index_counts

        for index in indexes:
            index_counts.append(indexconverter(index))

        # compare dates and find previous specified numnber of game dates
        index_counter = 0 #target_index_counter
        
        for count in index_counts:
            if index_counter == 0:
                if random_date_count <= count:
                    position = index_counts.index(count)

                    # use index counts to find positions of Boxscore indexes
                    multiple_index_counts = index_counts[::-1]
                    multiple_index_counts = multiple_index_counts[(82-position):((82-position) + self.n_games)]

                    index_counter = 1

        # use index counts to find positions of Boxscore indexes
        multiple_positions = list()
        self.multiple_indexes = list() #target_team_ten_indexes

        for index_count in multiple_index_counts:
            multiple_positions.append(index_counts.index(index_count))

        for position in multiple_positions:
            self.multiple_indexes.append(indexes[position])

        print('Found last ' + str(self.n_games) + ' boxscore indexes of ' + self.team)
        
        boxscore_list = list()
        dataframe_list = list()
        all_games_df = pd.DataFrame()

        for i in range(self.n_games):
            boxscore_list.append(Boxscore(self.multiple_indexes[i]))
    
            dataframe_list.append(boxscore_list[i].dataframe)

            dataframe_list[i].drop(columns=['winning_name', 'winning_abbr', 'winner',
                                        'losing_name', 'losing_abbr', 'home_wins',
                                        'away_wins', 'date', 'location'])

            all_games_df.append(dataframe_list[i], ignore_index=True, sort=False)
        
        for iterable, df in enumerate(all_games_df):
            for column in df:
                df.rename(columns={column: str(column) + str(int(iterable)+2)}, inplace=True)

phi = Team('PHI', year, 10)

'''
for team in team_abbrev:
    target_team_schedule = Schedule(team, year=year)
    target_team_indexes = list()

    print('Acquired ' + team + "'s " + 'schdeule.')

    for game in target_team_schedule:
        target_team_indexes.append(game.boxscore_index)

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
    target_team_index_counts = list()

    for i in target_team_indexes:
        target_team_index_counts.append(indexconverter(i))

    # compare dates and find previous ten game dates
    target_index_counter = 0
    
    for count in target_team_index_counts:
        if target_index_counter == 0:
            if random_date_count <= count:
                position = target_team_index_counts.index(count)

                # use index counts to find positions of Boxscore indexes
                target_team_ten_index_counts = target_team_index_counts[::-1]
                target_team_ten_index_counts = target_team_ten_index_counts[(82-position):((82-position)+10)]

                target_index_counter = 1

    # use index counts to find positions of Boxscore indexes
    target_team_ten_pos = list()
    target_team_ten_indexes = list()

    for index_count in target_team_ten_index_counts:
        target_team_ten_pos.append(target_team_index_counts.index(index_count))

    for position in target_team_ten_pos:
        target_team_ten_indexes.append(target_team_indexes[position])

    print('Found boxscore indexes of ' + team)
    
    # store each Boxscore
    first_game = Boxscore(target_team_ten_indexes[0])
    second_game = Boxscore(target_team_ten_indexes[1])
    third_game = Boxscore(target_team_ten_indexes[2])
    fourth_game = Boxscore(target_team_ten_indexes[3])
    fifth_game = Boxscore(target_team_ten_indexes[4])
    sixth_game = Boxscore(target_team_ten_indexes[5])
    seventh_game = Boxscore(target_team_ten_indexes[6])
    eighth_game = Boxscore(target_team_ten_indexes[7])
    ninth_game = Boxscore(target_team_ten_indexes[8])
    tenth_game = Boxscore(target_team_ten_indexes[9])

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

    target_ten_games_df = first_game_df

    for_game_df_list = list([second_game_df, third_game_df, fourth_game_df, fifth_game_df,
                    sixth_game_df, seventh_game_df, eighth_game_df, ninth_game_df, tenth_game_df])

    for iterable, gamedf in enumerate(for_game_df_list):
        for column in gamedf:
            gamedf.rename(columns={column: str(column) + str(int(iterable)+2)}, inplace=True)
    
    target_ten_games_df = target_ten_games_df.append(second_game_df, ignore_index=True, sort=False)
    target_ten_games_df = target_ten_games_df.append(third_game_df, ignore_index=True, sort=False)
    target_ten_games_df = target_ten_games_df.append(fourth_game_df, ignore_index=True, sort=False)
    target_ten_games_df = target_ten_games_df.append(fifth_game_df, ignore_index=True, sort=False)
    target_ten_games_df = target_ten_games_df.append(sixth_game_df, ignore_index=True, sort=False)
    target_ten_games_df = target_ten_games_df.append(seventh_game_df, ignore_index=True, sort=False)
    target_ten_games_df = target_ten_games_df.append(eighth_game_df, ignore_index=True, sort=False)
    target_ten_games_df = target_ten_games_df.append(ninth_game_df, ignore_index=True, sort=False)
    target_ten_games_df = target_ten_games_df.append(tenth_game_df, ignore_index=True, sort=False)
    
    for_game_list = list([first_game, second_game, third_game, fourth_game, fifth_game, sixth_game, seventh_game, eighth_game, ninth_game, tenth_game])
    target_ten_games_points_df = pd.DataFrame()
##
for game in for_game_list:
    target_ten_games_points_df = target_ten_games_points_df.append(game.dataframe[['home_points', 'away_points']], ignore_index=True)

print('Gathered past 10 game stats and seperated points of ' + team)

loaded_ten_games_df = pd.DataFrame()

try:
    ten_games_pickle_file = open('training_data_pickle_files\\' + random_date + '_ten_games_pickle.txt', 'rb')
    loaded_ten_games_df = pickle.load(ten_games_pickle_file)
    ten_games_pickle_file.close()

except:
    ten_games_pickle_file = open('training_data_pickle_files\\' + random_date + '_ten_games_pickle.txt', 'wb')
    ten_games_pickle_file.close()
    ten_games_pickle_file = open('training_data_pickle_files\\' + random_date + '_ten_games_pickle.txt', 'rb')

    try:
        loaded_ten_games_df = pickle.load(ten_games_pickle_file)
        ten_games_pickle_file.close()

    except:
        ten_games_pickle_file.close()

loaded_ten_games_df = loaded_ten_games_df.append(target_ten_games_df, ignore_index=True)

ten_games_pickle_file = open('training_data_pickle_files\\' + random_date + '_ten_games_pickle.txt', 'wb')
pickle.dump(loaded_ten_games_df, ten_games_pickle_file)
ten_games_pickle_file.close()
'''