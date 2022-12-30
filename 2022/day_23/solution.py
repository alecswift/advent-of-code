class Elf:
    
    def __init__(self, position):
        self.position = position
        self.adj_coords = None
        self.set_adj_coords()
        self.adj_bitmask = None

    def set_adj_coords(self):
        x_coord, y_coord = self.position
        # N, NE, E, SE, S, SW, W, NW
        self.adj_coords = [
            (x_coord, y_coord + 1),
            (x_coord + 1, y_coord + 1),
            (x_coord + 1, y_coord),
            (x_coord + 1, y_coord - 1),
            (x_coord, y_coord - 1),
            (x_coord - 1, y_coord - 1),
            (x_coord - 1, y_coord),
            (x_coord - 1, y_coord + 1),
        ]


def parse(input_file):
    in_file = open(input_file, "r", encoding="utf-8")
    with open(input_file, encoding="utf-8") as in_file:
        input_data = in_file.read()
    split_lines = input_data.split("\n")
    elf_positions = []
    for y_coord, line in zip(range(len(split_lines) - 1, -1, -1), split_lines):
        for x_coord, space in enumerate(line):
            if space == "#":
                elf_positions.append((x_coord, y_coord))
    return elf_positions


print(parse("2022/day_23/input_test.txt"))
