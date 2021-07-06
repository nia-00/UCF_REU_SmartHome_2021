import csv
from datetime import datetime


# This function combines the motor states output file with the sensor data output file.
def combine_outputs(file1, file2, new_filename):
    with open(file1, "r") as motor, open(file2, "r") as sensor, open(new_filename, "w", newline='') as of:
        # Make the input readers and the output writer
        motor_reader = csv.reader(motor)
        sensor_reader = csv.reader(sensor)
        out_writer = csv.writer(of, delimiter=',')

        # Turn the inputs into a list for easy traversal
        motor_data = list(motor_reader)
        sensor_data = list(sensor_reader)

        sensor_data[0][0] = "Sensor " + sensor_data[0][0]
        motor_data[0][0] = "Motor " + motor_data[0][0]

        # These reorder the column headers of the output file so the timestamps
        # of the sensors and motors are at the start of the file
        header = [sensor_data[0][0]]
        header.extend([motor_data[0][0]])
        header.extend(sensor_data[0][1:])
        header.extend(motor_data[0][1:])
        out_writer.writerow(header)

        # Keeps track of row indices for each list
        line_m = 1
        line_s = 1

        # Keeps track of current times for each list
        current_motor = datetime.strptime(motor_data[line_m][0], '%H:%M:%S')
        current_sensor = datetime.strptime(sensor_data[line_s][0], '%H:%M:%S')

        # Store the lengths here to save time when accessing in the loop
        motor_len = len(motor_data) - 1
        sensor_len = len(sensor_data) - 1

        length = motor_len + sensor_len

        # This loop goes through each row of both lists, going back and forth between the two
        for i in range(length):
            # Write the current lines for the actuators and sensors
            out_line = [sensor_data[line_s][0]]
            out_line.extend([motor_data[line_m][0]])
            out_line.extend(sensor_data[line_s][1:])
            out_line.extend(motor_data[line_m][1:])
            out_writer.writerow(out_line)

            # if we are at the end of both csv files
            if line_s == sensor_len and line_m == motor_len:
                break
            # if motor time is bigger than sensor time, update sensor
            elif current_motor > current_sensor:
                if line_s < sensor_len:
                    line_s += 1
                    current_sensor = datetime.strptime(sensor_data[line_s][0], '%H:%M:%S')
                else:
                    line_m += 1
            # if sensor time is bigger than motor time, update motor
            elif current_motor < current_sensor:
                if line_m < motor_len:
                    line_m += 1
                    current_motor = datetime.strptime(motor_data[line_m][0], '%H:%M:%S')
                else:
                    line_s += 1
            # if both times are equal, update both
            else:
                i += 1
                line_s += 1
                line_m += 1
                current_sensor = datetime.strptime(sensor_data[line_s][0], '%H:%M:%S')
                current_motor = datetime.strptime(motor_data[line_m][0], '%H:%M:%S')

    print("Successfully combined!")


original_read_file = input("Enter original sensors data file path: ")

sensor_data = original_read_file.replace('\\', '/')
sensor_data = sensor_data.replace('"', '')
sensor_data = sensor_data.replace("original", "cleaned")

motor_states = sensor_data.replace("cleaned_", "")
motor_states = motor_states.replace("sensors", "states")

filename = sensor_data.rsplit('/', 1)
filename = filename[1].replace("cleaned_", "")
filename = filename.replace("sensors", "combined")

print("sensor: ", sensor_data)
print("motor: ", motor_states)
print("new filename: ", filename)

combine_outputs(motor_states, sensor_data, filename)
