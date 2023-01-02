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
    # While iterating through characters in grid: add wall coordinates to a set
    # and connect the start of nonempty spaces to the end in a wrapper dict
    for y_coord, row in zip(range(len(rows) -1, -1, -1), rows):
        for x_coord, char in enumerate(row):
            if char != ' ':
                if not start:
                    start = True
                    start_coord = complex(x_coord, y_coord)
                if char == '#':
                    walls.add(complex(x_coord, y_coord))
            elif start:
                end_coord = complex(x_coord - 1, y_coord)
                row_wrappers[start_coord] = end_coord
                start = False
                break
        else:
            end_coord = complex(len(row) - 1, y_coord)
            row_wrappers[start_coord] = end_coord
            start = False

    for key, value in list(row_wrappers.items()):
        row_wrappers[value] = key
    for key in row_wrappers:
        start_point = key
        break
    return len(row_wrappers), len(walls), start_point

def wrapper_col(columns):
    start = False
    col_wrappers = {}
    # Same as previous function except for columns
    for x_coord, column in enumerate(columns):
        for y_coord, char in zip(range(len(column) -1, -1, -1), column):
            if char != ' ':
                if not start:
                    start = True
                    start_coord = complex(x_coord, y_coord)
            elif start:
                end_coord = complex(x_coord, y_coord + 1)
                col_wrappers[start_coord] = end_coord
                start = False
                break
        else:
            end_coord = complex(x_coord, 0)
            col_wrappers[start_coord] = end_coord
            start = False

    for key, value in list(col_wrappers.items()):
        col_wrappers[value] = key
    return len(col_wrappers)

 
    # write algo for movement
grid_1, procedure_1 = initial_parse("2022/day_22/input_test.txt")
rows_1, columns_1 = parse(grid_1)
print(wrapper(rows_1))
print(wrapper_col(columns_1))
