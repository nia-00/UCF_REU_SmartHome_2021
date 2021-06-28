import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.graph_objs as go
import plotly.offline as pyo

#lmap and heater
#combined_file = input("Enter file path: ")
combined_file = 'C:\\Users\\welcm\\PycharmProjects\\.smartHomeFiles\\graphing\\charlotte_sim_1_cooltoofast_combined.csv'
combined_file = combined_file.replace('\\', '/')
combined_file = combined_file.replace('"', '')

motor_times = pd.read_csv(combined_file, usecols=['Motor Time'])
csv_file = pd.read_csv(combined_file)

# x-axis, number of rows AKA number of readings
x_range = [i for i in range(len(motor_times)+1)]
print(x_range)

y_range = [i for i in range(19)]

motor_cols = ["Motor Time", "lamp", "heater", "fan", "ac",
              "Bedroom 2 to Bathroom", "Bedroom 1 to Living Room", "Living Room to Kitchen",
              "Living Room to Bathroom", "Bedroom 1 to Bathroom", "Living Room to Outside",
              "Bedroom 1 to Outside", "Bedroom 1 Left Window", "Living Room Left Window",
              "Bedroom 2 Right Window", "Kitchen Right Window", "Bedroom 2 Back Window",
              "Living Room Front Window", "Kitchen Front Window", "Bedroom 1 Back Window"]

# Preparing data
data = [go.Heatmap(x=x_range,
                   y=y_range,
                   z=csv_file['lamp'].values.tolist(),
                   colorscale='Jet')]

# Preparing layout
layout = go.Layout(title='Corona Virus Recovered Cases', xaxis_title="Day of Week",
                   yaxis_title="Week of Month")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='heatmap.html')

'''
lamp_state = pd.read_csv(combined_file, usecols=['lamp'])
heater_state = pd.read_csv(combined_file, usecols=['heater'])

motor_times = list(motor_times)


fig, ax = plt.subplots()

x_min = 0
x_max = 100

ax.set_xlim(x_min, x_max)
ax.set_xlabel('minutes since start')



ax.broken_barh([(110, 30), (150, 10)], (10, 9), facecolors='tab:blue')

ax.broken_barh([(10, 50), (100, 20), (130, 10)], (20, 9),
               facecolors=('tab:orange', 'tab:green', 'tab:red'))
ax.set_ylim(5, 35)

ax.set_yticks([15, 25])
ax.set_yticklabels(['Bill', 'Jim'])
ax.grid(True)

plt.show()
'''