# Simulation Files Breakdown

The purpose of the simulation files is to mimic the movement of a person or
multiple people around the house. Here, we will walk you through the format of
the input files, as well as describe what each file is simulating.

## Input Format

Each line in the input file describes a new state for the house. First, appliances
are toggled on or off. Then, doors and windows are opened or closed. The last part
of each line is a number, representing the number of seconds the house should
remain in the current state.

The appliances are referred to by name however, the doors and windows are referred
to using nicknames. The nicknaming convention is as follows:
- The first letter designates whether we are referring to a door (d) or window (w).
- The second letter for doors refers to the room it is opening in (ex. b1 for bedroom 1).
- The second letter for windows refers to the room the window is in (ex. k for kitchen).
- The last letter for doors refers to the room it opens into (ex. b for bathroom).
- The last letter for windows refers the side of the house the window is on (ex. f for front, l for left).

## Simulation Description

* **Simulation 1:** This simulates a single person waking up in the morning,
getting ready for work, and leaving for the day.
* **Simulation 2:** This simulated a single person coming back from work, preparing
dinner, getting ready for bed, and going to sleep.
* **Simulation 3:** This simulated two people going about their morning routine,
and leaving together.
* **Simulation 4:** This simulates two people getting home and going about their
nightly routine together.
* **Simulation 5:** This simulates a family of three getting ready for the day.
Two people reside in Bedroom 1 and one person resides in Bedroom 2. At the end
of the simulation, two people leave the home and one person stays behind and
continues to move about the house.
* **Simulation 6:** This simulates a family of three at the end of a typical weekday.
Two people return home and the three people have dinner together and prepare for bed. 
