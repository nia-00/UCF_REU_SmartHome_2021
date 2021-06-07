# IMPORTS
import time
from adafruit_servokit import ServoKit
import sys
import os
import csv
import RPi.GPIO as GPIO
from datetime import datetime
from time import strftime
import pdb

kit = ServoKit(channels=16)
# The Home class holds all of the rooms, appliances, doors, and windows in the
# house and acts as a hub for large scale commands like opening and closing all
# the windows and doors.
class Home:
    name = 'SmartHomeModel'
    def __init__(self, rooms, appliances, doors, windows):
        self.rooms = rooms
        self.appliances = appliances
        self.doors = doors
        self.windows = windows


    # These next few functions returns a list of the names of the different
    # objects in the house. This is used later to create the column names
    # for the output csv file.
    def getRooms(self):
        rL = []
        for r in self.rooms:
            rL.append(r.name)
        return rL


    def getApps(self):
        aL = []
        for a in self.appliances:
            aL.append(a.name)
        return aL


    def getDoors(self):
        dL = []
        for d in self.doors:
            dL.append(d.name)
        return dL


    def getDoorNicknames(self):
        dN = []
        for d in self.doors:
            dN.append(d.nickname)
        return dN


    def getWindows(self):
        wL = []
        for w in self.windows:
            wL.append(w.name)
        return wL


    def getWindowNicknames(self):
        wN = []
        for w in self.windows:
            wN.append(w.nickname)
        return wN


    # This function outputs the states of all the objects in the house (except
    # the rooms as they don't have states).
    def getStates(self):
        states = []
        # get appliance states
        states.append(strftime("%H:%M:%S"))
        for a in self.appliances:
            states.append(a.getState())
        # get door states
        for d in self.doors:
            states.append(d.getState())
        # get window states
        for w in self.windows:
            states.append(w.getState())
        return states


    # The next few functions add different things to the house so it can be built
    # in the controlTower class
    def addRoom(self, newRoom):
        self.rooms.append(newRoom)


    def addWindow(self, newWindow):
        self.windows.append(newRoom)


    def addDoor(self, newDoor):
        self.doors.append(newDoor)


    def addAppliance(self, newApp):
        self.appliances.append(newApp)


    # These next few functions control large scale operations of the house.
    def openWindows(self):
        print('opening all windows...')
        for w in self.windows:
            w.openHinge()


    def closeWindows(self):
        print('closing all windows...')
        for w in self.windows:
            w.closeHinge()


    def openDoors(self):
        print('opening all doors...')
        for d in self.doors:
            d.openHinge()


    def closeDoors(self):
        print('closing all doors...')
        for d in self.doors:
            d.closeHinge()


    def openEverything(self):
        print('opening everything...')
        self.openWindows()
        self.openDoors()


    def closeEverything(self):
        print('closing everything...')
        self.closeWindows()
        self.closeDoors()


    def turnEverythingOn(self):
        print('turning on all appliances...')
        for a in self.appliances:
            a.turnOn()


    def turnEverythingOff(self):
        print('turning off all appliances...')
        for a in self.appliances:
            a.turnOff()


    # toString function
    def __str__(self):
        output = "Home: " + name + "\n\t**Rooms**"
        for r in rooms:
            output += "\n" + r
        output += "\n\t**Appliances**"
        for ap in appliances:
            output += "\n\t~" + ap

# The Room class acts as an organizational vehicle for the house. It contains all
# the doors and windows associated with an individual room in the house.
class Room:
    def __init__(self, name, door_list, window_list):
        self.name = name
        self.door_list = door_list
        self.window_list = window_list


    def addRoom(self, newRoom):
        self.door_list.append(newRoom)


    def addWindow(self, newWindow):
        self.window_list.append(newWindow)


    def __str__(self):
        output = "\t~Room: " + name + "\n\t\t**Doors**"
        for door in door_list:
            output += "\n\t\t-" + door
        output += "\n\t\t**Windows**"
        for window in window_list:
                output += "\n\t\t-" + window
        return output

