# Weather Files Breakdown

The purpose of this research project is to perform accelerated experiments in
various simulated environments on our scaled home. Our ultimate goal is to develop
a smart-home program that predicts and regulates temperature in an energy-efficient
and cost-effective manner. With this in mind, it is essential to be able to simulate
a variety of real environments in our SmartHome home and enclosure in order to
make our data useful for nationwide, or worldwide, application.  Therefore, we
chose 5 cities during a particular month that represents the diverse climate of
the United States (only taking into account temperature and humidity):

* Charlotte, NC - Moderate, Moderate - April - April 28, 2020
* Denver, CO - Cool, Dry - April - April 18, 2020
* Detroit, MI - Cool, Humid - March - March 3, 2020
* Jacksonville, FL - Hot, Humid - July - July 26, 2020
* Las Vegas, NV - Hot, Dry - June - June 19, 2020

We selected months we felt represented the city and temperature/humidity type sought 
after. The specific day was chosen by finding the average max temperature, average 
temperature, low temperature, max humidity, average humidity, and min humidity of 
the chosen month. Then, the average difference of each of the six aforementioned
factors was calculated for each day in the chosen month. The day with the lowest
total average difference (i.e. most representable day for the month) was the day 
we chose to model. All weather data is sourced from https://www.wunderground.com.

The [Daily](https://github.com/nia-00/UCF_REU_SmartHome_2021/tree/main/Data/Weather/Original_Files)
folder contains hourly temperature and humidity data of the cities for the day we
selected(see lines 8-12). It also contains a folder of this data represented in
multi-line graphs. 

The [Monthly/CSV](https://github.com/nia-00/UCF_REU_SmartHome_2021/tree/main/Data/Weather/Monthly/CSV)
folder contains daily weather data of the cities for the month we selected (see lines 8-12).

The [Original_Files](https://github.com/nia-00/UCF_REU_SmartHome_2021/tree/main/Data/Weather/Original_Files)
folder contains weather data for our chosen cities on our chosen days. This includes Max
Temp, Avg Temp, Min Temp, Humidity (%), Max Humidity(%), and Avg Humidity (%) Min.
It also includes monthly averages for the above listed categories. The "Average Difference"
section of these spreadsheets calculates the difference between each day's
weather information and the monthly average weather data. The day with the lowest
difference is the particular day we use to model our simulations after.
Further down, the hourly weather data for the chosen date is listed.

The [Weather Scaled Charts](https://github.com/nia-00/UCF_REU_SmartHome_2021/blob/main/Data/Weather/Weather_Target_To_Scaled_Charts.pdf)
file shows the temperature and humidity benchmarks for each location we chose and
their scaled equivalent. Each day starts at 7:00 AM and we allotted 1 hour and 30
minutes of real time for the morning phase of each simulation. The middle phase
of the simulation takes 9 hours and 30 minutes of real time and runs from 8:30 AM
to 6:00 PM. The afternoon phase of the simulation takes 4 hours of real time and
runs from 6:00 PM to 10:00 PM. For each location we selected the temperatures and
humidities at these key times, as well as at the hottest part of the day. To scale
the temperature and humidity we used the following equation:

<a href="https://www.codecogs.com/eqnedit.php?latex=SH_{Temp}&space;=&space;\frac{target_{City}&space;-&space;min_{City}}{max_{City}&space;-&space;min_{City}}&space;\times&space;(max_{SmartHome}&space;-&space;min_{SmartHome})&space;&plus;&space;min_{SmartHome}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?SH_{Temp}&space;=&space;\frac{target_{City}&space;-&space;min_{City}}{max_{City}&space;-&space;min_{City}}&space;\times&space;(max_{SmartHome}&space;-&space;min_{SmartHome})&space;&plus;&space;min_{SmartHome}" title="SH_{Temp} = \frac{target_{City} - min_{City}}{max_{City} - min_{City}} \times (max_{SmartHome} - min_{SmartHome}) + min_{SmartHome}" /></a>

as well as the minimum and maximum temperatures recorded inside the greenhouse
environment (69.8° F and 79.8° F respectively).
