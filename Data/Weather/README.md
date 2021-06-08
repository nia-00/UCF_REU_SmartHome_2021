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

The [Original_Files](https://github.com/nia-00/UCF_REU_SmartHome_2021/tree/main/Data/Weather/Original_Files)
folder contains weather data for our chosen cities on our chosen days. This includes Max
Temp, Avg Temp, Min Temp, Humidity (%), Max Humidity(%), and Avg Humidity (%) Min.
It also includes monthly averages for the above listed categories. The "Difference"
section of these spreadsheets calculates the difference between each day's
weather information and the monthly average weather data. The day with the lowest
difference is the particular day we use to model our simulations after.
Further down, the hourly weather data for the chosen date is listed.

The [Monthly/CSV](https://github.com/nia-00/UCF_REU_SmartHome_2021/tree/main/Data/Weather/Monthly/CSV)
folder contains daily weather data of the cities for the month we selected (see lines 8-12).

The [Daily](https://github.com/nia-00/UCF_REU_SmartHome_2021/tree/main/Data/Weather/Original_Files)
folder contains hourly temperature and humidity data of the cities for the day we
selected(see lines 8-12). It also contains a folder of this data represented in
multi-line graphs.
