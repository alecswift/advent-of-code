"""
Find the shortest path from the start point to end point on a grid with moving obstacles
"""
from collections import deque


def parse(input_file):
    """
    Return the start point, end point, set of blizzards,
    dictionary of grid points with neighbors, and the max x
    and y coordinates of the grid from the given input file
    """
    with open(input_file, encoding="utf-8") as in_file:
        input_data = in_file.read()
    split_lines = input_data.split("\n")
    blizzards = set()
    nodes = {}
    max_y = len(split_lines) - 1
    max_x = len(split_lines[0]) - 1
    start = (1, max_y)
    end = (max_x - 1, 0)
    for y_coord, row in zip(range(max_y, -1, -1), split_lines):
        for x_coord, item in enumerate(row):
            if item == "#":
                continue
            if item in (">", "<", "v", "^"):
                blizzards.add((item, (x_coord, y_coord)))
                nodes[(x_coord, y_coord)] = build_neighbors(
                    x_coord, y_coord, max_y, row
                )
            else:
                nodes[(x_coord, y_coord)] = build_neighbors(
                    x_coord, y_coord, max_y, row
                )
    x_coord, y_coord = start
    nodes[start] = [(x_coord, y_coord - 1)]
    x_coord, y_coord = end
    nodes[end] = [(x_coord, y_coord + 1)]
    nodes = {coord: neighbors + [coord] for coord, neighbors in nodes.items()}
    return start, end, blizzards, nodes, max_x, max_y
    # Remove walls if unneeded


def build_neighbors(x_coord, y_coord, max_y, row):
    """Return the neighbors of a point on a grid"""
    neighbors = [
        (x_coord + 1, y_coord),
        (x_coord - 1, y_coord),
        (x_coord, y_coord + 1),
        (x_coord, y_coord - 1),
    ]
    if x_coord == 1:
        neighbors.pop(1)
        if y_coord == 1:
            neighbors.pop(2)
    elif x_coord == len(row) - 2:
        neighbors.pop(0)
        if y_coord == max_y - 1:
            neighbors.pop(1)
    elif y_coord == 1:
        neighbors.pop(3)
    elif y_coord == max_y - 1:
        neighbors.pop(2)
    return neighbors


def search(nodes, blizzards, start, end, max_x, max_y, start_time=0):
    """
    Utilizes a breadth first search to find the shortest path from
    the start point and end point with a given adjacency list, start
    time, and set of blizzard points (the movable obstacles)
    """
    if not start_time:
        blizzard_dict = {0: blizzards}
        bliz_wout_directions = {0: {coord for _, coord in blizzards}}
    else:
        blizzard_dict, bliz_wout_directions = blizzards
    seen = set([(start_time, start)])
    queue = deque([(start_time, start)])
    while queue:
        time, coord = queue[0]
        if coord == end:
            return time, (blizzard_dict, bliz_wout_directions)
        future = time + 1
        if future not in blizzard_dict:
            blizzard_dict[future] = move_blizzards(blizzard_dict[time], max_x, max_y)
        if future not in bliz_wout_directions:
            bliz_wout_directions[future] = {coord for _, coord in blizzard_dict[future]}
        for neighbor in nodes[coord]:
            if (
                neighbor not in bliz_wout_directions[future]
                and (future, neighbor) not in seen
            ):
                seen.add((future, neighbor))
                queue.append((future, neighbor))
        # add the same point to the queue for the case of staying in place
        queue.popleft()
    return time


def move_blizzards(blizzards, max_x, max_y):
    """
    Return an updated set of blizzard points with the given set
    """
    new_blizzards = set()
    for blizzard in blizzards:
        direction, coord = blizzard
        x_coord, y_coord = coord
        match direction:
            case "^":
                if y_coord == max_y - 1:
                    new_blizzards.add((direction, (x_coord, 1)))
                else:
                    new_blizzards.add((direction, (x_coord, y_coord + 1)))
            case "v":
                if y_coord == 1:
                    new_blizzards.add((direction, (x_coord, max_y - 1)))
                else:
                    new_blizzards.add((direction, (x_coord, y_coord - 1)))
            case "<":
                if x_coord == 1:
                    new_blizzards.add((direction, (max_x - 1, y_coord)))
                else:
                    new_blizzards.add((direction, (x_coord - 1, y_coord)))
            case ">":
                if x_coord == max_x - 1:
                    new_blizzards.add((direction, (1, y_coord)))
                else:
                    new_blizzards.add((direction, (x_coord + 1, y_coord)))
    return new_blizzards


def find_times(input_file):
    """
    Find the time it takes to move from the start point to the end point.
    And the time it takes to go back to the start point then back to the end point
    """
    start, end, blizzards, nodes, max_x, max_y = parse(input_file)
    time, blizzards_2 = search(nodes, blizzards, start, end, max_x, max_y)
    time_2, blizzards_3 = search(nodes, blizzards_2, end, start, max_x, max_y, time)
    time_3, _ = search(nodes, blizzards_3, start, end, max_x, max_y, time_2)
    return time, time_3


print(find_times("2022/day_24/input.txt"))
