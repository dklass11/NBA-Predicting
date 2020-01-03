from sportsreference.nba.teams import Teams

teams = Teams()

for team in teams:
    print(team.name)
    print(team.games_played)