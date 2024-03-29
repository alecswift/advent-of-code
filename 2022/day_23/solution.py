"""
An expanding matrix filled with empty spaces and elves that
have movement patterns that cycle in rounds. Finds the number
of empty spaces in the matrix after 10 rounds and the number
of rounds it takes for the elves to stop moving
"""

from collections import OrderedDict
from copy import deepcopy

def parse(input_file):
    """
    returns the initial positions of elves from the given input file
    """
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
    """
    Represents the positions of elves and their adjacent coordinates
    """

    def __init__(self, positions):
        self.positions = positions
        self.adj_coords = None

    def set_adj_coords(self):
        """Sets list of adjacent coordinates"""
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

    def build_potential_dirs(self, directions=[1, 3, 4, 2]):
        """
        Returns the potential direction of movement for each position
        based on the adjacency coordinates and a list of directions
        """
        # directions start as N, S, W, E
        self.set_adj_coords()
        potential_dirs = []
        set_positions = set(self.positions)
        for adj_coord in self.adj_coords:
            if set(adj_coord).intersection(set_positions):
                # need to change order every round somehow
                directions_dict = OrderedDict()
                for direction in directions:
                    if direction == 1:
                        directions_dict[1] = adj_coord[:2] + [adj_coord[-1]]
                    if direction == 2:
                        directions_dict[2] = adj_coord[1:4]
                    if direction == 3:
                        directions_dict[3] = adj_coord[3:6]
                    if direction == 4:
                        directions_dict[4] = adj_coord[5:]
                for direction, coords in directions_dict.items():
                    if not set(coords).intersection(set_positions):
                        potential_dirs.append(direction)
                        break
                else:
                    potential_dirs.append(0)
            else:
                potential_dirs.append(0)
        first = directions.pop(0)
        directions.append(first)
        return potential_dirs

    def move_positions(self):
        """Mutates the positions attribute based on the potential directions"""
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
            del cp_lst[index]
            if pot_position in cp_lst:
                new_positions[index] = self.positions[index]
        if self.positions == new_positions:
            return 0
        self.positions = new_positions
        return new_positions


def find_empty_spaces(positions):
    """Finds the number of empty spaces in the matrix"""
    max_x = max([x_coord for x_coord, _ in positions])
    max_y = max([y_coord for _, y_coord in positions])
    min_x = min([x_coord for x_coord, _ in positions])
    min_y = min([y_coord for _, y_coord in positions])
    num_of_spaces = (max_x - min_x + 1) * (max_y - min_y + 1)
    return num_of_spaces - len(positions)


def rounds(positions_object):
    """
    Cycles through rounds of movement given a positions object.
    Prints the number of empty spaces and returns the number of
    rounds it takes for movement to stop
    """
    count = 0
    movement = 1
    while movement:
        if count == 10:
            print(find_empty_spaces(positions_object.positions))
        movement = positions_object.move_positions()
        positions_object.set_adj_coords()
        count += 1
    return count


grove = Positions(parse("2022/day_23/input.txt"))
print(rounds(grove))
