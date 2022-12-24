# Create 3d array initialized at max z, max y, max x
# look for zeroes surrounded by 1s
# [[[1,1,1][1,1,1]]]
from collections import deque
from itertools import combinations
from re import findall

class Node:
    def __init__(self, coord):
        self.coord = coord
        x_coord, y_coord, z_coord = self.coord
        self.neighbors = [
            (x_coord, y_coord + 1, z_coord),
            (x_coord, y_coord - 1, z_coord),
            (x_coord - 1, y_coord, z_coord),
            (x_coord + 1, y_coord, z_coord),
            (x_coord, y_coord, z_coord + 1),
            (x_coord, y_coord, z_coord - 1),
        ]
        self.visited = False


def parse(input_file):
    in_file = open(input_file, "r", encoding="utf-8")
    with open(input_file, encoding="utf-8") as in_file:
        input_data = in_file.read()
    split_lines = input_data.split("\n")
    coords = [findall(r"(\d+),(\d+),(\d+)", line)[0] for line in split_lines]
    return {tuple(map(int, coord)): Node(tuple(map(int, coord))) for coord in coords}


def find_connections(cube_data):
    pairs = combinations(cube_data, 2)
    connections = 0
    for cube_1, cube_2 in pairs:
        x_coord, y_coord, z_coord = cube_1
        x_coord_1, y_coord_1, z_coord_1 = cube_2
        if (
            (x_coord == x_coord_1)
            and (y_coord == y_coord_1)
            and (abs(z_coord - z_coord_1) == 1)
        ):
            connections += 1
        elif (
            (x_coord == x_coord_1)
            and (abs(y_coord - y_coord_1) == 1)
            and (z_coord == z_coord_1)
        ):
            connections += 1
        elif (
            (abs(x_coord - x_coord_1) == 1)
            and (y_coord == y_coord_1)
            and (z_coord == z_coord_1)
        ):
            connections += 1
    return (len(cube_data) * 6) - (connections * 2)


def grid_3d(cube_data):
    grid = [[[0] * 22 for _ in range(22)] for _ in range(22)]
    for coord in cube_data:
        x_coord, y_coord, z_coord = coord
        grid[z_coord][y_coord][x_coord] = 1
    return grid

def boundary_space(coord, boundaries):
    max_x, max_y, max_z, min_x, min_y, min_z = boundaries
    x_coord, y_coord, z_coord = coord
    if (min_x > x_coord) or (max_x < x_coord):
        return True
    if (min_y > y_coord) or (max_y < y_coord):
        return True
    if (min_z > z_coord) or (max_z < z_coord):
        return True
    return False


cubes = parse("2022/day_18/input.txt")
print(find_connections(cubes))
grid_1 = grid_3d(cubes)
# at this point need to track functions to right vars
air_droplets = []
bs = False
boundaries = {}

root = (0, 0, 0)
boundaries[root] = Node(root)
boundaries[root].visited = True
empty_spaces_queue = deque([root])
grid_1[0][0][0] = 2
while empty_spaces_queue:
    current_node = empty_spaces_queue.popleft()
    for neighbor in boundaries[current_node].neighbors:
        x, y, z = neighbor
        if (0 <= x <= 21) and (0 <= y <= 21) and (0 <= z <= 21) and (neighbor not in cubes):
            if neighbor not in boundaries:
                boundaries[neighbor] = Node(neighbor)
            if not boundaries[neighbor].visited:
                empty_spaces_queue.append(neighbor)
                grid_1[z][y][x] = 2
                boundaries[neighbor].visited = True

air_droplets = []
for z_coord, z_row in enumerate(grid_1):
    for y_coord, y_row in enumerate(z_row):
        for x_coord, element in enumerate(y_row):
            if not element:
                air_droplets.append((x_coord, y_coord, z_coord))

print(find_connections(cubes) - find_connections(air_droplets))
