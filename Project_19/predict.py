# create script to predict closing stock prices based on S&P 500 historical data

# imports
import pandas as pd
import numpy as np
from datetime import datetime
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# read in the data
stocks = pd.read_csv('sphist.csv')
# convert Date column to datetime
stocks['Date'] = pd.to_datetime(stocks['Date'])
# sort the df on the Date column in ascending order
stocks = stocks.sort_values('Date')

# compute indicators that take advantage of our time series data
# average price for past five days
stocks['avg_price_last_5'] = stocks['Close'].rolling(5).mean()
# average price for last year (approx 252 trading days)
stocks['avg_price_last_year'] = stocks['Close'].rolling(252).mean()
# stdev of price for past five days
stocks['stdev_price_last_5'] = stocks['Close'].rolling(5).std()
# ratio of avg last 5 to avg last year
stocks['avg_ratio'] = stocks['avg_price_last_5'] / stocks['avg_price_last_year']

# the above are calculated as of last date in range, move to next date
stocks['avg_price_last_5'] = stocks['avg_price_last_5'].shift(periods=1, axis=0)
stocks['avg_price_last_year'] = stocks['avg_price_last_year'].shift(periods=1, axis=0)
stocks['stdev_price_last_5'] = stocks['stdev_price_last_5'].shift(periods=1, axis=0)
stocks['avg_ratio'] = stocks['avg_ratio'].shift(periods=1, axis=0)

# add columns for day of the week
# apply weekday function (0=Monday, 1=Tuesday, etc.) to get day
stocks['weekday'] = stocks['Date'].apply(lambda x: x.weekday())
# create dummy variables
weekday_dummies = pd.get_dummies(stocks['weekday'], prefix='weekday')
# concatenate with original df
stocks = pd.concat([stocks, weekday_dummies], axis=1)
# drop the weekday column and only keep the dummies
stocks = stocks.drop(['weekday'], axis=1)

# remove any rows before January 3, 1951 (b/c of one year rolling avg above)
stocks = stocks[stocks['Date'] > datetime(year=1951, month=1, day=2)]
# drop any rows with missing values
stocks = stocks.dropna(axis=0)

# generate train and test dataframes
# train for dates before January 1, 2013
train = stocks[stocks['Date'] < datetime(year=2013, month=1, day=1)]
# test for dates on or after January 1, 2013
test = stocks[stocks['Date'] >= datetime(year=2013, month=1, day=1)]

# define features columns
# small model features - only three columns
features_small = ['avg_price_last_5', 'avg_price_last_year', 'stdev_price_last_5']
# all features
features = ['avg_price_last_5', 'avg_price_last_year', 'stdev_price_last_5', 'avg_ratio', 'weekday_0', 'weekday_1', 'weekday_2', 'weekday_3', 'weekday_4']
# target is closing price
target = ['Close']

# initialize the model
model_small = LinearRegression()
# train the small model
model_small.fit(train[features_small], train[target])
# make predictions with this model
predictions_small = model_small.predict(test[features_small])
# calculate error (using mean_squared_error)
rmse_small = mean_squared_error(test[target], predictions_small) ** (1/2)
print('RMSE small model: ', rmse_small)

# repeat the analysis using all of the features
model = LinearRegression()
model.fit(train[features], train[target])
predictions = model.predict(test[features])
rmse = mean_squared_error(test[target], predictions) ** (1/2)
print('RMSE full model: ', rmse)
