"""
Find the number of points on a row that can not have a beacon
given an input file the specifies the point of a sensor and
the closest beacon
"""

from re import split, findall


def parse(input_file):
    """
    Return a dictionary that maps sensor points
    to beacon points from the given input file
    """
    in_file = open(input_file, "r", encoding="utf-8")
    with open(input_file, encoding="utf-8") as in_file:
        input_data = in_file.read()
    split_lines = split(r"\n", input_data)
    split_sensors = [findall(r"x=([-\d]+), y=([-\d]+)", line) for line in split_lines]
    sensors = {
        tuple(map(int, sensor)): tuple(map(int, beacon))
        for sensor, beacon in split_sensors
    }
    return sensors

def distance(point_1, point_2):
    """Return the manhattan distance of two points"""
    x_coord_1, y_coord_1 = point_1
    x_coord_2, y_coord_2 = point_2
    return abs(x_coord_1 - x_coord_2) + abs(y_coord_1 - y_coord_2)