# The Motor class is a parent class for all the objects in the house that can be
# controlled (i.e. doors, windows, and appliances).
class Motor:
    def __init__(self, name, nickname, pin):
        self.name = name
        self.nickname = nickname
        self.pin = int(pin)
        self.state = 0

    def __str__(self):
        out = "This is a " + self.name + " with the pin number " + str(self.pin) + "."
        return out

    def getState(self):
        return self.state

# The Hinge class is for the doors and windows of the house. It controls the
# opening and closing mechanism.
class Hinge(Motor):

    def __init__(self, name, nickname,  pin):
        super().__init__(name, nickname, pin)
        # This sets the opening angles of each pin
        if self.pin == 2 or self.pin == 13:
            self.openingAngle = 150
        elif self.pin == 15:
            self.openingAngle = 147
        else:
            self.openingAngle = 180
        # This sets the closing angle of each pin
        if self.pin == 10:
            self.closingAngle = 65
        elif self.pin == 12:
            self.closingAngle = 50
        elif self.pin == 15:
            self.closingAngle = 58
        elif pin == 6:
            self.closingAngle = 55
        else:
            self.closingAngle = 60

    def openHinge(self):
        print('opening ' + self.name + '...')
        kit.servo[self.pin].angle = self.openingAngle
        self.state = 1


    def closeHinge(self):
        print('closing ' + self.name + '...')
        kit.servo[self.pin].angle = self.closingAngle
        self.state = 0


# The Appliance class is for the appliances in the house that control the
# temperature (i.e. the heater, lamp, etc.). It controls the on and off
# mechanism.
class Appliance(Motor):
    def __init__(self, name, pin):
        super().__init__(name, name, pin)
        GPIO.setup(self.pin, GPIO.OUT)


    def turnOn(self):
        print('turning on ' + self.name + '...')
        GPIO.output(self.pin, GPIO.HIGH)
        self.state = 1


    def turnOff(self):
        print('turning off ' + self.name + '...')
        GPIO.output(self.pin, GPIO.LOW)
        self.state = 0


