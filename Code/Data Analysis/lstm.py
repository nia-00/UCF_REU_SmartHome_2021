# These are all to be used for lstm and data analysis.
import os
import csv
import math
import random
import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
import tensorflow.keras as keras
from keras import layers
from sklearn import preprocessing
from sklearn.utils import shuffle
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, Dense, GRU, Embedding
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint, TensorBoard, ReduceLROnPlateau
from tensorflow.keras.backend import square, mean

# make dict of all input files and names
comb_files_dict = {1: 'charlotte_sim_1_cooltoofast_combined.csv', 2: 'charlotte_sim_1_lowpeaktemp_combined.csv',
                   3: 'charlotte_sim_sucessful_combined.csv', 4: 'charlotte_sim_2_combined.csv',
                   5: 'charlotte_sim_2_v2_combined.csv', 6: 'charlotte_sim_3_combined.csv',
                   7: 'denver_sim_1_combined.csv', 8: 'detroit_sim_1_combined.csv'
                   9: 'detroit_sim_2_incomplete_combined.csv', 10: 'detroit_sim_3_combined.csv',
                   11: 'jacksonville_sim_1_combined.csv', 12: 'jacksonville_sim_2_combined.csv',
                   13: 'jacksonville_sim_3_combined.csv', 14: 'lasvegas_sim_1_combined.csv',
                   15: 'lasvegas_sim_2_combined.csv'}

# fix random seed so this can be reproduced
seed_val = 7
def reset_random_seeds():
    tf.random.set_seed(seed_val)
    np.random.seed(seed_val)
    random.seed(seed_val)

# setting some specifications for model based on data ** update vals **
num_features = 0
batch_size = 180
time_steps = 0
sequence_length = 20
shift_steps = 20

# sets the header to row 0, skips the header row, and excludes the first two columns
# with the sensor and motor times
df = pd.read_csv("combined_dataset1.csv", header = 0, skiprows = [0], usecols = [2:])
dataset = df.values
# make sure all the data is of the same type
dataset = dataset.astype('float32')
# shift the y data
target_names = ['S4_Temperature','S6_Temperature', 'S12_Temperature', 'S18_Temperature', 'S19_Temperature', 'S24_Temperature', 'S25_Temperature', 'S26_Temperature']
df_targets = data[][target_names].shift(-shift_steps)
# normalize dataset
scaler = MinMaxScaler(feature_range = (0, 1))
scale = scaler.fit_transform(values)
# split the data into train and test set (depending on the size of the data,
# we can set aside data from train to use for validation) 80% for training 20%
# for testing and 12% of that training for validation
# Percentages for training data: 85% of training data (68% of total data) for pure testing,
#                                15% of training data (12% of total data) for validation
train_size = int(dataset.shape[0] * 0.80)

# convert the array of values into a dataset matrix

# reshape the data
x_train, x_test = dataset[0:train_size, :], dataset[train_size: len(dataset), :]


# get the batches of data from larger dataset
def batch_generator(batch_size, sequence_length):
    while True:
        x_shape = (batch_size, sequence_length, num_x_signals)
        x_batch = np.zeros(shape = x_shape, dtype = np.float32)

        y_shape = (batch_size, sequence_length, num_y_signals)
        y_batch = np.zeros(shape = x_shape, dtype = np.float32)

    for i in range(batch_size):
        idx = np.random.randint(num_train - sequence_length)

        x_batch[i] = x_train_scaled[idx:idk+sequence_length]
        y_batch[i] = y_train_scaled[idx:idk+sequence_length]

    yield (x_batch, y_batch)
# create and fit the lstm model

# make predictions
# invert predictions

# calculate root mean squared error

# shift train predictions for plotting
# shift test predictions for plotting

# plot baseline and predictions
