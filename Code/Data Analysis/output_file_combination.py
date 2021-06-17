
# imports
import csv
import pandas as pd

# This function combines the motor states output file with the sensor data output file.
def combine_outputs(file1, file2):
    with open(file1, "r") as motor, open(file2, "r") as sensor, open("Combined_Output1.csv", "w", newline = '') as of:
            # Make the input readers and the output writer
            motorReader = csv.reader(motor)
            sensorReader = csv.reader(sensor)
            outWriter = csv.writer(of, delimiter = ',')

            # Turn the inputs into a list for easy traversal
            motorData = list(motorReader)
            sensorData = list(sensorReader)

            sensorData[0][0] = "Sensor " + sensorData[0][0]
            motorData[0][0] = "Motor " + motorData[0][0]

            # These reorder the column headers of the output file so the
            # timestamps of the sensors and motors are at the start of
            # the file
            header = [sensorData[0][0]]
            header.extend([motorData[0][0]])
            header.extend(sensorData[0][1:])
            header.extend(motorData[0][1:])
            outWriter.writerow(header)

            # Keeps track of row indices for each list
            lineM = 1
            lineS = 1

            # Keeps track of current times for each list
            currentMotor = datetime.datetime.strptime(motorData[lineM][0], '%H:%M:%S')
            currentSensor = datetime.datetime.strptime(sensorData[lineS][0], '%H:%M:%S')

            # Store the lengths here to save time when accessing in the loop
            motorLen = len(motorData) - 1
            sensorLen = len(sensorData) -1

            length = motorLen + sensorLen

            # This loop goes through each row of both lists, going back and forth between the two
            for i in range(length):
                # Write the current lines for the actuators and sensors
                outLine = [sensorData[lineS][0]]
                outLine.extend([motorData[lineM][0]])
                outLine.extend(sensorData[lineS][1:])
                outLine.extend(motorData[lineM][1:])
                outWriter.writerow(outLine)

                # if we are at the end of both csv files
                if lineS == sensorLen and lineM == motorLen:
                    break
                # if motor time is bigger than sensor time, update sensor
                elif currentMotor > currentSensor:
                    if lineS < sensorLen:
                        lineS += 1
                        currentSensor = datetime.datetime.strptime(sensorData[lineS][0], '%H:%M:%S')
                    else:
                        lineM += 1
                # if sensor time is bigger than motor time, update motor
                elif currentMotor < currentSensor:
                    if lineM < motorLen:
                        lineM += 1
                        currentMotor = datetime.datetime.strptime(motorData[lineM][0], '%H:%M:%S')
                    else:
                        lineS += 1
                # if both times are equal, update both
                else:
                    i += 1
                    lineS += 1
                    lineM += 1
                    currentSensor = datetime.datetime.strptime(sensorData[lineS][0], '%H:%M:%S')
                    currentMotor = datetime.datetime.strptime(motorData[lineM][0], '%H:%M:%S')


combine_outputs("charlotte_sim_1_cooltoofast_states.csv", "cleaned_charlotte_sim_1_cooltoofast_sensors.csv")
