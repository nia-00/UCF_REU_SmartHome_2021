import datetime
import pandas as pd

original_file = input("Enter combined, interpolated file to find lower times: ")
r_file = original_file.replace('\\', '/')
r_file = r_file.replace('"', '')

w_file = r_file.replace("combined_interpolated", "complete_time")
print("Read file: ", r_file)
print("Write file: ", w_file)

file_read = pd.read_csv(r_file)

sensor_time = file_read['Sensor Time']
motor_time = file_read['Motor Time']

headers = ['S4_Humidity', 'S4_Temperature', 'S6_Humidity', 'S6_Temperature',
           'S12_Humidity', 'S12_Temperature', 'S18_Humidity', 'S18_Temperature',
           'S19_Humidity', 'S19_Temperature', 'S24_Humidity', 'S24_Temperature',
           'S25_Humidity', 'S25_Temperature', 'S26_Humidity', 'S26_Temperature',
           "lamp", "heater", "fan", "ac",
           "Bedroom 2 to Bathroom", "Bedroom 1 to Living Room", "Living Room to Kitchen",
           "Living Room to Bathroom", "Bedroom 1 to Bathroom", "Living Room to Outside",
           "Bedroom 1 to Outside", "Bedroom 1 Left Window", "Living Room Left Window",
           "Bedroom 2 Right Window", "Kitchen Right Window", "Bedroom 2 Back Window",
           "Living Room Front Window", "Kitchen Front Window", "Bedroom 1 Back Window"]

remaining_file = file_read[headers]

# Turn the inputs into a list for easy traversal
sensor_time = list(sensor_time)
motor_time = list(motor_time)
earlier_time = []

for time in sensor_time:
    time = datetime.datetime.strptime(time, '%H:%M:%S')

for time in motor_time:
    time = datetime.datetime.strptime(time, '%H:%M:%S')

for x in range(len(sensor_time)):
    print("We are now comparing sensor time ", sensor_time[x],
          "and motor time ", motor_time[x])
    if sensor_time[x] < motor_time[x]:
        print("Sensor time was lower at ", sensor_time[x], "index: ", x)
        earlier_time.append(sensor_time[x])
    elif motor_time[x] < sensor_time[x]:
        print("Motor time was lower at ", motor_time[x], "index: ", x)
        earlier_time.append(motor_time[x])
    else:
        print("The times were the same, so motor time was appended: ", motor_time[x], "at index ", x)
        earlier_time.append(motor_time[x])

print(earlier_time)
print(type(earlier_time))

times_df = pd.DataFrame(earlier_time, columns=['Time'])
final_df = pd.concat([times_df, remaining_file], axis=1, ignore_index=True)
final_df.to_csv(path_or_buf=w_file, mode='a', index=None)


