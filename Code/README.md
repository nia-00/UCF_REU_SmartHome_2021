# Code Overview

This folder contains the code we have written for this project organized into
subfolders based on type.

The [Data Analysis](https://github.com/nia-00/UCF_REU_SmartHome_2021/tree/main/Code/Data%20Analysis)
folder contains the code we use to prepare the house's output files for analysis.
In addition, this folder contains the code for various machine learning algorithms
we used to analyze our data.

Procedure for Formatting Data saved in [Simulation_Data](https://github.com/nia-00/UCF_REU_SmartHome_2021/tree/main/Data/Simulation_Data):
1. Raw temperature and humidity data collected from simulations saved in [Seperate_Readings](https://github.com/nia-00/UCF_REU_SmartHome_2021/tree/main/Data/Simulation_Data/Seperate_Readings) are cleaned and also saved in [Seperate_Readings](https://github.com/nia-00/UCF_REU_SmartHome_2021/tree/main/Data/Simulation_Data/Seperate_Readings) using [remove_data_spikes.py](https://github.com/nia-00/UCF_REU_SmartHome_2021/blob/main/Code/Data%20Analysis/remove_data_spikes.py).
2. Cleaned temperature/humidity and motor state data files saved in [Seperate_Readings](https://github.com/nia-00/UCF_REU_SmartHome_2021/tree/main/Data/Simulation_Data/Seperate_Readings) are combined into a single file saved in [Combined](https://github.com/nia-00/UCF_REU_SmartHome_2021/tree/main/Data/Simulation_Data/Combined) using [output_file_combination.py](https://github.com/nia-00/UCF_REU_SmartHome_2021/blob/main/Code/Data%20Analysis/output_file_combination.py)
3. Missing data points removed using [remove_data_spikes.py](https://github.com/nia-00/UCF_REU_SmartHome_2021/blob/main/Code/Data%20Analysis/remove_data_spikes.py) are interpolated and saved in [Interpolated_Combined](https://github.com/nia-00/UCF_REU_SmartHome_2021/tree/main/Data/Simulation_Data/Interpolated_Combined) using [interpolate_data.py](https://github.com/nia-00/UCF_REU_SmartHome_2021/blob/main/Code/Data%20Analysis/interpolate_data.py).
4. The earlier time between the sensor reading times and motor times are determined and data is saved in [Interpolated_Combined_LowestTime](https://github.com/nia-00/UCF_REU_SmartHome_2021/tree/main/Data/Simulation_Data/Interpolated_Combined_LowestTime) using [find_earlier_time.py](https://github.com/nia-00/UCF_REU_SmartHome_2021/blob/main/Code/Data%20Analysis/find_earlier_time.py).
5. Times from [Interpolated_Combined_LowestTime](https://github.com/nia-00/UCF_REU_SmartHome_2021/tree/main/Data/Simulation_Data/Interpolated_Combined_LowestTime) are converted and graphed to a sinusoidal variable and saved in [Complete_Sun_Cos](https://github.com/nia-00/UCF_REU_SmartHome_2021/tree/main/Data/Simulation_Data/Complete_Sin_Cos) using [convert_to_time_cycle.py](https://github.com/nia-00/UCF_REU_SmartHome_2021/blob/main/Code/Data%20Analysis/convert_to_time_cycle.py). 

The [House Code](https://github.com/nia-00/UCF_REU_SmartHome_2021/tree/main/Code/House%20Code)
folder contains the code we use to control the house and collect data from it.
This folder also contains the code to establish a client server connection between
our two Raspberry Pis which was not used in the version presented in July 2021.

The [Trimmed Code](https://github.com/nia-00/UCF_REU_SmartHome_2021/tree/main/Code/Trimmed%20Code)
folder contains the original code for establishing a client server connection that
we modeled our code after.
