"""
Find the number of grains of sand that have fallen
after the first grain of sand enters the abyss from
the given input data that defines a grid of cave space
"""

from itertools import product
from re import findall, split

def parse(input_file):
    """
    Return a list of lists of coordinates
    (inner list represents a line on a grid)
    from the given input data
    """
    in_file = open(input_file, 'r', encoding = 'utf-8')
    with open(input_file, encoding = 'utf-8') as in_file:
        input_data = in_file.read()
    split_lines = [findall(r'(\d+),(\d+)', line)for line in split(r'\n', input_data)]
    return [[tuple(map(int, coordinate)) for coordinate in line]for line in split_lines]

def init_point_dict(input_file):
    """
    Return a dictionary of all points on a grid from the given input file
    """
    input_data = parse(input_file)
    max_x = max([x_coord for line in input_data for x_coord, _ in line])
    min_x = min([x_coord for line in input_data for x_coord, _ in line])
    max_y = max([y_coord for line in input_data for _, y_coord in line])
    min_y = 0
    points_lst = list(product(range(min_x, max_x +1), range(min_y, max_y +1)))
    sorted_points = sorted(points_lst, key = lambda point: point[1])
    return {point: 0 for point in sorted_points}

def add_rocks(input_file):
    """
    Add rocks of the cave to the points in
    the dictionary from the given input file
    """
    input_data = parse(input_file)
    points = init_point_dict(input_file)
    for line in input_data:
        for num in range(len(line) - 1):
            point_1, point_2 = line[num: num + 2]
            x_1, y_1 = point_1
            x_2, y_2 = point_2
            if x_1 == x_2:
                if y_1 < y_2:
                    for num in range(y_1, y_2 + 1):
                        points[(x_1, num)] = "#"
                if y_1 > y_2:
                    for num in range(y_2, y_1 + 1):
                        points[(x_1, num)] = "#"
            if y_1 == y_2:
                if x_1 < x_2:
                    for num in range(x_1, x_2 + 1):
                        points[(num, y_1)] = "#"
                if x_1 > x_2:
                    for num in range(x_2, x_1 + 1):
                        points[(num, y_1)] = "#"
    points[500, 0] = '+'
    return points

def display(grid):
    """
    Display the 2D slice of cave space with
    # representing rocks, . representing empty space,
    and + representing the source of sand from the
    given dictionary of points.
    """
    count = 0
    grid_str = ''
    for value in grid.values():
        count += 1
        grid_str += value
        if not count % 10:
            grid_str += '\n'
    return grid_str

def move(direction, point):
    """
    Return a new coordinate from a given coordinate
    and the direction to move the coordinate
    """
    x_coord, y_coord = point
    match direction:
        case 'down':
            y_coord += 1
        case 'downleft':
            y_coord += 1
            x_coord -= 1
        case 'downright':
            y_coord += 1
            x_coord += 1
    return x_coord, y_coord

def falling_sand(input_file):
    """
    Return a count of the number of grains of falling sand,
    that move down, downleft, or downright based on the rocks
    in the grid, that can fill the cave before a grain of sand
    enters the abyss (outside the defined grid)
    """
    points = add_rocks(input_file)
    point = (500, 0)
    count = 0
    while points[point] is not None:
        if not points.setdefault(move('down', point)):
            point = move('down', point)
        elif not points.setdefault(move('downleft', point)):
            point = move('downleft', point)
        elif not points.setdefault(move('downright', point)):
            point = move('downright', point)
        else:
            count += 1
            points[point] = 'o'
            point = (500, 0)
    return count


print(falling_sand('2022/day_14/input.txt'))
