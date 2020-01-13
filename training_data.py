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

# get random team's full schedule and boxscore indexes
team_abbrev = list(['ATL', 'BKN', 'BOS', 'CHA', 'CHI', 'CLE', 'DAL', 'DEN', 'DET', 'GSW', 'HOU', 'IND', 'LAC',
            'LAL', 'MEM', 'MIA', 'MIN', 'NOP', 'NYK', 'OKC', 'PHI', 'PHX', 'SAC', 'SAS', 'TOR', 'UTA', 'WAS'])

for team in team_abbrev:
    target_team = team
    target_team_schedule = Schedule(target_team)
    target_team_indexes = list()

    print('Acquired team schdeule.')

    for game in target_team_schedule:
        target_team_indexes.append(game.boxscore_index)

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
        count += int(date[8:10])

        return count

    # run random date through converter
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
    target_team_index_counts = list()

    for i in target_team_indexes:
        target_team_index_counts.append(indexconverter(i))

    # compare dates and find previous five game dates
    target_index_counter = 0

    for count in target_team_index_counts:
        if target_index_counter == 0:
            if current_date_count <= count:
                position = target_team_index_counts.index(count)

                # use index counts to find positions of Boxscore indexes

                target_team_five_index_counts = target_team_index_counts[::-1]
                target_team_five_index_counts = target_team_five_index_counts[(82-position):((82-position)+5)]

                target_index_counter = 1

    # use index counts to find positions of Boxscore indexes
    target_team_five_pos = list()
    target_team_five_indexes = list()

    for index_count in target_team_five_index_counts:
        target_team_five_pos.append(target_team_index_counts.index(index_count))

    for position in target_team_five_pos:
        target_team_five_indexes.append(target_team_indexes[position])

    print('Found boxscore indexes of team.')

    # store each Boxscore
    first_game = Boxscore(target_team_five_indexes[0])
    second_game = Boxscore(target_team_five_indexes[1])
    third_game = Boxscore(target_team_five_indexes[2])
    fourth_game = Boxscore(target_team_five_indexes[3])
    fifth_game = Boxscore(target_team_five_indexes[4])

    # create boolean list to show if target team is home
    home_list = list([False, False, False, False, False])

    for index in target_team_five_indexes:
        if target_team in index:
            home_list[target_team_five_indexes.index(index)] = True

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

    target_five_games_df = first_game_df
    target_five_games_df = target_five_games_df.append(second_game_df, ignore_index=True)
    target_five_games_df = target_five_games_df.append(third_game_df, ignore_index=True)
    target_five_games_df = target_five_games_df.append(fourth_game_df, ignore_index=True)
    target_five_games_df = target_five_games_df.append(fifth_game_df, ignore_index=True)

    for_game_list = list([first_game, second_game, third_game, fourth_game, fifth_game])
    target_five_games_points_df = pd.DataFrame()

    for game in for_game_list:
        target_five_games_points_df = target_five_games_points_df.append(game.dataframe[['home_points', 'away_points']], ignore_index=True)

    print('Gathered 5 game stats and seperated points of team.')