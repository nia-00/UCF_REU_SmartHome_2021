import RPi.GPIO as GPIO
import os
import Adafruit_DHT
import time
import sys
import csv
import pandas as pd
import numpy as np
import pdb
import threading
from multiprocessing import Process
from datetime import datetime


class temp_sensor:
    sensor = Adafruit_DHT.DHT22
    
    def __init__(self, pin, moving_average_size = 30):
        self.pin = pin
        self.moving_average_size = moving_average_size
        self.last_30_temp = np.zeros(self.moving_average_size)
        self.last_30_hum = np.zeros(self.moving_average_size)
        self.index = 0
        
    def moving_average():
        avg_temp = np.average(self.last_30_temp[self.last_30_temp > 0])
        avg_hum = np.average(self.last_30_hum[self.last_30_hum > 0])
        return avg_hum, avg_temp
    
    def measure(self):
        # read_retry will retry up to 15 times to get a sensor
        # reading (waiting 2 seconds between each retry)
        hum, temp = Adafruit_DHT.read_retry(self.sensor, self.pin)
        #print(pin)
        if hum is None or hum > 100:
            print('Bad humidity data')
            hum = -1
        if temp is None:
            print('Bad temperature data')
            temp = -1
            hum = -1
        else:
            temp = (temp * 1.8) + 32 # C to F conversion
            print('Temp = {0:0.2f}*F  Humidity = {0:0.2f}%'.format(temp, hum))
        
        if self.index == self.moving_average_size:
            self.last_30_temp[0:29] = self.last_30_temp[1:30]
            self.last_30_temp[29] = temp
            self.last_30_hum[0:29] = self.last_30_hum[1:30]
            self.last_30_hum[29] = hum
        else:
            self.last_30_temp[self.index] = temp
            self.last_30_hum[self.index] = hum
            self.index += 1
        
        return hum, temp


# Set sensor type: Options are DHT11, DHT22 or AM2302
 
# Set GPIO sensor is connected to
# Pin 4: Outside
# Pin 6: Bedroom 1 
# Pin 12: Kitchen 1 
# Pin 18: Dining Room
# Pin 19: Bathroom  
# Pin 24: Living Rm 1 
# Pin 25: Living Rm 2 
# Pin 26: Bedroom 2 
sensor_4 = temp_sensor(4)
sensor_6 = temp_sensor(6)
sensor_12 = temp_sensor(12)
sensor_18 = temp_sensor(18)
sensor_19 = temp_sensor(19)
sensor_24 = temp_sensor(24)
sensor_25 = temp_sensor(25)
sensor_26 = temp_sensor(26)

#gpioArray = [sensor_4, sensor_6, sensor_12, sensor_18, sensor_19, sensor_24, sensor_25, sensor_26]
#gpioArray = [sensor_12, sensor_18, sensor_19, sensor_24, sensor_25, sensor_26]
gpioArray = [sensor_4]


def setup():
    GPIO.setmode(GPIO.BCM)
    
    GPIO.setup(21, GPIO.OUT) # Set heating lamp as output
    GPIO.setup(20, GPIO.OUT) # Set fan as output
    
    GPIO.output(21, GPIO.LOW)
    GPIO.output(20, GPIO.LOW)
    

put_header = not os.path.isfile('test.csv')

try:
    with open('testMaxTempFarCornerREAL.csv', 'a') as test:
        fieldnames = 'Time,' + \
                      'S4_Humidity,' +  'S4_Temperature,' +  'S6_Humidity,' +  'S6_Temperature,' + \
                     'S12_Humidity,' + 'S12_Temperature,' + 'S18_Humidity,' + 'S18_Temperature,' + \
                     'S19_Humidity,' + 'S19_Temperature,' + 'S24_Humidity,' + 'S24_Temperature,' + \
                     'S25_Humidity,' + 'S25_Temperature,' + 'S26_Humidity,' + 'S26_Temperature'
            
        if put_header:
            test.write(fieldnames)
                

        
        while(True):
        
            test.flush()
            test.write('\n' + str(datetime.now()))
            print("Collecting data")
            
            #threadInit = threading.Thread(target = temp_sensor.measure, args = tuple(gpioArray,))
            #threadInit.start()
            #threadInit.join()
            
            for sensor in gpioArray:
                humidity, temperature = sensor.measure()
                #pdb.set_trace()
                test.write("{0:.1f}".format(humidity) + "," + "{0:.1f}".format(temperature))
