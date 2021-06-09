# Simulation Files Breakdown

The purpose of the simulation files is to mimic the movement of a person or
multiple people around the house. Here, we will walk you through the format of
the input files, as well as describe what each file is simulating.

## Input Format

Each line in the input file describes a new state for the house. First, appliances
are toggled on or off. Then, doors and windows are opened or closed. The last part
of each line is a number, representing the number of seconds the house should
remain in the current state.

In order to make the simulation files more readable, we have added commenting
capabilities. To signal that a line is a comment instead of a command, start the
line with "* ". The space after the asterisk is necessary.

The appliances are referred to by name however, the doors and windows are referred
to using nicknames. The nicknaming convention is as follows:
- The first letter designates whether we are referring to a door (d) or window (w).
- The second letter for doors refers to the room it is opening in (ex. b1 for bedroom 1).
- The second letter for windows refers to the room the window is in (ex. k for kitchen).
- The last letter for doors refers to the room it opens into (ex. b for bathroom).
- The last letter for windows refers the side of the house the window is on (ex. f for front, l for left).

## Simulation Description

There are 3 different kinds of simulations. Each location has a version of all the
simulations with differences in outdoor appliances to model the changes in that
location's temperature and humidity. Below are descriptions of each kind of simulation
a location will have.

* **Simulation 1:** These simulate a single person waking up in the morning,
getting ready for work, and leaving for the day. The house remains empty for a bit
and then the person comes back from work, prepares dinner and gets ready for bed.
* **Simulation 2:** These simulate two people going about their morning routine,
and leaving together. The house remains empty for a bit and then the two people
get back home and go about their nightly routine together.
* **Simulation 3:** These simulate a family of three getting ready for the day.
Two people reside in Bedroom 1 and one person resides in Bedroom 2. At the end
of the simulation, two people leave the home and one person stays behind and
continues to move about the house. At the end of the day, the two that left get
back home, the three have dinner together and go about their nightly routine.
