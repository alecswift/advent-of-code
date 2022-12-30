from copy import deepcopy
from enum import Enum


class Directions(Enum):

    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4


def parse(input_file):
    in_file = open(input_file, "r", encoding="utf-8")
    with open(input_file, encoding="utf-8") as in_file:
        input_data = in_file.read()
    split_lines = input_data.split("\n")
    positions = []
    for y_coord, line in zip(range(len(split_lines) - 1, -1, -1), split_lines):
        for x_coord, space in enumerate(line):
            if space == "#":
                positions.append((x_coord, y_coord))
    return positions


class Positions:
    def __init__(self, positions):
        self.positions = positions
        self.adj_coords = None
        self.set_adj_coords()
        # maybe change to sets?

    def set_adj_coords(self):
        # 0: N, 1: NE, 2: E, 3: SE, 4: S, 5: SW, 6:W, 7: NW
        self.adj_coords = [
            [
                (x_coord, y_coord + 1),
                (x_coord + 1, y_coord + 1),
                (x_coord + 1, y_coord),
                (x_coord + 1, y_coord - 1),
                (x_coord, y_coord - 1),
                (x_coord - 1, y_coord - 1),
                (x_coord - 1, y_coord),
                (x_coord - 1, y_coord + 1),
            ]
            for x_coord, y_coord in self.positions
        ]

    def build_potential_dirs(self):
        # N, S, W, E
        potential_dirs = []
        for adj_coord in self.adj_coords:
            if set(adj_coord).intersection(set(self.positions)):
                # need to change order every round somehow
                directions = {
                    1: adj_coord[:2] + [adj_coord[-1]],
                    3: adj_coord[3:6],
                    4: adj_coord[5:],
                    2: adj_coord[1:4]
                }
                for direction, coords in directions.items():
                    if not set(coords).intersection(set(self.positions)):
                        potential_dirs.append(direction)
                        break
                else:
                    potential_dirs.append(0)
            else:
                potential_dirs.append(0)
        return potential_dirs
    
    def move_positions(self):
        potential_dirs = self.build_potential_dirs()
        pot_positions = []
        for position, direction in zip(self.positions, potential_dirs):
            x_coord, y_coord = position
            match direction:
                case 0:
                    pot_positions.append(position)
                case 1:
                    pot_positions.append((x_coord, y_coord + 1))
                case 2:
                    pot_positions.append((x_coord + 1, y_coord))
                case 3:
                    pot_positions.append((x_coord, y_coord - 1))
                case 4:
                    pot_positions.append((x_coord - 1, y_coord))
        new_positions = deepcopy(pot_positions)
        # filter elves that propose the same direction
        for index, pot_position in enumerate(pot_positions):
            cp_lst = list(pot_positions)
            # May be bugs here haven't test
            del cp_lst[index]
            if pot_position in cp_lst:
                new_positions[index] = self.positions[index]
        self.positions = new_positions
        return new_positions



grove = Positions(parse("2022/day_23/input_test.txt"))
print(sorted(grove.move_positions()))
print(sorted(parse('2022/day_23/input_test_2.txt')))
# 3 values different: (5, 3) should be (4,2) ane two others