from collections import deque

def parse(input_file):
    in_file = open(input_file, "r", encoding="utf-8")
    with open(input_file, encoding="utf-8") as in_file:
        input_data = in_file.read()
    split_lines = input_data.split("\n")
    blizzards = set()
    walls = set()
    nodes = {}
    max_y = len(split_lines) - 1
    max_x = len(split_lines[0]) - 1
    start = (1, max_y)
    end = (max_x - 1, 0)
    for y_coord, row in zip(range(max_y, -1, -1), split_lines):
        for x_coord, item in enumerate(row):
            if item == "#":
                walls.add((x_coord, y_coord))
            elif item in (">", "<", "v", "^"):
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
    return start, end, blizzards, walls, nodes, max_x, max_y
    # Remove walls if unneeded


def build_neighbors(x_coord, y_coord, max_y, row):
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

def search(nodes, blizzards, start, end, max_x, max_y):
    blizzard_dict = {0: blizzards}
    bliz_wout_directions = {0: {coord for _, coord in blizzards}}
    queue = deque([(0, start)])
    while queue:
        time, coord = queue[0]
        if (time + 1) not in blizzard_dict:
                blizzard_dict[time + 1] = insert_blizzard(blizzard_dict[time], max_x, max_y)
                del blizzard_dict[time]
        if (time + 1) not in bliz_wout_directions:
            bliz_wout_directions[time + 1] = {coord for _, coord in blizzard_dict[time + 1]}
            del bliz_wout_directions[time]
        for neighbor in nodes[coord]:
            if neighbor == end:
                return time + 1
            if neighbor not in bliz_wout_directions[time + 1]:
                queue.append((time + 1, neighbor))
        # add the same point to the queue for the case of staying in place
        queue.append((time + 1, coord))
        queue.popleft()

def insert_blizzard(blizzards, max_x, max_y):
    new_blizzards = set()
    for blizzard in blizzards:
        direction, coord = blizzard
        x_coord, y_coord = coord
        match direction:
            case '^':
                if y_coord == max_y - 1:
                    new_blizzards.add((direction, (x_coord, 1)))
                else:
                    new_blizzards.add((direction, (x_coord, y_coord + 1)))
            case 'v':
                if y_coord == 1:
                    new_blizzards.add((direction, (x_coord, max_y - 1)))
                else:
                    new_blizzards.add((direction, (x_coord, y_coord - 1)))
            case '<':
                if x_coord == 1:
                    new_blizzards.add((direction, (max_x - 1, y_coord)))
                else:
                    new_blizzards.add((direction, (x_coord - 1, y_coord)))
            case '>':
                if x_coord == max_x - 1:
                    new_blizzards.add((direction, (1, y_coord)))
                else:
                    new_blizzards.add((direction, (x_coord + 1, y_coord)))
    return new_blizzards


start_1, end_1, blizzards_1, walls_1, nodes_1, max_x_1, max_y_1 = parse("2022/day_24/input_test.txt")
print(search(nodes_1, blizzards_1, start_1, end_1, max_x_1, max_y_1))
