"""
Finds the total priorities of common items
in two compartments of a list of rucksacks
"""
from typing import TextIO
from string import ascii_letters


def parse(input_file: str) -> list[tuple[set[str], set[str]]]:
    """
    Return parsed data with the given input file. Parsed data is in the format
    of a list containing tuples which represent the rucksacks which contain
    two sets that represent the two compartments
    """
    in_file: TextIO = open(input_file, "r", encoding="utf-8")
    with open(input_file, encoding="utf-8") as in_file:
        input_data: str = in_file.read()
    parsed_data: list[tuple[set[str], set[str]]] = [
        (set(rucksack[: len(rucksack) // 2]), set(rucksack[len(rucksack) // 2 :]))
        for rucksack in input_data.splitlines()
    ]
    return parsed_data


def total_priority(input_file: str) -> int:
    """
    Returns the total priority of common items in compartments
    of rucksacks from a given input file
    """
    rucksacks: list[tuple[set[str], set[str]]] = parse(input_file)
    total: int = 0
    for comp_1, comp_2 in rucksacks:
        common_item: str = comp_1.intersection(comp_2).pop()
        total += ascii_letters.index(common_item) + 1
    return total


print(total_priority("2022/day_3/input.txt"))
