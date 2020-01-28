from sportsreference.nba.teams import Teams
from sportsreference.nba.boxscore import Boxscore
from sportsreference.nba.boxscore import Boxscores
from sportsreference.nba.schedule import Schedule
from datetime import datetime

teams = Teams()
print('\nnew run\n')

'''
for team in teams:
    print(team.name)
    print(team.games_played)
'''

specificgame = Boxscore('202001050LAC')
print("\n" + str(specificgame.home_blocks))

phila_schedule = Schedule('PHI')

for i in phila_schedule:
    if i.date == "Tue, Nov 12, 2019":
        print(i.boxscore_index)
        print(i.dataframe)

game2018 = Boxscore('201810160BOS')

print(game2018.winner)

'''
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

target1_converted_abbr_l = list()

letter_number_dicionary = {'A':'01', 'B':'02', 'C':'03', 'D':'04', 'E':'05', 'F':'06', 'G':'07', 'H':'08', 'I':'09', 'J':'10', 'K':'11', 'L':'12', 'M':'13',
                    'N':'14', 'O':'15', 'P':'16', 'Q':'17', 'R':'18', 'S':'19', 'T':'20', 'U':'21', 'V':'22', 'W':'23', 'X':'24', 'Y':'25', 'Z':'26'}

def abbreviation_converter(abbreviations):
    for i in abbreviations:
        for abbrev in i:
            for letter in abbrev:
                pos = letter_number_dicionary[letter]
                target1_converted_abbr_l.append(pos)

abbreviation_converter(target1_five_games_df_w_l)

number1 = ''
number2 = ''
number3 = ''

pos_number1 = True
pos_number2 = False
pos_number3 = False
b = False

number_list = list()

for number in target1_converted_abbr_l:
    print(pos_number1, pos_number2, pos_number3)

    b = True

    if pos_number2 == True:
        number2 = number
        pos_number3 = True
        pos_number2 = False
        b = False

    elif pos_number1 == True:
        number1 = number
        pos_number2 = True
        pos_number1 = False

    elif pos_number3 == True & b == True:
        number3 = number
        pos_number1 = True
        combined_numbers = number1 + number2 + number3
        number_list.append(combined_numbers)
        pos_number3 = False

target1_converted_abbr = pd.DataFrame(number_list, columns="winning_abbr")

'''

'''

# convert schedule dates to count
def dateconverter1(date):
    count = 0

    # convert month to number of days
    if 'Oct' in date:
        count = 0
    elif 'Nov' in date:
        count = 31
    elif 'Dec' in date:
        count = 61
    elif 'Jan' in date:
        count = 92
    elif 'Feb' in date:
        count = 123
    elif 'Mar' in date:
        count = 152 # for this leap year only
    elif 'Apr' in date:
        count = 183

    # find and add number of days
    if date[10] is not ',':
        count += int(date[9:11])
    else:
        count += int(date[9])

    return count

# convert current date to count
def dateconverter2(date):
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

    # find and add number of days
    count += int(date[8:10])

    return count

# run schedulate dates through converter
home_schedule_date_counts = list()

for date in home_team_dates:
    home_schedule_date_counts.append(dateconverter1(date))

# run current date through converter
current_date_count = dateconverter2(str(datetime.date.today()))


# use last five game dates to find uri's
old_home_five_team_uri = list()
month = ''
day = '' 

def home_boxscore_uri_creator(game_dates):
    for date in game_dates:
        # convert month to numeric value
        if 'Oct' in date:
            month = '10'
        elif 'Nov' in date:
            month = '11'
        elif 'Dec' in date:
            month = '12'
        elif 'Jan' in date:
            month = '01'
        elif 'Feb' in date:
            month = '02'
        elif 'Mar' in date:
            month = '03'
        elif 'Apr' in date:
            month = '04'

        # find and pull day number
        if date[10] is not ',':
            day = date[9:11]
        else:
            day = "0" + date[9]

        # add each uri to list
        old_home_five_team_uri.append('2020' + month + day + '0' + home_team) # for this year only

home_boxscore_uri_creator(home_game_date_list)

team_abbrev = list(['ATL', 'BKN', 'BOS', 'CHA', 'CHI', 'CLE', 'DAL', 'DEN', 'DET', 'GSW', 'HOU', 'IND', 'LAC',
            'LAL', 'MEM', 'MIA', 'MIN', 'NOP', 'NYK', 'OKC', 'PHI', 'PHX', 'SAC', 'SAS', 'TOR', 'UTA', 'WAS'])

home_five_team_uri = list()

print(old_home_five_team_uri)

'''

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
        
        for iterable, df in enumerate(dataframe_list):
            for column in df:
                df.rename(columns={column: (str(column) + str(iterable))}, inplace=True)
        
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