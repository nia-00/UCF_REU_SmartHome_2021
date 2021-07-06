# Data Overview

The folders above contain different kinds of data we used for this project.

The [Machine Learning](https://github.com/nia-00/UCF_REU_SmartHome_2021/tree/main/Data/Machine_Learning)
folder contains the results of our machine learning algorithms represented as
graphs. We fed each algorithm two datasets, one with time as an input and one without.
For each run we graphed all the sensor predictions vs actual values for temperature
and humidity. There is a graph for each room in the house as well as one for the
entire house.

The [Simulation_Data](https://github.com/nia-00/UCF_REU_SmartHome_2021/tree/main/Data/Simulation_Data)
folder contains all the data we have collected from the house when
running simulations. There is a subfolder for the separate sensor and actuator readings
and a subfolder for the cleaned combined data files we will use for our machine
learning algorithms. The sensor and motor output files are combined using their
timestamps. The sensor readings and motor states that happen in the same time range
are combined into one line, so there are some times that are repeated for both
sensor readings and motor readings. This is because these data points are collected
at different time intervals. There may be multiple sensor readings for one state
of the house and multiple states for one sensor reading. There is another subfolder
that contains the clean combined data with the time as a sinusoidal variable.

Procedure for Formatting Data saved in [Simulation_Data](https://github.com/nia-00/UCF_REU_SmartHome_2021/tree/main/Data/Simulation_Data):
1. Raw temperature and humidity data collected from simulations saved in [Seperate_Readings](https://github.com/nia-00/UCF_REU_SmartHome_2021/tree/main/Data/Simulation_Data/Seperate_Readings) are cleaned and also saved in [Seperate_Readings](https://github.com/nia-00/UCF_REU_SmartHome_2021/tree/main/Data/Simulation_Data/Seperate_Readings) using [remove_data_spikes.py](https://github.com/nia-00/UCF_REU_SmartHome_2021/blob/main/Code/Data%20Analysis/remove_data_spikes.py).
2. Cleaned temperature/humidity and motor state data files saved in [Seperate_Readings](https://github.com/nia-00/UCF_REU_SmartHome_2021/tree/main/Data/Simulation_Data/Seperate_Readings) are combined into a single file saved in [Combined](https://github.com/nia-00/UCF_REU_SmartHome_2021/tree/main/Data/Simulation_Data/Combined) using [output_file_combination.py](https://github.com/nia-00/UCF_REU_SmartHome_2021/blob/main/Code/Data%20Analysis/output_file_combination.py)
3. Missing data points removed using [remove_data_spikes.py](https://github.com/nia-00/UCF_REU_SmartHome_2021/blob/main/Code/Data%20Analysis/remove_data_spikes.py) are interpolated and saved in [Interpolated_Combined](https://github.com/nia-00/UCF_REU_SmartHome_2021/tree/main/Data/Simulation_Data/Interpolated_Combined) using [interpolate_data.py](https://github.com/nia-00/UCF_REU_SmartHome_2021/blob/main/Code/Data%20Analysis/interpolate_data.py).
4. The earlier time between the sensor reading times and motor times are determined and data is saved in [Interpolated_Combined_LowestTime](https://github.com/nia-00/UCF_REU_SmartHome_2021/tree/main/Data/Simulation_Data/Interpolated_Combined_LowestTime) using [find_earlier_time.py](https://github.com/nia-00/UCF_REU_SmartHome_2021/blob/main/Code/Data%20Analysis/find_earlier_time.py).
5. Times from [Interpolated_Combined_LowestTime](https://github.com/nia-00/UCF_REU_SmartHome_2021/tree/main/Data/Simulation_Data/Interpolated_Combined_LowestTime) are converted and graphed to a sinusoidal variable and saved in [Complete_Sun_Cos](https://github.com/nia-00/UCF_REU_SmartHome_2021/tree/main/Data/Simulation_Data/Complete_Sin_Cos) using [convert_to_time_cycle.py](https://github.com/nia-00/UCF_REU_SmartHome_2021/blob/main/Code/Data%20Analysis/convert_to_time_cycle.py). 

The [Stabilization](https://github.com/nia-00/UCF_REU_SmartHome_2021/tree/main/Data/Stabilization)
folder contains all of the appliance stabilization data we collected. This
data was used to determine the limitations of what we can model in the house
in regards to temperature and humidity. In addition this data was used to determine
the timing to use to reach target scaled temperatures in the simulations. We ran
each appliance individually until it reached its maximum or minimum temperature
or humidity. We then turned off the appliance and continued to record sensor
readings until they returned to the starting temperature and humidity.


The [Weather](https://github.com/nia-00/UCF_REU_SmartHome_2021/tree/main/Data/Weather)
folder contains the real world data for each of our chosen cities. Further descriptions
of the data and how we used it can be found in this folder as well.
