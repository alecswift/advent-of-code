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
