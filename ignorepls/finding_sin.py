import csv
# from datetime import datetime
import datetime

import numpy as np
import pandas as pd
# "C:\Users\welcm\Documents\smartHome\charlotte_sim_1_cooltoofast_combined_interpolated.csv"
import matplotlib.pyplot as plt


#r_file = input("Input read file: ")
r_file = "C:/Users/welcm/PycharmProjects/.smartHomeFiles/lasvegas_sim_1_complete_time.csv"
#r_file = r_file.replace('\\', '/')
#r_file = r_file.replace('"', '')
w_file = r_file.replace("combined_interpolated", "complete_timed")
print("Read file: ", r_file)
print("Write file: ", w_file)
# Save first columns of sensors time to df
df = pd.read_csv(r_file, sep=',', header=0, usecols=[0])

# Convert times to timedelta so that we can use dt.total_seconds
df['Time'] = pd.to_timedelta(df['Time'])
# Convert all sensor timestamps to seconds
timestamp_s = df['Time'].dt.total_seconds()
print(timestamp_s)

#date_time = pd.to_datetime(df.pop('Time'), format='%H:%M:%S')
#timestamp_s = date_time.map(pd.Timestamp.timestamp)
#print(timestamp_s)
#timestamp_s
# Convert seconds to a usable "time of day" signal
day = 24*60*60
df['Day sin'] = np.sin(timestamp_s * (2 * np.pi / day))
df['Day cos'] = np.cos(timestamp_s * (2 * np.pi / day))
plt.plot(np.array(df['Day sin'])[:15])
plt.plot(np.array(df['Day cos'])[:15])
plt.xlabel('Time [h]')
plt.title('Time of day signal')

plt.savefig('plot6.png')
print("hi")
