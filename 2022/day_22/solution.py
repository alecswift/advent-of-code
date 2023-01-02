from collections import deque
from re import findall
from numpy import array


def initial_parse(input_file):
    in_file = open(input_file, "r", encoding="utf-8")
    with open(input_file, encoding="utf-8") as in_file:
        input_data = in_file.read()
    grid_str, procedure_str = input_data.split("\n\n")
    procedure = [
        int(instruction) if instruction.isdigit() else instruction
        for instruction in findall(r"[\d]+|[RL]", procedure_str)
    ]
    grid = grid_str.split("\n")
    return grid, procedure


def parse(grid):
    rows = [list(row) for row in grid]
    max_x = max([len(row) for row in rows])
    # Add white spaces to the end of rows to equalize lengths
    for row in rows:
        length = len(row)
        if length < max_x:
            row.extend([" "] * (max_x - length))
    columns = array(rows).transpose().tolist()
    return rows, columns


def wrapper(rows):
    walls = set()
    start = False
    west_wrappers = {}
    # While iterating through characters in grid: add wall coordinates to a set
    # and connect the start of nonempty spaces to the end in a wrapper dict
    for y_coord, row in zip(range(len(rows) - 1, -1, -1), rows):
        for x_coord, char in enumerate(row):
            if char != " ":
                if not start:
                    start = True
                    start_coord = complex(x_coord, y_coord)
                if char == "#":
                    walls.add(complex(x_coord, y_coord))
            elif start:
                end_coord = complex(x_coord - 1, y_coord)
                west_wrappers[start_coord] = end_coord
                start = False
                break
        else:
            end_coord = complex(len(row) - 1, y_coord)
            west_wrappers[start_coord] = end_coord
            start = False

    east_wrappers = {}
    for key, value in list(west_wrappers.items()):
        east_wrappers[value] = key
    for key in west_wrappers:
        start_point = key
        break
    return west_wrappers, east_wrappers, walls, start_point


def wrapper_col(columns):
    start = False
    north_wrappers = {}
    # Same as previous function except for columns
    for x_coord, column in enumerate(columns):
        for y_coord, char in zip(range(len(column) - 1, -1, -1), column):
            if char != " ":
                if not start:
                    start = True
                    start_coord = complex(x_coord, y_coord)
            elif start:
                end_coord = complex(x_coord, y_coord + 1)
                north_wrappers[start_coord] = end_coord
                start = False
                break
        else:
            end_coord = complex(x_coord, 0)
            north_wrappers[start_coord] = end_coord
            start = False

    south_wrappers = {}
    for key, value in list(north_wrappers.items()):
        south_wrappers[value] = key
    return north_wrappers, south_wrappers


def execute_proc(start_point, walls, wrappers, procedure):
    north_wrappers, south_wrappers, west_wrappers, east_wrappers = wrappers
    directions = deque([1, -1j, -1, 1j])
    prev_point = None
    current_point = start_point
    for item in procedure:
        if isinstance(item, int):
            for _ in range(item):
                if current_point in walls:
                    current_point = prev_point
                    break
                if (directions[0] == 1) and (current_point in east_wrappers):
                    prev_point = current_point
                    current_point = east_wrappers[current_point]
                elif (directions[0] == -1) and (current_point in west_wrappers):
                    prev_point = current_point
                    current_point = west_wrappers[current_point]
                elif (directions[0] == 1j) and (current_point in north_wrappers):
                    prev_point = current_point
                    current_point = north_wrappers[current_point]
                elif (directions[0] == -1j) and (current_point in south_wrappers):
                    prev_point = current_point
                    current_point = south_wrappers[current_point]
                else:
                    prev_point = current_point
                    current_point += directions[0]
                    if current_point in walls:
                        current_point = prev_point
                        break
        else:
            if item == "L":
                directions.rotate()
            else:
                directions.rotate(-1)
    return current_point, directions[0]

    # write algo for movement


grid_1, procedure_1 = initial_parse("2022/day_22/input.txt")
rows_1, columns_1 = parse(grid_1)
print(len(rows_1))
west_wrappers_1, east_wrappers_1, walls_1, start_point_1 = wrapper(rows_1)
north_wrappers_1, south_wrappers_1 = wrapper_col(columns_1)
wrappers_1 = north_wrappers_1, south_wrappers_1, west_wrappers_1, east_wrappers_1
final_coord, facing = execute_proc(start_point_1, walls_1, wrappers_1, procedure_1)
print(facing)
print(((final_coord.real + 1)*4) + ((len(rows_1) - final_coord.imag) * 1000) + 2)
