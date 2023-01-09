"""
Parses data from an input file and then finds the top three sums of the data
"""
import re
from typing import TextIO

def main():
    parsed_data = parse("2022/day_1/input.txt")
    first,  top_three = find_top_three(parsed_data)
    print(first)
    print(top_three)

def find_top_three(parsed_data: list[list[str]]) -> int:
    """
    Returns the top three sums of calories from a given
    input file that contains calories that elves are holding
    """
    elves: list[list[int]] = [list(map(int, cals)) for cals in parsed_data]
    sum_cals: list[int] = [sum(cals) for cals in elves]

    first: int = max(sum_cals)
    sum_cals.remove(first)
    second: int = max(sum_cals)
    sum_cals.remove(second)
    third: int = max(sum_cals)
    return first, first + second + third

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


if __name__ == "__main__":
    main()
