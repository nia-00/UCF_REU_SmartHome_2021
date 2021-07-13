Procedure for Formatting Data saved in Simulation_Data:

Raw temperature and humidity data collected from simulations saved in Seperate_Readings are cleaned and also saved in Seperate_Readings using remove_data_spikes.py.
Cleaned temperature/humidity and motor state data files saved in Seperate_Readings are combined into a single file saved in Combined using output_file_combination.py
Missing data points removed using remove_data_spikes.py are interpolated and saved in Interpolated_Combined using interpolate_data.py.
The earlier time between the sensor reading times and motor times are determined and data is saved in Interpolated_Combined_LowestTime using find_earlier_time.py.
Times from Interpolated_Combined_LowestTime are converted and graphed to a sinusoidal variable and saved in Complete_Sun_Cos using convert_to_time_cycle.py.
