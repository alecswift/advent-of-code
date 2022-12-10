"""
Parses data from an input file and then finds the top three sums of the data
"""
import re
from typing import TextIO

def parse(input_file: str) -> list[list[str]]:
    """
    Returns a list that contains lists of calories that elves are holding
    from a given input file
    """
    in_file: TextIO = open(input_file, "r", encoding="utf-8")
    with open(input_file, encoding="utf-8") as in_file:
        input_data: str = in_file.read()
    parsed_data: list[list[str]] = [
        re.split("\n", cals) for cals in re.split(r"\n\n", input_data.rstrip())
    ]
    return parsed_data


def top(input_file: str) -> int:
    """
    Returns the top sum of calories from a given
    input file that contains calories that elves are holding
    """
    parsed_data: list[list[str]] = parse(input_file)
    elves: list[list[int]] = [list(map(int, cals)) for cals in parsed_data]
    sum_cals: list[int] = [sum(cals) for cals in elves]

    first: int = max(sum_cals)
    return first


def top_three(input_file: str) -> int:
    """
    Returns the top three sums of calories from a given
    input file that contains calories that elves are holding
    """
    parsed_data: list[list[str]] = parse(input_file)
    elves: list[list[int]] = [list(map(int, cals)) for cals in parsed_data]
    sum_cals: list[int] = [sum(cals) for cals in elves]

    first: int = max(sum_cals)
    sum_cals.remove(first)
    second: int = max(sum_cals)
    sum_cals.remove(second)
    third: int = max(sum_cals)
    return first + second + third

print(top('2022/day_1/input.txt'))
print(top_three('2022/day_1/input.txt'))
