import csv
import pandas as pd
import numpy as np
from numpy import genfromtxt


def clean_file(r_file, w_file, low_temp, low_hum, denom_temp, denom_hum, times, sensors, motors):
    # Turns data into 2D numpy array
    data = genfromtxt(r_file, delimiter=',')

    all_data = []
    removed_indices = []

    # Calculate number of rows and columns for reshaping (number of sensors used in data)
    results = pd.read_csv(r_file)
    column_headers = results.head(0)
    print(column_headers)
    num_of_rows = len(results)
    num_of_cols = data[0].size - 2

    # Remove all NaN (headings and times), turns data into 1D array
    data = data[~np.isnan(data)]
    # Restore to 2D numpy array, now columns = category (temp, humidity)
    data = np.reshape(data, (num_of_rows, num_of_cols))

    sensors_data_only = []

    for s, array in enumerate(data):
        sensors_data_only.append(array[0:16])

    print("SENSORS BEFORE: ", sensors_data_only)

    for col_num, column in enumerate(sensors_data_only):
        if col_num % 2 == 0:
            for row_num, val in enumerate(column):
                column[row_num] = ((((column[row_num] - 70) / 10) * denom_temp) + low_temp).__round__(1)
        else:

            for row_num, val in enumerate(column):
                column[row_num] = ((((column[row_num] - 44.7) / 7.4) * denom_hum) + low_hum).__round__(1)


    print("SENSORS AFTER: ", sensors_data_only)


'''
    for x in range(16):
        for element in sensors_data_only[x]:

            data_list = [y[x] for y in sensors_data_only]  # Each column will take turns being data_list
        # data_list = [x for x in data_list if x > 0]  # Remove all negative numbers in array

        if x % 2 == 0:
            for z, hum in enumerate(data_list):
                print("HUM BEFORE: ", data_list[z])
                data_list[z] = ((((hum - 44.7) / 7.4) * denom_hum) + low_hum).__round__(1)
                print("HUM AFTER: ", data_list[z])
                all_data.append(data_list)

        else:
            for z, temp in enumerate(data_list):
                print("TEMP BEFORE: ", data_list[z])
                data_list[z] = ((((temp - 70) / 10) * denom_temp) + low_temp).__round__(1)
                print("TEMP AFTER: ", data_list[z])
            all_data.append(data_list)

    print("ALL DATA:", all_data)
    print(type(all_data))

    scaledData = pd.DataFrame(all_data)
    print("SCALED DATA:", scaledData)

    result = pd.concat([times, scaledData, motors], axis=1)
    #print(result)

    result.to_csv(path_or_buf="helpme4.csv")
'''

if __name__ == "__main__":
    min_temp = 44
    denominator_temp = 31
    min_hum = 36
    denominator_hum = 34

    original_file = input("Enter file path to rescale: ")
    read_file = original_file.replace('\\', '/')
    read_file = read_file.replace('"', '')

    write_file = read_file.replace("combined_interpolated", "3complete")

    print("Read file: ", original_file)
    print("Write file: ", write_file.replace("/", "\\"))

    df0 = pd.read_csv(read_file, usecols=['Sensor Time', 'Motor Time'])

    df1 = pd.read_csv(read_file, usecols=['S4_Humidity', 'S4_Temperature', 'S6_Humidity', 'S6_Temperature',
                                          'S12_Humidity', 'S12_Temperature', 'S18_Humidity', 'S18_Temperature',
                                          'S19_Humidity', 'S19_Temperature', 'S24_Humidity', 'S24_Temperature',
                                          'S25_Humidity', 'S25_Temperature', 'S26_Humidity', 'S26_Temperature'])

    df2 = pd.read_csv(read_file, usecols=["lamp", "heater", "fan", "ac",
                                          "Bedroom 2 to Bathroom", "Bedroom 1 to Living Room", "Living Room to Kitchen",
                                          "Living Room to Bathroom", "Bedroom 1 to Bathroom", "Living Room to Outside",
                                          "Bedroom 1 to Outside", "Bedroom 1 Left Window", "Living Room Left Window",
                                          "Bedroom 2 Right Window", "Kitchen Right Window", "Bedroom 2 Back Window",
                                          "Living Room Front Window", "Kitchen Front Window", "Bedroom 1 Back Window"])

    with open(read_file, 'r') as master, open(write_file, 'w') as matched:
        matched.write(next(master))

    clean_file(read_file, write_file, min_temp, min_hum, denominator_temp, denominator_hum, df0, df1, df2)
