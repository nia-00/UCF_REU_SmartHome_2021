import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

r_file = input("Input read file: ")
r_file = r_file.replace('\\', '/')
r_file = r_file.replace('"', '')

# The following maintains our naming convention for this project; change as needed
w_file = r_file.replace("complete", "sin_cos")
print("Read file: ", r_file)
print("Write file: ", w_file)

df = pd.read_csv(r_file, sep=',')

# Changes format of time column so we can use .map
date_time = pd.to_datetime(df.pop(df.columns[0]), format='%H:%M:%S')
# Convert time to seconds
timestamp_s = date_time.map(pd.Timestamp.timestamp)
# Start time at 0 seconds
timestamp_s = timestamp_s - min(timestamp_s)
# Scale all times between 0 and 1
timestamp_s = timestamp_s / max(timestamp_s)
# Our simulations represent a 15-hour period which start at 7am
timestamp_s = (timestamp_s*15*60*60) + (7*60*60)

day = 24*60*60
sin = pd.Series(dtype=float)
cos = pd.Series(dtype=float)
# Convert times in seconds to sin for LSTM parameter
sin = np.sin(timestamp_s * (2 * np.pi / day))
df.insert(0, 'Sin', sin)
# Convert times in seconds to cos for LSTM parameter
cos = np.cos(timestamp_s * (2 * np.pi / day))
df.insert(1, 'Cos', cos)
plt.plot(np.array(df['Sin']))
plt.plot(np.array(df['Cos']))
plt.xlabel('Time')
plt.title('Title')

plt.savefig('')
df.to_csv(path_or_buf=w_file, index=None)
