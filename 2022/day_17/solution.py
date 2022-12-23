"""
Find the highest point of a rock tower after simulating
the falling of 2022 rocks with different shapes and gusts
of wind that move the rock left or right
"""

from array import array
from itertools import cycle

cave_grid = [array('I', [0,0,0,0,0,0,0]) for _ in range(100000)]
cave_grid[0] = array('I', [1, 1, 1, 1, 1, 1, 1])

def parse(input_file):
    """Return the data of the given input file"""
    in_file = open(input_file, "r", encoding="utf-8")
    with open(input_file, encoding="utf-8") as in_file:
        input_data = in_file.read()

    lst_data = array('I', [0 if direction == "<" else 1 for direction in input_data])
    return lst_data, len(input_data)


def move(rock_object, direction):
    """Move the rock object down, left, or right"""
    match direction:
        case "D":
            rock_object.position = [[x, y - 1] for x, y in rock_object.position]
        case 0:
            rock_object.position = [[x - 1, y] for x, y in rock_object.position]
        case 1:
            rock_object.position = [[x + 1, y] for x, y in rock_object.position]


class HorLineRock:
    """
    Represents a horizontal line with x and y coordinates
    that can move down, left, and right
    """

    def __init__(self, row):
        # row is the highest rock, points initialized three rows above
        # list is ordered down_most, rest
        self.position = [[2, row + 4], [5, row + 4], [3, row + 4], [4, row + 4]]

    def scan_below(self):
        """
        Scan the cave below the object to see if there are any objects
        """
        left_point, *_ = self.position
        x_coord, y_coord = left_point
        if 1 in cave_grid[y_coord - 1][x_coord : x_coord + 4]:
                return True
        return False

    def scan_left(self):
        """
        Scan the cave left of the object to see if there are any objects
        """
        left_point, *_ = self.position
        x_coord, y_coord = left_point
        if cave_grid[y_coord][x_coord - 1]:
            return True
        return False

    def scan_right(self):
        """
        Scan the cave left of the object to see if there are any objects
        """
        right_point = self.position[1]
        x_coord, y_coord = right_point
        if cave_grid[y_coord][x_coord + 1]:
            return True
        return False

    def top(self):
        """Highest y coordinate of rock"""
        return self.position[3][1]

    def lowest_x(self):
        """Lowest x coordinate of rock"""
        return self.position[0][0]

    def highest_x(self):
        """Highest x coordinate of rock"""
        return self.position[1][0]


class PlusRock:
    """
    Represents a plus sign with x and y coordinates
    that can move down, left, and right
    """

    def __init__(self, row):
        self.position = [
            [3, row + 4],
            [2, row + 5],
            [3, row + 5],
            [3, row + 6],
            [4, row + 5],
        ]

    def scan_below(self):
        """
        Scan the cave below the object to see if there are any objects
        """
        points = [self.position[0], self.position[1], self.position[4]]
        if 1 in [cave_grid[y_coord - 1][x_coord] for x_coord, y_coord in points]:
                return True
        return False

    def scan_left(self):
        """
        Scan the cave left of the object to see if there are any objects
        """
        points = [self.position[0], self.position[1], self.position[3]]
        if 1 in [cave_grid[y_coord][x_coord - 1] for x_coord, y_coord in points]:
                return True
        return False

    def scan_right(self):
        """
        Scan the cave left of the object to see if there are any objects
        """
        points = [self.position[0], self.position[3], self.position[4]]
        if 1 in [cave_grid[y_coord][x_coord + 1] for x_coord, y_coord in points]:
                return True
        return False

    def top(self):
        """Highest y coordinate of rock"""
        return self.position[3][1]

    def lowest_x(self):
        """Lowest x coordinate of rock"""
        return self.position[1][0]

    def highest_x(self):
        """Highest x coordinate of rock"""
        return self.position[4][0]


class LRock:
    """
    Represents a L shape with x and y coordinates
    that can move down, left, and right
    """

    def __init__(self, row):
        self.position = [
            [2, row + 4],
            [3, row + 4],
            [4, row + 4],
            [4, row + 5],
            [4, row + 6],
        ]

    def scan_below(self):
        """
        Scan the cave below the object to see if there are any objects
        """
        left_point, *_ = self.position
        x_coord, y_coord = left_point
        # could test line of code see if joining and truth value is faster
        if 1 in cave_grid[y_coord - 1][x_coord : x_coord + 3]:
                return True
        return False

    def scan_left(self):
        """
        Scan the cave left of the object to see if there are any objects
        """
        points = [self.position[0], self.position[3], self.position[4]]
        if 1 in [cave_grid[y_coord][x_coord - 1] for x_coord, y_coord in points]:
                return True
        return False

    def scan_right(self):
        """
        Scan the cave left of the object to see if there are any objects
        """
        right_point = self.position[2]
        x_coord, y_coord = right_point
        if 1 in [cave_grid[y_coord + num][x_coord + 1] for num in range(3)]:
                return True
        return False

    def top(self):
        """Highest y coordinate of rock"""
        return self.position[4][1]

    def lowest_x(self):
        """Lowest x coordinate of rock"""
        return self.position[0][0]

    def highest_x(self):
        """Highest x coordinate of rock"""
        return self.position[4][0]


