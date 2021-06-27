import csv
#from datetime import datetime
import datetime

import numpy as np
import pandas as pd
import pdb
# "C:\Users\welcm\Documents\smartHome\charlotte_sim_1_cooltoofast_combined_interpolated.csv"
import matplotlib.pyplot as plt

'''
#r_file = input("Input read file: ")

r_file = "C:/Users/welcm/Documents/smartHome/charlotte_sim_1_cooltoofast_combined_interpolated.csv"

#r_file = r_file.replace('\\', '/')
#r_file = r_file.replace('"', '')

w_file = r_file.replace("combined_interpolated", "complete_timed")

print("Read file: ", r_file)
print("Write file: ", w_file)

# Save first columns of sensors time to df
df = pd.read_csv(r_file, sep=',', header=0, usecols=[0])

# Convert times to timedelta so that we can use dt.total_seconds
df['Sensor Time'] = pd.to_timedelta(df['Sensor Time'])
# Convert all sensor timestamps to seconds
df['Sensor Time'] = df['Sensor Time'].dt.total_seconds()

pdb.set_trace()

date_time = pd.to_datetime(df.pop('Sensor Time'), format='%H:%M:%S')
timestamp_s = date_time.map(pd.Timestamp.timestamp)
print(timestamp_s)

#timestamp_s

# Convert seconds to a usable "time of day" signal
day = 24*60*60
df['Day sin'] = np.sin(timestamp_s * (2 * np.pi / day))
df['Day cos'] = np.cos(timestamp_s * (2 * np.pi / day))

plt.plot(np.array(df['Day sin'])[:15])
plt.plot(np.array(df['Day cos'])[:15])
plt.xlabel('Time [h]')
plt.title('Time of day signal')
print("hi")

'''

r_file = "C:/Users/welcm/Documents/smartHome/charlotte_sim_1_cooltoofast_combined_interpolated.csv"
w_file = r_file.replace("combined_interpolated", "TESTING_TIMES")
print("Read file: ", r_file)
print("Write file: ", w_file)

file_read = pd.read_csv(r_file)

sensor_time = file_read['Sensor Time']
motor_time = file_read['Motor Time']

# Turn the inputs into a list for easy traversal
sensor_time = list(sensor_time)
motor_time = list(motor_time)
earlier_time = []


for time in sensor_time:
    time = datetime.datetime.strptime(time, '%H:%M:%S')

for time in motor_time:
    time = datetime.datetime.strptime(time, '%H:%M:%S')

for x in range(len(sensor_time)):
    if sensor_time[x] < motor_time[x]:
        print("This is sensor time at index ", x)
        earlier_time.append(sensor_time[x])
    elif motor_time[x] < sensor_time[x]:
        print("This is motor time at index ", x)
        earlier_time.append(motor_time[x])
    else:
        print("This is shared time at index ", x)
        earlier_time.append(motor_time[x])

print(earlier_time)





'''


print(df['Sensor Time'])

'''

'''
# You should never directly modifying data you are iterating through according to
# pandas 0.19.1 docs, hence we are using a list to preform operations
time_in_seconds = recorded_times.values.tolist()

for index, time in enumerate(time_in_seconds):
    for element in time:
        print("FIRST TIME: ", time[0])
        print(element)

    #if index == len(time_in_seconds):
    #    break
    #time[index] = time[index] - time[0]
    #print(time[index], '=', time[index], '-', time[0])


#for index, time in recorded_times.itertuples():
#    recorded_times[index] = recorded_times[index] - recorded_times[0]

#print(recorded_times)
'''