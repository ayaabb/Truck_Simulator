from Classes.Road import *


def Bad(length, truck):
    road = Road_type("Bad", 4, -30, 2)

    if length <= truck.remaining_distance():
        print("The truck is driving on Bad road:")
        truck.apply_terrain_effects(road, length)
        return True
    return False