class VertLineRock:
    """
    Represents a vertical line with x and y coordinates
    that can move down, left, and right
    """

    def __init__(self, row):
        self.position = [[2, row + 4], [2, row + 5], [2, row + 6], [2, row + 7]]

    def scan_below(self):
        """
        Scan the cave below the object to see if there are any objects
        """
        down_most, *_ = self.position
        x_coord, y_coord = down_most
        if cave_grid[y_coord - 1][x_coord]:
            return True
        return False

    def scan_left(self):
        """
        Scan the cave left of the object to see if there are any objects
        """
        left_point, *_ = self.position
        x_coord, y_coord = left_point
        if 1 in [cave_grid[y_coord + num][x_coord - 1] for num in range(4)]:
                return True
        return False

    def scan_right(self):
        """
        Scan the cave left of the object to see if there are any objects
        """
        right_point, *_ = self.position
        x_coord, y_coord = right_point
        if 1 in [cave_grid[y_coord + num][x_coord + 1] for num in range(4)]:
                return True
        return False

    def top(self):
        """Highest y coordinate of rock"""
        return self.position[3][1]

    def lowest_x(self):
        """Lowest x coordinate of rock"""
        return self.position[0][0]

    def highest_x(self):
        """Highest x coordinate of rock"""
        return self.position[0][0]


class SquareRock:
    """
    Represents a 2x2 square with x and y coordinates
    that can move down, left, and right
    """

    def __init__(self, row):
        self.position = [[2, row + 4], [3, row + 4], [2, row + 5], [3, row + 5]]

    def scan_below(self):
        """
        Scan the cave below the object to see if there are any objects
        """
        left_point, *_ = self.position
        x_coord, y_coord = left_point
        if 1 in cave_grid[y_coord - 1][x_coord : x_coord + 2]:
                return True
        return False

    def scan_left(self):
        """
        Scan the cave left of the object to see if there are any objects
        """
        left_point, *_ = self.position
        x_coord, y_coord = left_point
        if 1 in [cave_grid[y_coord + num][x_coord - 1] for num in range(2)]:
                return True
        return False

    def scan_right(self):
        """
        Scan the cave left of the object to see if there are any objects
        """
        right_point = self.position[1]
        x_coord, y_coord = right_point
        if 1 in [cave_grid[y_coord + num][x_coord + 1] for num in range(2)]:
                return True
        return False

    def top(self):
        """Highest y coordinate of rock"""
        return self.position[2][1]

    def lowest_x(self):
        """Lowest x coordinate of rock"""
        return self.position[0][0]

    def highest_x(self):
        """Highest x coordinate of rock"""
        return self.position[1][0]


def gust(direction, rock_object):
    """
    Move the rock in the given direction if the space is not blocked
    """
    if direction == 0:
        if rock_object.lowest_x() != 0:
            if not rock_object.scan_left():
                move(rock_object, 0)
    else:
        if rock_object.highest_x() != 6:
            if not rock_object.scan_right():
                move(rock_object, 1)


def falling_rocks(input_file, num_of_rocks):
    """
    Return the height of the rock tower after simulating 2022 rocks falling
    """
    cache = {}
    directions, len_input_data = parse(input_file)
    rocks = [HorLineRock, PlusRock, LRock, VertLineRock, SquareRock]
    for num_rock, rock in zip(range(num_of_rocks), cycle(rocks)):
        if not num_rock:
            top_row = 0
            saved_index = 0
                # return cache[state], "y"
        if num_rock == 2022:
            print(top_row)
        rock = rock(top_row)
        gust(directions[saved_index], rock)
        if saved_index == len_input_data - 1:
            saved_index = 0
        else:
            saved_index += 1
        while not rock.scan_below():
            move(rock, 'D')
            gust(directions[saved_index], rock)
            if saved_index == len_input_data - 1:
                saved_index = 0
            else:
                saved_index += 1
        for x_coord, y_coord in rock.position:
            cave_grid[y_coord][x_coord] = 1
        if top_row < rock.top():
            top_row = rock.top()
        if top_row >= 20:
            state = (
                saved_index % len_input_data,
                num_rock % 5,
                tuple(tuple(el) for el in cave_grid[top_row - 20: top_row + 1])
            )
            if state not in cache:
                cache[state] = top_row, num_rock
            else:
                top_row_1, num_rock_1 = cache[state]
                return top_row_1, num_rock_1, top_row, num_rock
    return top_row

def calculate_1_trillion_rocks(input_file, num_rocks):
    top_row_1, num_rock_1, top_row, num_rock = falling_rocks(input_file, num_rocks)
    num_of_cycles, remaining_rocks = divmod((1000000000000 - num_rock_1), (num_rock - num_rock_1))
    height_for_cycles = num_of_cycles * (top_row - top_row_1)
    global cave_grid
    cave_grid = [array('I', [0,0,0,0,0,0,0]) for _ in range(100000)]
    cave_grid[0] = array('I', [1, 1, 1, 1, 1, 1, 1])
    remaining_height = falling_rocks(input_file, num_rock_1 + remaining_rocks) - top_row_1
    return top_row_1 + height_for_cycles + remaining_height


print(
    (
    calculate_1_trillion_rocks("2022/day_17/input.txt", 6000)
    )
)