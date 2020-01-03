# import needed modules
import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense

# read in NBA 2018 team stats
nba2018_df_initial = pd.read_csv('NBA2018Stats.csv')

# read in NBA 2019 team stats
nba2019_df_initial = pd.read_csv('NBA2019Stats.csv')

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

'''
# repeat for 2017 stats

nba2017_df_initial = pd.read_csv('NBA2017Stats.csv')

nba2017_df = nba2017_df_initial.drop(columns=['W','L','TEAM','WIN%','GP'])

nba2017_wins = nba2017_df_initial[['W']]

model1 = Sequential()

model1.add(Dense(24, activation='relu', input_shape=(n_cols,)))
model1.add(Dense(100, activation='relu'))
model1.add(Dense(100, activation='relu'))
model1.add(Dense(100, activation='relu'))
model1.add(Dense(100, activation='relu'))
model1.add(Dense(100, activation='relu'))
model1.add(Dense(1))

model1.compile(optimizer='adam', loss='mean_squared_error')

model1.fit(nba2017_df, nba2017_wins, validation_split=0.1, epochs=1000)

predicted_wins1 = model1.predict(nba2019_df)

predicted_wins_gp1 = predicted_wins1 * nba2019_gp_array_percent
predicted_wins_gp_rounded1 = np.round(predicted_wins_gp1, 0)

final_array1 = np.hstack([team_names_array, predicted_wins_gp_rounded1])

print(final_array1)


# repeat for 2016 stats

nba2016_df_initial = pd.read_csv('NBA2016Stats.csv')

nba2016_df = nba2016_df_initial.drop(columns=['W','L','TEAM','WIN%','GP'])

nba2016_wins = nba2016_df_initial[['W']]

model2 = Sequential()

model2.add(Dense(24, activation='relu', input_shape=(n_cols,)))
model2.add(Dense(100, activation='relu'))
model2.add(Dense(100, activation='relu'))
model2.add(Dense(100, activation='relu'))
model2.add(Dense(100, activation='relu'))
model2.add(Dense(100, activation='relu'))
model2.add(Dense(1))

model2.compile(optimizer='adam', loss='mean_squared_error')

model2.fit(nba2016_df, nba2016_wins, validation_split=0.1, epochs=1000)

predicted_wins2 = model2.predict(nba2019_df)

predicted_wins_gp2 = predicted_wins2 * nba2019_gp_array_percent
predicted_wins_gp_rounded2 = np.round(predicted_wins_gp2, 0)

final_array2 = np.hstack([team_names_array, predicted_wins_gp_rounded2])

print(final_array2)


# repeat for 2015 stats

nba2015_df_initial = pd.read_csv('NBA2015Stats.csv')

nba2015_df = nba2015_df_initial.drop(columns=['W','L','TEAM','WIN%','GP'])

nba2015_wins = nba2015_df_initial[['W']]

model3 = Sequential()

model3.add(Dense(24, activation='relu', input_shape=(n_cols,)))
model3.add(Dense(100, activation='relu'))
model3.add(Dense(100, activation='relu'))
model3.add(Dense(100, activation='relu'))
model3.add(Dense(100, activation='relu'))
model3.add(Dense(100, activation='relu'))
model3.add(Dense(1))

model3.compile(optimizer='adam', loss='mean_squared_error')

model3.fit(nba2015_df, nba2015_wins, validation_split=0.1, epochs=1000)

predicted_wins3 = model3.predict(nba2019_df)

predicted_wins_gp3 = predicted_wins3 * nba2019_gp_array_percent
predicted_wins_gp_rounded3 = np.round(predicted_wins_gp3, 0)

final_array3 = np.hstack([team_names_array, predicted_wins_gp_rounded3])

print(final_array3)


# repeat for 2014 stats

nba2014_df_initial = pd.read_csv('NBA2014Stats.csv')

nba2014_df = nba2014_df_initial.drop(columns=['W','L','TEAM','WIN%','GP'])

nba2014_wins = nba2014_df_initial[['W']]

model4 = Sequential()

model4.add(Dense(24, activation='relu', input_shape=(n_cols,)))
model4.add(Dense(100, activation='relu'))
model4.add(Dense(100, activation='relu'))
model4.add(Dense(100, activation='relu'))
model4.add(Dense(100, activation='relu'))
model4.add(Dense(100, activation='relu'))
model4.add(Dense(1))

model4.compile(optimizer='adam', loss='mean_squared_error')

model4.fit(nba2014_df, nba2014_wins, validation_split=0.1, epochs=1000)

predicted_wins4 = model4.predict(nba2019_df)

predicted_wins_gp4 = predicted_wins4 * nba2019_gp_array_percent
predicted_wins_gp_rounded4 = np.round(predicted_wins_gp4, 0)

final_array4 = np.hstack([team_names_array, predicted_wins_gp_rounded4])

print(final_array4)


# repeat for 2013 stats

nba2013_df_initial = pd.read_csv('NBA2013Stats.csv')

nba2013_df = nba2013_df_initial.drop(columns=['W','L','TEAM','WIN%','GP'])

nba2013_wins = nba2013_df_initial[['W']]

model5 = Sequential()

model5.add(Dense(24, activation='relu', input_shape=(n_cols,)))
model5.add(Dense(100, activation='relu'))
model5.add(Dense(100, activation='relu'))
model5.add(Dense(100, activation='relu'))
model5.add(Dense(100, activation='relu'))
model5.add(Dense(100, activation='relu'))
model5.add(Dense(1))

model5.compile(optimizer='adam', loss='mean_squared_error')

model5.fit(nba2013_df, nba2013_wins, validation_split=0.1, epochs=1000)

predicted_wins5 = model5.predict(nba2019_df)

predicted_wins_gp5 = predicted_wins5 * nba2019_gp_array_percent
predicted_wins_gp_rounded5 = np.round(predicted_wins_gp5, 0)

final_array5 = np.hstack([team_names_array, predicted_wins_gp_rounded5])

print(final_array5)


# separate games won from 2019 data
nba2019_wins = nba2019_df_initial[['W']]
nba2019_wins_array = nba2019_wins.to_numpy()

# compare each network's win totals to 2019 wins
compared_wins_2018 = predicted_wins_gp_rounded0 / nba2019_wins_array
compared_wins_2018 = compared_wins_2018 - 1
compared_wins_2018 = np.absolute(compared_wins_2018)
print(compared_wins_2018)

compared_wins_2017 = predicted_wins_gp_rounded0 / nba2019_wins_array
compared_wins_2017 = compared_wins_2017 - 1
compared_wins_2017 = np.absolute(compared_wins_2017)
print(compared_wins_2017)

compared_wins_2016 = predicted_wins_gp_rounded0 / nba2019_wins_array
compared_wins_2016 = compared_wins_2016 - 1
compared_wins_2016 = np.absolute(compared_wins_2016)
print(compared_wins_2016)

compared_wins_2015 = predicted_wins_gp_rounded0 / nba2019_wins_array
compared_wins_2015 = compared_wins_2015 - 1
compared_wins_2015 = np.absolute(compared_wins_2015)
print(compared_wins_2015)

compared_wins_2014 = predicted_wins_gp_rounded0 / nba2019_wins_array
compared_wins_2014 = compared_wins_2014 - 1
compared_wins_2014 = np.absolute(compared_wins_2014)
print(compared_wins_2014)

compared_wins_2013 = predicted_wins_gp_rounded0 / nba2019_wins_array
compared_wins_2013 = compared_wins_2013 - 1
compared_wins_2013 = np.absolute(compared_wins_2013)
print(compared_wins_2013)
'''