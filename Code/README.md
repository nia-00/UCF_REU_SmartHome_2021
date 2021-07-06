# Code Overview

This folder contains the code we have written for this project organized into
subfolders based on type.

The [Data Analysis](https://github.com/nia-00/UCF_REU_SmartHome_2021/tree/main/Code/Data%20Analysis)
folder contains the code we use to prepare the house's output files for analysis.
In addition, this folder contains the code for various machine learning algorithms
we used to analyze our data.

Procedure for Formatting Data:
1. Raw temperature and humidity data collected from simulations saved in [Seperate_Readings](https://github.com/nia-00/UCF_REU_SmartHome_2021/tree/main/Data/Simulation_Data/Seperate_Readings) are cleaned and also saved in [Seperate_Readings](https://github.com/nia-00/UCF_REU_SmartHome_2021/tree/main/Data/Simulation_Data/Seperate_Readings) using [remove_data_spikes.py](https://github.com/nia-00/UCF_REU_SmartHome_2021/blob/main/Code/Data%20Analysis/remove_data_spikes.py).
2. Cleaned temperature/humidity and motor state data files saved in [Seperate_Readings](https://github.com/nia-00/UCF_REU_SmartHome_2021/tree/main/Data/Simulation_Data/Seperate_Readings) are combined into a single file saved in [Combined](https://github.com/nia-00/UCF_REU_SmartHome_2021/tree/main/Data/Simulation_Data/Combined) using [output_file_combination.py](https://github.com/nia-00/UCF_REU_SmartHome_2021/blob/main/Code/Data%20Analysis/output_file_combination.py)

The [House Code](https://github.com/nia-00/UCF_REU_SmartHome_2021/tree/main/Code/House%20Code)
folder contains the code we use to control the house and collect data from it.
This folder also contains the code to establish a client server connection between
our two Raspberry Pis.

The [Trimmed Code](https://github.com/nia-00/UCF_REU_SmartHome_2021/tree/main/Code/Trimmed%20Code)
folder contains the original code for establishing a client server connection that
we modeled our code after.