#seconds += 1#print(pin)            
        
        for i in range(0, 1):
            print('Next reading in: ' + str(i)+'/5', flush=True)
            time.sleep(5)
            

except KeyboardInterrupt:
        print("Keyboard Interrupt")
except Exception as e: 
    	print(e)
#finally:
#        GPIO.cleanup()
 
 
#        with open("lamp_stabilization.txt", "a") as datafile:
#            datafile.write('\n')
#            datafile.write(str(datetime.now()) + '\t')
            
            
            
#            print("collecting data")
#            for pin in gpioArray:
#                humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
#                print(pin)
#                checkTemp(pin)
#                if humidity is None:
                    # bad data?
#                    humidity = -1
#                if temperature is None:
                    # bad data?
#                    temperature = -1
#                else:
#                    temperature = (temperature * 1.8) + 32 # C to F
                
#                datafile.write("{0:.1f}".format(humidity) +'\t')
#                datafile.write("{0:.1f}".format(temperature) + '\t') 
#seconds += 1
        
#datafile.write(str(lamp_state) + '\t')
#datafile.write(str(fan_state) + '\t')
        
#if seconds % 30 == 0:
#    if lamp_state == 0:
#        print("turning on lamp")
#        turnOnLamp(21)
#        lamp_state = 1
#    else:
#        print("turning off lamp")
#        turnOffLamp(21)
#        lamp_state = 0
        
#if seconds % 300 == 0:
#    if fan_state == 0:
#        print("turning on fan")
#        turnOnFan(20)
#        fan_state = 1
#    else:
#        print("turning off fan")
#        turnOffFan(20)
#        fan_state = 0
            
#seconds = 0
#lamp_state = 0
#fan_state = 0

#setup()
#turnOnLamp(21)
#lamp_state = 1
#turnOnFan(20)
#fan_state = 1

            #df = pd.read_csv('test.csv', header=None)
            #df.rename(columns={0:   'S4 - Humidity', 1:   'S4 - Temperature',
            #                   2:   'S6 - Humidity', 3:   'S6 - Temperature',
            #                   4:  'S12 - Humidity', 5:  'S12 - Temperature',
            #                   6:  'S18 - Humidity', 7:  'S18 - Temperature',
            #                   8:  'S19 - Humidity', 9:  'S19 - Temperature',
            #                   10: 'S24 - Humidity', 11: 'S24 - Temperature',
            #                   12: 'S25 - Humidity', 13: 'S25 - Temperature',
            #                   14: 'S26 - Humidity', 15: 'S26 - Temperature',})
            
'''
def movingAverageHumidity(humidity, window_size):
    humidity_series = pd.Series(humidity)
    windows = humidity_series.rolling(window_size)
    moving_humidity_averages = round(windows.mean(), 1)
    
    moving_humidity_averages_list = moving_humidity_averages.tolist()
    humidity_without_nans = moving_humidity_averages_list[window_size - 1:]
    
    print('Moving humidity average:')
    print(humidity_without_nans)
    

def movingAverageTemperature(temperature, window_size):
    temperature_series = pd.Series(temperature)
    windows = temperature_series.rolling(window_size)
    moving_temperature_averages = round(windows.mean(), 1)
    
    moving_temperature_averages_list = moving_temperature_averages.tolist()
    temperature_without_nans = moving_temperature_averages_list[window_size - 1:]
    
    print('Moving temperature average:')
    print(temperature_without_nans)
    '''
            
'''
                humidityList.append(humidity)
                if loopIteration >= 3:
                    humidityList.pop()
                    readHumidity += 1
                    if pin == 26:
                        readHumidity = 0
                        movingAverageHumidity(humidityList, 30)
                    
                # Check for bad data
                if humidity is None:
                    humidity = -1
                if temperature is None:
                    temperature = -1
                    humidity = -1
                else:
                    temperature = (temperature * 1.8) + 32 # C to F conversion
                    
                '''
            
'''          # Get temp and check if valid
def checkTemp (gpio):
    if humidity is None or humidity > 100:
        print('Bad humidity data')
    elif temperature is None:
        
    else:
        temp = (temperature * 1.8) + 32
        '''
        
