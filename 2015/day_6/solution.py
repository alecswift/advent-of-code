"""Puzzle explanation: https://adventofcode.com/2015/day/6"""

from re import findall, split
from itertools import product


def main():
    instructions, intervals = parse("day_6/input.txt")
    print(light_show(instructions, intervals))
    print(sum(lights_on_2.values()))


def parse(input_file):
    in_file = open(input_file, "r", encoding="utf-8")
    with open(input_file, encoding="utf-8") as in_file:
        input_data = in_file.read()
    split_lines = split(r"\n", input_data)

    instructions = []
    intervals = []
    for line in split_lines:
        interval = [int(num) for num in findall(r"\d+", line)]
        intervals.append(interval)
        if "on" in line:
            instruction = 1
        elif "off" in line:
            instruction = 0
        else:
            instruction = -1
        instructions.append(instruction)
    return instructions, intervals

# make this whole module a class
lights_on_2 = {}
lights_on = set()

def light_show(instructions, intervals):
    for index, interval in enumerate(intervals):
        instruction = instructions[index]
        x_1, y_1, x_2, y_2 = interval
        for x_coord, y_coord in product(range(x_1, x_2 + 1), range(y_1, y_2 + 1)):
            coord = complex(x_coord, y_coord)
            part_1(instruction, coord)
            part_2(instruction, coord)
    return len(lights_on)

def part_1(instruction, coord):
    if instruction == 1:
        if coord not in lights_on:
            lights_on.add(coord)
    elif instruction == 0:
        if coord in lights_on:
            lights_on.remove(coord)
    else:
        if coord in lights_on:
            lights_on.remove(coord)
        else:
            lights_on.add(coord)

def part_2(instruction, coord):
    if instruction == 1:
        lights_on_2[coord] = lights_on_2.setdefault(coord, 0) + 1
    elif instruction == 0:
        if lights_on_2.get(coord):
            lights_on_2[coord] -= 1
    else:
        lights_on_2[coord] = lights_on_2.setdefault(coord, 0) + 2


if __name__ == "__main__":
    main()
