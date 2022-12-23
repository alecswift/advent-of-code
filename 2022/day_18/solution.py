# Create 3d array initialized at max z, max y, max x
# look for zeroes surrounded by 1s
# [[[1,1,1][1,1,1]]]
from itertools import combinations
from re import findall

def parse(input_file):
    in_file = open(input_file, 'r', encoding = 'utf-8')
    with open(input_file, encoding = 'utf-8') as in_file:
        input_data = in_file.read()
    split_lines = input_data.split('\n')
    coords = [findall(r'(\d+),(\d+),(\d+)', line)[0] for line in split_lines]
    return sorted((tuple(map(int, coord)) for coord in coords), key = lambda point: sum(point))

cubes = parse('2022/day_18/input_test.txt')

def find_connections(cube_data):
    pairs = combinations(cube_data, 2)
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
    print(connections)
    return (len(cube_data) * 6) - (connections * 2)

def trapped_air():
    air_cubes = []
    for cube in cubes:
        x_coord, y_coord, z_coord = cube
        if (x_coord + 1, y_coord + 1, z_coord) not in cubes:
            continue
        if (x_coord - 1, y_coord + 1, z_coord) not in cubes:
            continue
        if (x_coord, y_coord + 2, z_coord) not in cubes:
            continue
        if (x_coord, y_coord + 1, z_coord + 1) not in cubes:
            continue
        if (x_coord, y_coord + 1, z_coord - 1) not in cubes:
            continue
        if (x_coord, y_coord + 1, z_coord) in cubes:
            continue
        air_cubes.append((x_coord, y_coord + 1, z_coord))
    return air_cubes


print(find_connections(cubes))
print(find_connections(cubes) - find_connections(trapped_air()))
