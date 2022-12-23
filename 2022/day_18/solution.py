# split into combinations, go through each combination and check if it's the same but off by one, if it is count = 1
from itertools import combinations
from re import findall

def parse(input_file):
    in_file = open(input_file, 'r', encoding = 'utf-8')
    with open(input_file, encoding = 'utf-8') as in_file:
        input_data = in_file.read()
    split_lines = input_data.split('\n')
    coords = [findall(r'(\d+),(\d+),(\d+)', line)[0] for line in split_lines]
    return [tuple(map(int, coord)) for coord in coords]

def find_connections(input_file):
    cubes = parse(input_file)
    pairs = combinations(cubes, 2)
    connections = 0
    for cube_1, cube_2 in pairs:
        x_coord, y_coord, z_coord = cube_1
        x_coord_1, y_coord_1, z_coord_1 = cube_2
        if (x_coord == x_coord_1) and (y_coord == y_coord_1) and (abs(z_coord - z_coord_1) == 1):
            connections += 1
        elif (x_coord == x_coord_1) and (abs(y_coord - y_coord_1) == 1) and (z_coord == z_coord_1):
            connections += 1
        elif (abs(x_coord - x_coord_1) == 1) and (y_coord == y_coord_1) and (z_coord == z_coord_1):
            connections += 1
    return (len(cubes) * 6) - (connections * 2)


print(find_connections('/home/alec/Desktop/code/advent_of_code/2022/day_18/input.txt'))