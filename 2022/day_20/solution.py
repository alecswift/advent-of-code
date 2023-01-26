"""
Sort a circular list of coordinates (integers) by moving each coordinate
forward or backwards based on the value of that coordinate. After sorting
find the sum of the 1000th, 2000th, and 3000th element after 0 in the
circular list
"""

from collections import deque
from itertools import cycle


def parse(input_file):
    """
    From the given input file return a list of tuples with the coordinate
    value and original index and the same list with each coordinate multiplied
    by 811589153
    """
    with open(input_file, encoding="utf-8") as in_file:
        input_data = in_file.read()
    split_lines = input_data.split("\n")
    coords = [(int(line), index) for index, line in enumerate(split_lines)]
    multiplied_coords = [(value * 811589153, index) for value, index in coords]
    return coords, multiplied_coords


def mix(coords, original_coords):
    """
    Return a sorted a circular list of coordinates (integers) by moving
    each coordinate forward or backwards based on the value of that
    coordinate.
    """
    queue_coords = deque(coords)
    for coord in original_coords:
        index = queue_coords.index(coord)
        queue_coords.remove(coord)
        queue_coords.rotate(-coord[0])
        queue_coords.insert(index, coord)
    return list(queue_coords)


def cycles(sorted_coords):
    """
    Find the sum of the 1000th, 2000th, and 3000th coordinate from the
    given sorted circular list
    """
    sorted_coords = [coord[0] for coord in sorted_coords]
    count = None
    numbers = []
    for coord in cycle(sorted_coords):
        if len(numbers) == 3:
            break
        if count is not None:
            count += 1
            if (count != 0) and (count % 1000 == 0):
                numbers.append(coord)
        elif coord == 0:
            count = 0
    return sum(numbers)

def solutions(input_file):
    """
    Find the sums for the the original list mixed once
    and for the multiplied list mixed 10 times
    """
    coords, multiplied_coords = parse(input_file)
    original_coords = list(coords)
    og_multiplied_coords = list(multiplied_coords)
    mixed_coords = mix(coords, original_coords)
    part_1 = cycles(mixed_coords)
    for _ in range(10):
        multiplied_coords = mix(multiplied_coords, og_multiplied_coords)
    part_2 = cycles(multiplied_coords)
    return part_1, part_2

print(solutions('2022/day_20/input.txt'))
