# import needed modules
import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense

# read in NBA 2018 team stats
nba2018_df_initial = pd.read_csv('old excel stats\\NBA2018Stats.csv')

# read in NBA 2019 team stats
nba2019_df_initial = pd.read_csv('old excel stats\\NBA2019Stats.csv')

# take out wins and losses from 2019 stats
nba2019_df = nba2019_df_initial.drop(columns=['W','L','TEAM','WIN%','GP'])

# separate games played from 2019 data
nba2019_gp = nba2019_df_initial[['GP']]
nba2019_gp_array = nba2019_gp.to_numpy()

# seperate target data from training data
nba2018_df = nba2018_df_initial.drop(columns=['W','L','TEAM','WIN%','GP'])

# insert target data 
nba2018_wins = nba2018_df_initial[['W']]

# initalize model
model0 = Sequential()

# get number of columns from training data
n_cols = nba2018_df.shape[1]

# create model layers
model0.add(Dense(24, activation='relu', input_shape=(n_cols,)))
model0.add(Dense(100, activation='relu'))
model0.add(Dense(100, activation='relu'))
model0.add(Dense(100, activation='relu'))
model0.add(Dense(100, activation='relu'))
model0.add(Dense(100, activation='relu'))
model0.add(Dense(1))


# compile model
model0.compile(optimizer='adam', loss='mean_squared_error')

# train model
model0.fit(nba2018_df, nba2018_wins, validation_split=0.1, epochs=1000)

# predict based on model's findings
predicted_wins0 = model0.predict(nba2019_df)

# add team names into wins array
team_names_df = nba2018_df_initial[['TEAM']]
team_names_array = team_names_df.to_numpy()

# multiply games played percentages by win totals
nba2019_gp_array_percent = nba2019_gp_array / 82
predicted_wins_gp0 = predicted_wins0 * nba2019_gp_array_percent
predicted_wins_gp_rounded0 = np.round(predicted_wins_gp0, 0)

# concantate team names with predicted wins
final_array0 = np.hstack([team_names_array, predicted_wins_gp_rounded0])

print(final_array0)