class ControlTower():

    def getObject(self, name, listOfNames, listOfObjects):
        try:
            index = listOfNames.index(name)
            return listOfObjects[index]
        except ValueError:
            return None


    def readInstructions(self, home, filename):
        print('Starting Simulation...')

        with open(filename, "r") as simFile, open("appliance_and_motor_states1.csv", "w") as outFile:
            # get the column titles for the csv file
            time_header = "Time on " + strftime("%d %b %Y")
            fieldnames = [time_header]
            fieldnames.extend(list(home.getApps()))
            fieldnames.extend(home.getDoors())
            fieldnames.extend(home.getWindows())
            out_writer = csv.writer(outFile, delimiter = ',')
            out_writer.writerow(fieldnames)

            # save the list of names and objects we need to use in the for loop to save time
            appsName = home.getApps()
            doorsName = home.getDoorNicknames()
            windowsName = home.getWindowNicknames()
            apps = home.appliances
            doors = home.doors
            windows = home.windows
            timeSkip = 0

            # The initial state of the house is collected before anything is turned on or opened
            out_writer.writerow(home.getStates())

            # This for loop goes line by line in the input file. It splits each line into
            # a list of strings and starts the for loop to go through each string.
            for line in simFile:
                splitLine = line.strip().lower().split()
                i = 0
                current = None
                lineLen = len(splitLine)
                # This for loop goes through a single line, word by word, and parses it.
                # If the current word is an appliance, it turns it on/off based on the next
                # command. Same with doors and windows. If the string is an integer, that
                # represents the time we remain in the current state
                for i in range(0, lineLen, 2):
                    current = self.getObject(splitLine[i], appsName, apps)
                    if current != None:
                        if splitLine[i + 1] == "on":
                            current.turnOn()
                        elif splitLine[i + 1] =="off":
                            current.turnOff()
                        else:
                            pdb.set_trace()
                            print("Invalid input on word " + str(i) + " in the following line: " + line + "\t" + splitLine[i])
                    current = self.getObject(splitLine[i], doorsName, doors)
                    if current == None:
                        current = self.getObject(splitLine[i], windowsName, windows)
                    if current != None:
                        # get the next word and open or close it
                        if splitLine[i + 1] == "open":
                            current.openHinge()
                        elif splitLine[i + 1] == "close":
                            current.closeHinge()
                        else:
                            print("Invalid input on word " + str(i) + " in the following line: " + line + "\t" + splitLine[i])
                    if splitLine[i].isnumeric():
                        timeSkip = int(splitLine[i])
                        break

                out_writer.writerow(home.getStates())
                time.sleep(timeSkip)

        print("\nEnd of simulation")

    def buildHouse(house):
        # make house object
        # open build house text file
        # return house
        return house



    def main(self, filename):

        # *** BUILDING THE HOUSE ***
        # --appliances--
        # no nickname needed, just use regular name when writing the test file
        lamp = Appliance("lamp", 5)
        heater = Appliance("heater", 6)
        fan = Appliance("fan", 12)
        ac = Appliance("ac", 13)
        applianceList = [lamp, heater, fan, ac]

        # --doors--
        # nicknaming convention: d + the initials of the door name. Example: db2b
        #                       is the -D-oor from -B-edroom -2- to the -B-athroom
        bed2_bath = Hinge("Bedroom 2 to Bathroom","db2b", 0)
        bed1_living = Hinge("Bedroom 1 to Living Room", "db1l", 1)
        living_kitchen = Hinge("Living Room to Kitchen", "dlk",  2)
        living_bath = Hinge("Living Room to Bathroom", "dlb", 3)
        bed1_bath = Hinge("Bedroom 1 to Bathroom", "db1b", 4)
        living_outside = Hinge("Living Room to Outside", "dlo", 5)
        bed1_outside = Hinge("Bedroom 1 to Outside", "db1o", 6)
        doorList = [bed2_bath, bed1_living, living_kitchen, living_bath, bed1_bath, living_outside, bed1_outside]

        # --windows--
        bed1_left = Hinge("Bedroom 1 Left Window", "wb1l", 8)
        living_left = Hinge("Living Room Left Window", "wll",  9)
        bed2_right = Hinge("Bedroom 2 Right Window", "wb2r", 10)
        kitchen_right = Hinge("Kitchen Right Window", "wkr", 11)
        bed2_back = Hinge("Bedroom 2 Back Window", "wb2b", 12)
        living_front = Hinge("Living Room Front Window", "wlf", 13)
        kitchen_front = Hinge("Kitchen Front Window", "wkf", 14)
        bed1_back = Hinge("Bedroom 1 Back Window", "wb1b", 15)
        windowList = [bed1_left, living_left, bed2_right, kitchen_right, bed2_back, living_front, kitchen_front, bed1_back]

        # --rooms--
        bed1 = Room("Bedroom 1", [bed1_living, bed1_bath, bed1_outside], [bed1_left, bed1_back])
        bed2 = Room("Bedroom 2", [bed2_bath], [bed2_right, bed2_back])
        bath = Room("Bathroom", [bed2_bath, living_bath, bed1_bath], [])
        living = Room("Living Room", [bed1_living, living_kitchen, living_bath, living_outside], [living_left, living_front])
        kitchen = Room("Kitchen", [living_kitchen], [kitchen_right, kitchen_front])
        roomList = [bed1, bed2, bath, living, kitchen]

        # --house--
        scaledHome = Home(roomList, applianceList, doorList, windowList)

        # *** CONTROLLING THE HOUSE ***
        #bed1_left.openHinge()
        #time.sleep(5)
        #bed1_left.closeHinge()
        #time.sleep(2)
        #fan.turnOn()
        #time.sleep(5)
        #lamp.turnOff()
        #scaledHome.openEverything()
        #time.sleep(5)
        #scaledHome.closeEverything()

        #self.testFunct()
        #time.sleep(5)

        # incorporate filename here
        self.readInstructions(scaledHome, filename)

        #print(scaledHome.getDoors())

        # make sure to always do GPIO.cleanup() at the end of running bc otherwise
        # it will mess up the appliances
        GPIO.cleanup()



if __name__ == "__main__":
    start = ControlTower()
    filename = "simulation1.txt"
    start.main(filename)
