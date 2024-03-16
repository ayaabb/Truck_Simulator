import json
import os
from importlib import import_module


def get_roads_length_dict(roads_file):
    with open(roads_file, 'r') as file:
        road_data = json.load(file)
    return road_data


def load_roads_type():
    roads_file = [f.replace(".py", "") for f in os.listdir('basic_roads') if
                  f.endswith('.py') and not f.startswith("__")]
    basic_roads = {}
    for name_road in roads_file:
        module = import_module(f"basic_roads.{name_road}")
        road_ = getattr(module, name_road)
        if callable(road_):
            basic_roads[name_road] = road_
    return basic_roads
