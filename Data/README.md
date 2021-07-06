# Data Overview

The folders above contain different kinds of data we used for this project.

The [Machine Learning](https://github.com/nia-00/UCF_REU_SmartHome_2021/tree/main/Data/Machine_Learning)
folder contains the results of our machine learning algorithms represented as
graphs. We fed each algorithm two datasets, one with time as an input and one without.
For each run we graphed all the sensor predictions vs actual values for temperature
and humidity. There is a graph for each room in the house as well as one for the
entire house.

The [Simulation_Data](https://github.com/nia-00/UCF_REU_SmartHome_2021/tree/main/Data/Simulation_Data)
folder contains all the data we have collected from the house when
running simulations. There is a subfolder for the separate sensor and actuator readings
and a subfolder for the cleaned combined data files we will use for our machine
learning algorithms. The sensor and motor output files are combined using their
timestamps. The sensor readings and motor states that happen in the same time range
are combined into one line, so there are some times that are repeated for both
sensor readings and motor readings. This is because these data points are collected
at different time intervals. There may be multiple sensor readings for one state
of the house and multiple states for one sensor reading. There is another subfolder
that contains the clean combined data with the time as a sinusoidal variable.

The [Stabilization](https://github.com/nia-00/UCF_REU_SmartHome_2021/tree/main/Data/Stabilization)
folder contains all of the appliance stabilization data we collected. This
data was used to determine the limitations of what we can model in the house
in regards to temperature and humidity. In addition this data was used to determine
the timing to use to reach target scaled temperatures in the simulations. We ran
each appliance individually until it reached its maximum or minimum temperature
or humidity. We then turned off the appliance and continued to record sensor
readings until they returned to the starting temperature and humidity.


The [Weather](https://github.com/nia-00/UCF_REU_SmartHome_2021/tree/main/Data/Weather)
folder contains the real world data for each of our chosen cities. Further descriptions
of the data and how we used it can be found in this folder as well.
