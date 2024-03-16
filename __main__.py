import sys
from Classes.simulator import *
from utils import get_roads_length_dict
from Classes.Truck import *


def main():
    roads_file = sys.argv[1]
    roads = get_roads_length_dict(roads_file)
    truck_simulator = Truck_Simulator()
    truck = Truck(10, 5, 1, "Mercedes")
    truck_simulator.start_ride(truck, roads)


if __name__ == '__main__':
    main()
