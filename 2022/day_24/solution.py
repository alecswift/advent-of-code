def parse(input_file):
    in_file = open(input_file, "r", encoding="utf-8")
    with open(input_file, encoding="utf-8") as in_file:
        input_data = in_file.read()
    split_lines = input_data.split("\n")
    blizzards = set()
    walls = set()
    nodes = {}
    max_y = len(split_lines) - 1
    start = (1, max_y)
    end = (len(split_lines[0]) - 2, 0)
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
    return start, end, blizzards, walls, nodes
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


print(parse("2022/day_24/input_test.txt"))

