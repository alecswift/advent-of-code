"""
Find the sum of signal strength during the
20th, 60th, 100th, and 140th cycle of a CPU
"""

from typing import TextIO
from re import findall


def parse(input_file: str) -> list[tuple[str, int | None]]:
    """
    Return a list of commands for execution
    of a CPU from a given input file
    """
    in_file: TextIO = open(input_file, "r", encoding="utf-8")
    with open(input_file, encoding="utf-8") as in_file:
        input_data: str = in_file.read()
    split_lines: list[str] = input_data.split("\n")
    parsed_data: list[tuple[str, int | None]] = [
        findall(r"(addx) ([-\d]+)", line)[0] if "addx" in line else (line, None)
        for line in split_lines
    ]
    return parsed_data


print(parse("/home/alec/Desktop/code/advent_of_code/2022/day_10/input.txt"))
