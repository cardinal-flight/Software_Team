# Derrek Brock
# Created 2-26-19
# Last Edited 2-26-19

python -m pip install numpy
# Installs numpy library

class Plane_2:
    # Creates Plane 2 class and related information
    def__init__(self, position, velocity, aircraft_priority):
        self.position = [0, 0, 0]
        # Sets position of aircraft
        self.velocity = [0, 0, 0]
        # Sets velocity of aircraft
        self.aircraft_priority = 2
        # Sets aircraft priority for the aircraft
        # High priority number = high priority, low priority number = low priority 
