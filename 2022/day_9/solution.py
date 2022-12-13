"""
Find the number of positions that a rope tail
occupies given motions of the rope head
"""

from typing import TextIO
from re import findall


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

print(parse("2022/day_9/input.txt"))