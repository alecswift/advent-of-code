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
    row_wrappers = {}
    for y_coord, row in zip(range(len(rows) -1, -1, -1), rows):
        for x_coord, char in enumerate(row):
            if char != ' ':
                if not start:
                    start = True
                    start_coord = complex(x_coord, y_coord)
                if char == '#':
                    walls.add(complex(x_coord, y_coord))
            elif start:
                end_coord = complex(x_coord, y_coord)
                row_wrappers[start_coord] = end_coord
                start = False
                break
        else:
            end_coord = complex(len(row) - 1, y_coord)
            row_wrappers[start_coord] = end_coord
            start = False
    # add column checker to flip x and y
    # add reverse of keys/values to wrapper dict
    # initialize wrapper dict of rows and columns 
    # write algo for movement
    return row_wrappers, walls




grid_1, procedure_1 = initial_parse("2022/day_22/input_test.txt")
rows_1, columns_1 = parse(grid_1)
print(wrapper(rows_1))
