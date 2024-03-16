from Classes.Road import *

def Gravel(length, truck):
    road = Road_type("Gravel", 2, -10, 1)
    if length <= truck.remaining_distance():
        print("The truck is driving on Gravel road")
        truck.apply_terrain_effects(road, length)
        return True
    return False
