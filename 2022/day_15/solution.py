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
    with open(input_file, encoding="utf-8") as in_file:
        input_data = in_file.read()
    split_lines = split(r"\n", input_data)
    split_sensors = [findall(r"x=([-\d]+), y=([-\d]+)", line) for line in split_lines]
    sensors = {
        tuple(map(int, sensor)): tuple(map(int, beacon))
        for sensor, beacon in split_sensors
    }
    return sensors


def manhattan_distance(point_1, point_2):
    """Return the manhattan distance of two points"""
    x_coord_1, y_coord_1 = point_1
    x_coord_2, y_coord_2 = point_2
    return abs(x_coord_1 - x_coord_2) + abs(y_coord_1 - y_coord_2)


def distance_dict(input_file):
    """
    Return a dictionary that maps sensors to the distance between
    a sensor and a beacon from the given input file
    """
    sensors = parse(input_file)
    return {sensor: manhattan_distance(sensor, beacon) for sensor, beacon in sensors.items()}
    # could move this code into parse function

def move(point, direction):
    """Return the new point after moving a coordinate left or right"""
    x_coord, y_coord = point
    match direction:
        case 'left':
            point = x_coord - 1, y_coord
        case 'right':
            point = x_coord + 1, y_coord
    return point

def spaces_without_beacons(input_file):
    """
    Return the number of spaces without beacons on
    the row y = 2,000,000 from the given input file
    """
    distances = distance_dict(input_file)
    beacons = set(parse(input_file).values())
    points = set()
    y_row = 2000000
    for sensor, distance in distances.items():
        x_coord, _ = sensor
        distance_to_y_row = manhattan_distance(sensor, (x_coord, y_row))
        if distance_to_y_row <= distance:
            point_on_y_row = (x_coord, y_row)
            points.add(point_on_y_row)
            temp_point = point_on_y_row
            for _ in range(distance - distance_to_y_row):
                temp_point = move(temp_point, 'left')
                points.add(temp_point)
            temp_point = point_on_y_row
            for _ in range(distance - distance_to_y_row):
                temp_point = move(temp_point, 'right')
                points.add(temp_point)
    return len(points.difference(beacons))

def tuning_frequency(input_file):
    """
    Return the tuning frequency (x * 4000000 + y) of the distress
    signal location from the input file by locating boundary points
    of sensors and checking every boundary point for the distress beacon
    """
    sensors = distance_dict(input_file)
    points = set()
    for point, distance in sensors.items():
        x_coord, y_coord = point
        for boundary_point in zip(
            list(range(x_coord, y_coord + distance + 2)) * 2,
            range(y_coord - distance - 1, y_coord + distance + 2)
        ):
            x_coord_1, y_coord_1 = boundary_point
            if (0 <= x_coord_1 <= 4000000) and (0 <= y_coord_1 <= 4000000):
                points.add(boundary_point)
    for boundary_point in points:
        for point, distance in sensors.items():
            if distance >= manhattan_distance(point, boundary_point):
                break
        else:
            x_coord, y_coord = boundary_point
            return (x_coord * 4000000) + y_coord

print(spaces_without_beacons('2022/day_15/input.txt'))
print(tuning_frequency('2022/day_15/input.txt'))
