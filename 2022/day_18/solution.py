"""
Find the surface area of a formation of cubes, then utilize
a flood fill algorithm to find the exterior surface area
"""
from collections import deque
from itertools import combinations
from re import findall


class Node:
    """
    represents a point on a 3d grid with neighbors in six directions
    """

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
    """
    Return a dictionary of 3d coordinates and their node object
    from the given import file
    """
    in_file = open(input_file, "r", encoding="utf-8")
    with open(input_file, encoding="utf-8") as in_file:
        input_data = in_file.read()
    split_lines = input_data.split("\n")
    coords = [findall(r"(\d+),(\d+),(\d+)", line)[0] for line in split_lines]
    return {tuple(map(int, coord)): Node(tuple(map(int, coord))) for coord in coords}


def find_surface_area(cube_data):
    """
    Return the total surface area of a formation of cubes
    from the given cube coordinates
    """
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
    """
    Return a 3 dimensional grid from the given input file.
    1's represent cube coordinates, 0's represent empty spaces
    """
    grid = [[[0] * 22 for _ in range(22)] for _ in range(22)]
    for coord in cube_data:
        x_coord, y_coord, z_coord = coord
        grid[z_coord][y_coord][x_coord] = 1
    return grid


def flood_fill(grid):
    """
    Mutate the given grid utilizing a flood fill algorithm
    through a breadth first search
    """
    boundaries = {}
    root = (0, 0, 0)
    boundaries[root] = Node(root)
    boundaries[root].visited = True
    empty_spaces_queue = deque([root])
    grid[0][0][0] = 2
    while empty_spaces_queue:
        current_node = empty_spaces_queue.popleft()
        for neighbor in boundaries[current_node].neighbors:
            x_coord, y_coord, z_coord = neighbor
            if (
                (0 <= x_coord <= 21)
                and (0 <= y_coord <= 21)
                and (0 <= z_coord <= 21)
                and (neighbor not in cubes)
            ):
                if neighbor not in boundaries:
                    boundaries[neighbor] = Node(neighbor)
                if not boundaries[neighbor].visited:
                    empty_spaces_queue.append(neighbor)
                    grid_1[z_coord][y_coord][x_coord] = 2
                    boundaries[neighbor].visited = True


def count_spaces(grid):
    """
    Count the number of interior spaces from the given flood filled grid
    """
    air_droplets = []
    for z_coord, z_row in enumerate(grid):
        for y_coord, y_row in enumerate(z_row):
            for x_coord, element in enumerate(y_row):
                if not element:
                    air_droplets.append((x_coord, y_coord, z_coord))
    return air_droplets


cubes = parse("2022/day_18/input.txt")
grid_1 = grid_3d(cubes)
surface_area = find_surface_area(cubes)
print(surface_area)
flood_fill(grid_1)
print(surface_area - find_surface_area(count_spaces(grid_1)))
