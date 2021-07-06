import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
from time import strftime

# Load CSV file from Datasets folder
df = pd.read_csv('filepath', usecols=['Time', 'S4_Temperature'])

# Preparing data
data = [go.Scatter(x=df['Time'], y=df['S4_Temperature'], mode='lines', name='name')]

# Preparing layout
layout = go.Layout(title='Title', xaxis_title="Time",
                   yaxis_title="Temperature")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='linechart.html')
