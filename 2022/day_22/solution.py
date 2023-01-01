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
    for row in rows:
        length = len(row)
        if length < max_x:
            row.extend([" "] * (max_x - length))
    columns = array(rows).transpose().tolist()
    return rows, columns


grid_1, procedure_1 = initial_parse("2022/day_22/input_test.txt")
print(parse(grid_1))
