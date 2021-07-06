import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
from time import strftime

# Load CSV file from Datasets folder
df = pd.read_csv('/home/pi/Desktop/UCF-REU-SmartHome/aaaaaa8.csv', usecols=['Time on 05 Jun 2021', 'S4_Temperature', 'S4_Humidity'])
#df['Date'] = pd.to_datetime(df['Date'])

# Preparing data
multiline_df = df

trace1_multiline = go.Scatter(x=multiline_df['Time'], y=multiline_df['S4_Temperature'], mode='lines', name='Temperature')
trace2_multiline = go.Scatter(x=multiline_df['Time'], y=multiline_df['S4_Humidity'], mode='lines', name='Humidity')
data_multiline = [trace1_multiline, trace2_multiline]


# Preparing layout
layout = go.Layout(title='Title)', xaxis_title="Time",
                   yaxis_title="Temperature")

# Plot the figure and saving in a html file
fig = go.Figure(data=data_multiline, layout=layout)
pyo.plot(fig, filename='multiLineChart.html')


