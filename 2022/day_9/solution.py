"""
Find the number of positions that a rope tail
occupies given motions of the rope head
"""

from typing import TextIO
from re import findall


class Point:
    """Represents a point with an x and y coordinate"""

    def __init__(self, x_coord, y_coord):
        self.x_coord = x_coord
        self.y_coord = y_coord

    def move_straight(self, direction):
        """Move point 1 step up, down, left, or right"""
        match direction:
            case "U":
                self.y_coord += 1
            case "D":
                self.y_coord -= 1
            case "L":
                self.x_coord -= 1
            case "R":
                self.x_coord += 1

    def move_diagonal(self, direction):
        """Move point 1 step diagonally with a given direction"""
        match direction:
            case "up_right":
                self.x_coord += 1
                self.y_coord += 1
            case "up_left":
                self.x_coord -= 1
                self.y_coord += 1
            case "down_right":
                self.x_coord += 1
                self.y_coord -= 1
            case "down_left":
                self.x_coord -= 1
                self.y_coord -= 1


class Rope:
    """
    Represents a rope object with a head or a tail
    that occupy a point in space
    """

    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

    def distance(self):
        """Return the distance between the head and tail"""
        x_head, y_head = self.head.x_coord, self.head.y_coord
        x_tail, y_tail = self.tail.x_coord, self.tail.y_coord
        return (((x_tail - x_head) ** 2) + ((y_tail - y_head) ** 2)) ** 0.5

    def is_adjacent(self):
        """Returns whether or not the head and tail are adjacent"""
        distance = self.distance()
        return distance in (1, 2**0.5)


def parse(input_file: str) -> list[tuple[str, str]]:
    """
    Return a list of motions of a rope head from the given input file
    """
    in_file: TextIO = open(input_file, "r", encoding="utf-8")
    with open(input_file, encoding="utf-8") as in_file:
        input_data: str = in_file.read()
    split_lines: list[str] = input_data.split("\n")
    parsed_data: list[tuple[str, str]] = [
        findall(r"([LRDU]) (\d+)", line)[0] for line in split_lines
    ]
    return parsed_data


def num_of_tail_positions(input_file: str) -> int:
    """
    Find the number of positions the tail of a rope
    occupies with given motions for the head of a rope
    """
    motions: list[tuple[str, str]] = parse(input_file)
    location_head = Point(0, 0)
    location_tail = Point(0, 0)
    rope = Rope(location_head, location_tail)
    tail_positions: set[tuple[int, int]] = set([(0, 0)])
    for direction, steps in motions:
        for _ in range(int(steps)):
            rope.head.move_straight(direction)
            if rope.is_adjacent():
                continue
            if rope.distance() == 2:
                if rope.head.x_coord > rope.tail.x_coord:
                    rope.tail.move_straight("R")
                if rope.head.x_coord < rope.tail.x_coord:
                    rope.tail.move_straight("L")
                if rope.head.y_coord > rope.tail.y_coord:
                    rope.tail.move_straight("U")
                if rope.head.y_coord < rope.tail.y_coord:
                    rope.tail.move_straight("D")
                tail_positions.add((rope.tail.x_coord, rope.tail.y_coord))
            elif rope.distance() == 5**0.5:
                if (rope.head.x_coord > rope.tail.x_coord) and (
                    rope.head.y_coord > rope.tail.y_coord
                ):
                    rope.tail.move_diagonal("up_right")
                if (rope.head.x_coord > rope.tail.x_coord) and (
                    rope.head.y_coord < rope.tail.y_coord
                ):
                    rope.tail.move_diagonal("down_right")
                if (rope.head.x_coord < rope.tail.x_coord) and (
                    rope.head.y_coord < rope.tail.y_coord
                ):
                    rope.tail.move_diagonal("down_left")
                if (rope.head.x_coord < rope.tail.x_coord) and (
                    rope.head.y_coord > rope.tail.y_coord
                ):
                    rope.tail.move_diagonal("up_left")
                tail_positions.add((rope.tail.x_coord, rope.tail.y_coord))
    return len(tail_positions)
