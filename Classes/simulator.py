from utils import load_roads_type


class Truck_Simulator:
    def __init__(self):
        self.roads_type = load_roads_type()

    def start_ride(self, truck, roads):
        for road in roads:
            if road['road_type'] in self.roads_type.keys():
                if self.roads_type[road['road_type']](road['length'], truck):
                    print(f"The truck finished {road['road_type']} road successfully\n")
                else:
                    print(f"The remaining fuel in the truck won't be enough to reach {road['road_type']} road.\nTruck stopped and can't continue the ride")
                    return
            else:
                print(f"Road {road['road_type']} not found!!")

