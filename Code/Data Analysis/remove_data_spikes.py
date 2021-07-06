import csv
import pandas as pd
import numpy as np
from numpy import genfromtxt


def clean_file(r_file, w_file, recorded_times):
    # Turns data into 2D numpy array
    data = genfromtxt(r_file, delimiter=',')

    all_data = []
    removed_indices = []

    # Calculate number of rows and columns for reshaping (number of sensors used in data)
    results = pd.read_csv(r_file)
    column_headers = results.head(0)
    print(column_headers)
    num_of_rows = len(results)
    num_of_cols = data[0].size - 1

    # Remove all NaN (headings and times), turns data into 1D array
    data = data[~np.isnan(data)]
    # Restore to 2D numpy array, now columns = category (temp, humidity)
    data = np.reshape(data, (num_of_rows, num_of_cols))

    for x in range(num_of_cols):
        for element in data[x]:
            data_list = [y[x] for y in data]  # Each column will take turns being data_list
        # data_list = [x for x in data_list if x > 0]  # Remove all negative numbers in array
        print('CURRENT ARRAY: ', data_list)

        for z, value in enumerate(data_list):
            if z == len(data_list) - 1:  # Prevents indexing error
                break
            # if data_list[z] < 0:
            #    data_list[z] = 0
            #    z+=1
            # Remove any value whose predecessor has a difference of 10 or more
            # Outlier formula does not cover data spikes
            if abs((data_list[z + 1] - data_list[z])) > 10:
                print('REMOVING ELEMENT ', data_list[z + 1], 'AT INDEX ', z)
                # data_list[z + 1] = 0  # Remove unusual value
                removed_indices.append(z + 1)
                data_list[z + 1] = data_list[z]

        for a, values in enumerate(data_list):
            if a in removed_indices:
                data_list[a] = None

        all_data.append(data_list)  # Append cleaned columns
        removed_indices = []

    all_data = all_data[:0] + [recorded_times] + all_data[0:]  # Ensures that recorded times is only printed once
    print(type(all_data))
    print('all DATA: ', all_data)

    all_data = zip(*all_data)
    print(type(all_data))

    with open(w_file, "a", newline='') as f:
        writer = csv.writer(f)
        for row in all_data:
            writer.writerow(row)


if __name__ == "__main__":

    original_file = input("Enter file path to clean: ")
    read_file = original_file.replace('\\', '/')
    read_file = read_file.replace('"', '')

    file_keyword = "original"
    write_file = read_file.rsplit('/', 1)

    if file_keyword in read_file:
        write_file = read_file.replace("original", "cleaned")
        end_name_index = write_file.find('.csv')
    else:
        print("File path not entered with conventional naming for this project.")

    print("Original file name: ", original_file)
    print("Cleaned file name: ", write_file.replace("/", "\\"))

    df = pd.read_csv(read_file)
    times = df.Time.to_list()

    with open(read_file, 'r') as master, open(write_file, 'w') as matched:
        matched.write(next(master))

    clean_file(read_file, write_file, times)
