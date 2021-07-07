import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

   
def convert_to_time_cycle(file_path):
    df = pd.read_csv(file_path)
    times_in_seconds = pd.Series(pd.to_timedelta(df[df.columns[0]]))     # Convert time to seconds
    times_in_seconds = times_in_seconds.dt.total_seconds()
    times_in_seconds = times_in_seconds - min(times_in_seconds)          # Start time at 0 seconds
    times_in_seconds = times_in_seconds / max(times_in_seconds)          # Scale all times between 0 and 1
    times_in_seconds = times_in_seconds * 15 * 60 * 60 + 7 * 60 * 60     # Our simulations represent a 15-hour period which start at 7am

    day = 24 * 60 * 60
    second_to_hour = 60 * 60
    x_tick_list = []
    x_tick_locater = []
    for i in range(int(min(times_in_seconds / second_to_hour)), int(max(times_in_seconds / second_to_hour))+1):
        if i<12:
            x_tick_list.append(f'{i} a.m.')
        elif i==12:
            x_tick_list.append(f'{i} p.m.')
        else:
            x_tick_list.append(f'{i-12} p.m.')
        x_tick_locater.append(i)
    x_fornatter = FixedFormatter(x_tick_list)
    x_locator = FixedLocator(x_tick_locater)
    df['Days sin'] = np.sin(times_in_seconds * (2 * np.pi / day))    # Convert times in seconds to sin for LSTM parameter
    df['Days cos'] = np.cos(times_in_seconds * (2 * np.pi / day))    # Convert times in seconds to cos for LSTM parameter
    fig = plt.figure()
    ax = fig.gca()
    ax.plot(times_in_seconds / second_to_hour, df['Days sin'])
    ax.plot(times_in_seconds / second_to_hour, df['Days cos'])
    ax.xaxis.set_major_formatter(x_fornatter)
    ax.xaxis.set_major_locator(x_locator)
    ax.tick_params(axis='x', labelrotation=-60)
    ax.set_xlabel('Time Being Modeled')
    ax.set_ylabel('Converted Time')
    ax.set_title('Cyclic Time Representation')
    fig.savefig('time.png', bbox_inches='tight')
    print(times_in_seconds.head)

r_file = input("Input read file: ")
r_file = r_file.replace('\\', '/')
r_file = r_file.replace('"', '')

# The following maintains our naming convention for this project; change as needed
w_file = r_file.replace("RESCALED", "sin_cos")
print("Read file: ", r_file)
print("Write file: ", w_file)

convert_to_time_cycle(r_file)
