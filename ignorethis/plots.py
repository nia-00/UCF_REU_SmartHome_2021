import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import plotly.offline as pyo
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go

temp_cols = ["Sensor Time", "S4_Temperature", "S6_Temperature",
             "S12_Temperature", "S18_Temperature", "S19_Temperature",
             "S24_Temperature", "S25_Temperature", "S26_Temperature"]

hum_cols = ["Sensor Time", "S4_Humidity", "S6_Humidity",
            "S12_Humidity", "S18_Humidity", "S19_Humidity",
            "S24_Humidity", "S25_Humidity", "S26_Humidity"]

motor_cols = ["Motor Time", "lamp", "heater", "fan", "ac",
              "Bedroom 2 to Bathroom", "Bedroom 1 to Living Room", "Living Room to Kitchen",
              "Living Room to Bathroom", "Bedroom 1 to Bathroom", "Living Room to Outside",
              "Bedroom 1 to Outside", "Bedroom 1 Left Window", "Living Room Left Window",
              "Bedroom 2 Right Window", "Kitchen Right Window", "Bedroom 2 Back Window",
              "Living Room Front Window", "Kitchen Front Window", "Bedroom 1 Back Window"]

data_multiline = []  # global variable


def graphHumidity(df, col_headers):
    multiline_df = df
    global data_multiline

    for x in range(1):
        multiline = go.Scatter(x=multiline_df[col_headers[0]], y=multiline_df[col_headers[x]], mode='lines',
                               name=col_headers[x])
        data_multiline.append(multiline)
        graphLayout()

def graphTemperature(df, col_headers):
    multiline_df = df
    global data_multiline

    for x in range(len(col_headers)):
        multiline = go.Scatter(x=multiline_df[col_headers[0]], y=multiline_df[col_headers[x]], mode='lines',
                               name=col_headers[x])
        data_multiline.append(multiline)


# def visualizeMotorStates(df):


# ---------- BEGINNING OF PROGRAM ----------

# ---------- Charlotte ----------

charlotte_urls = [
    "https://raw.githubusercontent.com/nia-00/UCF_REU_SmartHome_2021/main/Data/Simulation_Data/Combined/Charlotte/charlotte_sim_1_cooltoofast_combined.csv",
    "https://raw.githubusercontent.com/nia-00/UCF_REU_SmartHome_2021/main/Data/Simulation_Data/Combined/Charlotte/charlotte_sim_1_lowpeaktemp_combined.csv",
    "https://raw.githubusercontent.com/nia-00/UCF_REU_SmartHome_2021/main/Data/Simulation_Data/Combined/Charlotte/charlotte_sim_1_successful_combined.csv",
    "https://raw.githubusercontent.com/nia-00/UCF_REU_SmartHome_2021/main/Data/Simulation_Data/Combined/Charlotte/charlotte_sim_2_combined.csv",
    "https://raw.githubusercontent.com/nia-00/UCF_REU_SmartHome_2021/main/Data/Simulation_Data/Combined/Charlotte/charlotte_sim_2_v2_combined.csv",
    "https://raw.githubusercontent.com/nia-00/UCF_REU_SmartHome_2021/main/Data/Simulation_Data/Combined/Charlotte/charlotte_sim_3_combined.csv"]

# url = 'https://raw.githubusercontent.com/nia-00/UCF_REU_SmartHome_2021/main/Data/Simulation_Data/Combined/Charlotte/charlotte_sim_1_cooltoofast_combined.csv'

app = dash.Dash()

def graphLayout():
    # Layout
    app.layout = html.Div(children=[
        html.H1(children='Python Dash',
                style={
                    'textAlign': 'center',
                    'color': '#ef3e18'
                }
                ),
        html.Div('Web dashboard for Data Visualization using Python', style={'textAlign': 'center'}),
        html.Div('ScaledHome Simulation Data - UCF REU IoT', style={'textAlign': 'center'}),
        html.Br(),
        html.Br(),
        html.Hr(style={'color': '#7FDBFF'}),
        html.H3('Multi Line chart', style={'color': '#df1e56'}),
        html.Div(
            'This line chart represent...'),
        dcc.Graph(id='graph5',
                  figure={
                      'data': data_multiline,
                      'layout': go.Layout(
                          title='Title',
                          xaxis={'title': 'Date'}, yaxis={'title': 'Number of cases'})
                  }
                  )

    ])

for url in charlotte_urls:
    df_hum = pd.read_csv(url, usecols=hum_cols)
    df_temp = pd.read_csv(url, usecols=temp_cols)
    #print('URL: ', url)
    df_motor = pd.read_csv(url, usecols=motor_cols)
    for col in temp_cols:
        graphTemperature(df_temp, temp_cols)
        # visualizeMotorStates(df_motor, motor_cols)
        #graphHumidity(df_hum, hum_cols)
        # visualizeMotorStates(df_motor, motor_cols)



if __name__ == '__main__':
    app.run_server()
