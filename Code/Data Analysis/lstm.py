# These are all to be used for lstm and data analysis.
import csv
import math
import pandas
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from sklearn.utils import shuffle

# fix random seed so this can be reproduced
np.random.seed(7)
random.seed(7)
# setting some specifications for model based on data ** update vals **
num_features = 0
batch_size = 0
time_steps = 0

# clean up the data (remove outliers) and normalize the dataset
def clean_data():
    # caitlin is writing this!

# sets the header to row 0, skips the header row, and excludes the first two columns
# with the sensor and motor times
data = pd.read_csv("combined_dataset1.csv", header = 0, skiprows = [0], usecols = [2:])
dataset = clean_data(data)

# split the data into train and test set (depending on the size of the data,
# we can set aside data from train to use for validation) 80% for training 20%
# for testing and 12% of that training for validation
# Percentages for training data: 85% of training data (68% of total data) for pure testing,
#                                15% of training data (12% of total data) for validation
train_size = int(dataset.shape[0] * 0.80)

# convert the array of values into a dataset matrix
# reshape the data
train, test = dataset[0:train_size, :], dataset[train_size: len(dataset), :]

scaler = MinMaxScaler(feature_range = (-1, 1))
scaler = scaler.fit(train)

# create and fit the lstm model

# make predictions
# invert predictions

# calculate root mean squared error

# shift train predictions for plotting
# shift test predictions for plotting

# plot baseline and predictions
