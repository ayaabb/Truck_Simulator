from Classes.Road import *


def Smooth(length, truck):
    road = Road_type("Smooth", 1, 15, 0.5)

    if length <= truck.remaining_distance():
        print("The truck is driving on Smooth road")
        truck.apply_terrain_effects(road, length)
        return True
    return False
