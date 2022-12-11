import re
from typing import TextIO


def parse(input_file: str) -> tuple[list[list[str]], list[tuple[str, str, str]]]:
    """Return the input data from a given input file
    the input data is a tuple containing two lists:
    The first list represents the diagram.
    The second list represents the procedure"""
    in_file: TextIO = open(input_file, "r", encoding="utf-8")
    with open(input_file, encoding="utf-8") as in_file:
        input_data: str = in_file.read()
    split_data: list[str] = input_data.split("\n\n")
    diagram: str
    procedure: str
    diagram, procedure = split_data
    parsed_proc: list[tuple[str, str, str]] = re.findall(
        r"(\d+) from (\d+) to (\d+)", procedure
    )
    parsed_diagram: list[list[str]] = [[] for _ in range(9)]
    for row in diagram.split("\n"):
        index: int = 1
        count: int = 0
        while index < len(row):
            if row[index].isalpha():
                parsed_diagram[count].append(row[index])
            index += 4
            count += 1
    return parsed_diagram, parsed_proc


print(parse("/home/alec/Desktop/code/advent_of_code/2022/day_5/input.txt"))
