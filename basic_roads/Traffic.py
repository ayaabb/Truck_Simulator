from Classes.Road import*


def Traffic(length, truck):
    road = Road_type("Traffic", 1.5, -13, 0.8)

    if length <= truck.remaining_distance():
        print("The truck is driving on Traffic road")
        truck.apply_terrain_effects(road, length)
        return True
    return False
