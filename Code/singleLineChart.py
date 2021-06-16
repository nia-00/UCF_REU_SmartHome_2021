import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
from time import strftime

# Load CSV file from Datasets folder
df = pd.read_csv('/home/pi/Desktop/UCF-REU-SmartHome/aaaaaa8.csv', usecols=['Time on 05 Jun 2021', 'S4_Temperature'])
#df['Date'] = pd.to_datetime(df['Date'])

# Preparing data
data = [go.Scatter(x=df['Time on 05 Jun 2021'], y=df['S4_Temperature'], mode='lines', name='Death')]

# Preparing layout
layout = go.Layout(title='Stabilization Point - Lamp - High Point (05 Jun 2021)', xaxis_title="Time",
                   yaxis_title="Temperature")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='linechart.html')
