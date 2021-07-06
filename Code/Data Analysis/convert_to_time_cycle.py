import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def convert_to_time_cycle(read_file_path):
    df = pd.read_csv(read_file_path, sep=',')

    times_in_seconds = pd.Series(pd.to_timedelta(df[df.columns[0]]))
    # Convert time to seconds
    times_in_seconds = times_in_seconds.dt.total_seconds()
    # Start time at 0 seconds
    times_in_seconds = times_in_seconds-min(times_in_seconds)
    # Scale all times between 0 and 1
    times_in_seconds = times_in_seconds / max(times_in_seconds)
    # Our simulations represent a 15-hour period which start at 7am
    times_in_seconds = times_in_seconds * 15 * 60 * 60 + 7*60*60
    day = 24*60*60
    second_to_hour = 60*60

    # Convert times in seconds to sin for LSTM parameter
    df['Days sin'] = np.sin(times_in_seconds * (2*np.pi / day))
    # Convert times in seconds to cos for LSTM parameter
    df['Days cos'] = np.cos(times_in_seconds * (2*np.pi / day))

    # Plotting
    plt.plot(times_in_seconds/second_to_hour, df['Days sin'])
    plt.plot(times_in_seconds/second_to_hour, df['Days cos'])
    plt.xlabel('Hours')
    plt.show()
    print(times_in_seconds.head)


r_file = input("Input read file: ")
r_file = r_file.replace('\\', '/')
r_file = r_file.replace('"', '')

# The following maintains our naming convention for this project; change as needed
w_file = r_file.replace("RESCALED", "sin_cos")
print("Read file: ", r_file)
print("Write file: ", w_file)

convert_to_time_cycle(r_file)
