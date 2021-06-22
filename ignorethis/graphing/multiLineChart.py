import csv

import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
from time import strftime


def figures_to_html(figs, filename):
    dashboard = open(filename, 'w')
    dashboard.write("<html><head></head><body>" + "\n")
    for fig in figs:
        inner_html = fig.to_html().split('<body>')[1].split('</body>')[0]
        dashboard.write(inner_html)
    dashboard.write("</body></html>" + "\n")


# Load CSV file from Datasets folder
df_path = input("Enter file path: ")
df_path = df_path.replace('\\', '/')
df_path = df_path.replace('"', '')

w_file = df_path.rsplit('/', 1)
w_file = w_file[1].replace("cleaned_", "")
w_file = w_file.replace("sensors", "graphed")
w_file = w_file.replace("csv", "html")

print(w_file)

print("df: ", df_path)

df = pd.read_csv(df_path)
# df['Date'] = pd.to_datetime(df['Date'])

# Preparing data
multiline_df = df

x_axis = 'Sensor Time'

# All temperature data throughout simulation
trace1_multiline_temp = go.Scatter(x=multiline_df[x_axis], y=multiline_df['S4_Temperature'], mode='lines',
                                   name='S4_Temp')
trace2_multiline_temp = go.Scatter(x=multiline_df[x_axis], y=multiline_df['S6_Temperature'], mode='lines',
                                   name='S6_Temp')
trace3_multiline_temp = go.Scatter(x=multiline_df[x_axis], y=multiline_df['S12_Temperature'], mode='lines',
                                   name='S12_Temp')
trace4_multiline_temp = go.Scatter(x=multiline_df[x_axis], y=multiline_df['S18_Temperature'], mode='lines',
                                   name='S18_Temp')
trace5_multiline_temp = go.Scatter(x=multiline_df[x_axis], y=multiline_df['S19_Temperature'], mode='lines',
                                   name='S19_Temp')
trace6_multiline_temp = go.Scatter(x=multiline_df[x_axis], y=multiline_df['S24_Temperature'], mode='lines',
                                   name='S24_Temp')
trace7_multiline_temp = go.Scatter(x=multiline_df[x_axis], y=multiline_df['S25_Temperature'], mode='lines',
                                   name='S25_Temp')
trace8_multiline_temp = go.Scatter(x=multiline_df[x_axis], y=multiline_df['S26_Temperature'], mode='lines',
                                   name='S26_Temp')

data_multiline_temps = [trace1_multiline_temp, trace2_multiline_temp, trace3_multiline_temp, trace4_multiline_temp,
                        trace5_multiline_temp, trace6_multiline_temp, trace7_multiline_temp, trace8_multiline_temp]

# All humidity data throughout simulation
trace1_multiline_hum = go.Scatter(x=multiline_df[x_axis], y=multiline_df['S4_Humidity'], mode='lines', name='S4_Hum')
trace2_multiline_hum = go.Scatter(x=multiline_df[x_axis], y=multiline_df['S6_Humidity'], mode='lines', name='S6_Hum')
trace3_multiline_hum = go.Scatter(x=multiline_df[x_axis], y=multiline_df['S12_Humidity'], mode='lines', name='S12_Hum')
trace4_multiline_hum = go.Scatter(x=multiline_df[x_axis], y=multiline_df['S18_Humidity'], mode='lines', name='S18_Hum')
trace5_multiline_hum = go.Scatter(x=multiline_df[x_axis], y=multiline_df['S19_Humidity'], mode='lines', name='S19_Hum')
trace6_multiline_hum = go.Scatter(x=multiline_df[x_axis], y=multiline_df['S24_Humidity'], mode='lines', name='S24_Hum')
trace7_multiline_hum = go.Scatter(x=multiline_df[x_axis], y=multiline_df['S25_Humidity'], mode='lines', name='S25_Hum')
trace8_multiline_hum = go.Scatter(x=multiline_df[x_axis], y=multiline_df['S26_Humidity'], mode='lines', name='S26_Hum')

data_multiline_hums = [trace1_multiline_hum, trace2_multiline_hum, trace3_multiline_hum, trace4_multiline_hum,
                       trace5_multiline_hum, trace6_multiline_hum, trace7_multiline_hum, trace8_multiline_hum]

# Preparing layout
layout = go.Layout(title='TEMPERATURE', xaxis_title="Time",
                   yaxis_title="Temperature (Fahrenheit)")

layout2 = go.Layout(title='HUMIDITY', xaxis_title="Time",
                    yaxis_title="Humidity (%)")

# Plot the figure and saving in a html file
fig = go.Figure(data=data_multiline_temps, layout=layout)
fig2 = go.Figure(data=data_multiline_hums, layout=layout2)

# pyo.plot(fig, filename='multiLineChart.html')

figures_to_html([fig, fig2], w_file)
