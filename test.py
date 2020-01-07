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