# be thoughtful of coordinates y = row number in array,
# x = column number, also moving down is moving up
# could use a dictionary of rock types rather or match case statements

from collections import deque
from itertools import cycle

cave_grid = [[0] * 7 for _ in range(10000)]
cave_grid[0] = [1, 1, 1, 1, 1, 1, 1]

def parse(input_file):
    """Return the data of the given input file"""
    in_file = open(input_file, 'r', encoding = 'utf-8')
    with open(input_file, encoding = 'utf-8') as in_file:
        input_data = in_file.read()
    lst_data = list(input_data) * 2000
    return deque(lst_data)

def move(rock_object, direction):
    """Move the rock object down, left, or right"""
    match direction:
        case 'D':
            rock_object.position = [[x, y - 1] for x, y in rock_object.position]
        case '<':
            rock_object.position = [[x - 1, y] for x, y in rock_object.position]
        case '>':
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
        if 1 in cave_grid[y_coord - 1][x_coord: x_coord + 4]:
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
        return self.position[3][1]

    def lowest_x(self):
        return self.position[0][0]

    def highest_x(self):
        return  self.position[1][0]

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
        return self.position[3][1]

    def lowest_x(self):
        return self.position[1][0]

    def highest_x(self):
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
        if 1 in cave_grid[y_coord - 1][x_coord: x_coord + 3]:
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
        return self.position[4][1]

    def lowest_x(self):
        return self.position[0][0]

    def highest_x(self):
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
        return self.position[3][1]

    def lowest_x(self):
        return self.position[0][0]

    def highest_x(self):
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
        # could test line of code see if joining and truth value is faster
        if 1 in cave_grid[y_coord - 1][x_coord: x_coord + 2]:
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
        return self.position[2][1]

    def lowest_x(self):
        return self.position[0][0]

    def highest_x(self):
        return self.position[1][0]

def gust(direction, rock_object):
    if direction == '<':
        if rock_object.lowest_x() != 0:
            if not rock_object.scan_left():
                move(rock_object, '<')
    else:
        if rock_object.highest_x() != 6:
            if not rock_object.scan_right():
                move(rock_object, '>')

def falling_rocks(input_file):
    direction_queue = parse(input_file)
    rocks = [HorLineRock, PlusRock, LRock, VertLineRock, SquareRock]
    for num_rock, rock in zip(range(2022), cycle(rocks)):
        if not num_rock:
            row = 0
        rock = rock(row)
        for _ in range(3): # no need to scan first 3 movements
            gust(direction_queue[0], rock)
            direction_queue.popleft()
            move(rock, 'D')
        gust(direction_queue[0], rock)
        direction_queue.popleft()
        while not rock.scan_below():
            move(rock, 'D')
            gust(direction_queue[0], rock)
            direction_queue.popleft()
        # make different function
        for x_coord, y_coord in rock.position:
            cave_grid[y_coord][x_coord] = 1
        row = rock.top()
    return row + 1


print(falling_rocks('/home/alec/Desktop/code/advent_of_code/2022/day_17/input_test.txt'))
# display test
rock_1 = HorLineRock(0)
# print(rock.highest_x())
'''array = [["."] * 7 for _ in range(8)]
for num in range(7):
    array[0][num] = "#"
rocks = [HorLineRock(0), SquareRock(0), PlusRock(0), LRock(0), VertLineRock(0)]
for rock in rocks:
    move(rock, 'R')
    for x, y in rock.position:
        array[y][x] = "#"
    print('\n'.join([''.join(line) for line in array[::-1]]))
    array = [["."] * 7 for _ in range(8)]
    for num in range(7):
        array[0][num] = "#"'''
