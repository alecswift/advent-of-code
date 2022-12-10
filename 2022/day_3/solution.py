"""
Finds the total priorities of common items
in two compartments of a list of rucksacks
"""
from typing import TextIO
from string import ascii_letters


def parse(input_file: str) -> list[str]:
    """
    Return parsed data with the given input file. Parsed data is in the format
    of a list containing strings which represent the rucksacks
    """
    in_file: TextIO = open(input_file, "r", encoding="utf-8")
    with open(input_file, encoding="utf-8") as in_file:
        input_data: str = in_file.read()
    parsed_data: list[str] = input_data.splitlines()
    return parsed_data


def total_priority(input_file: str) -> int:
    """
    Returns the total priority of common items in compartments
    of rucksacks from a given input file
    """
    parsed_data: list[str] = parse(input_file)
    rucksacks: list[tuple[set[str], set[str]]] = [
        (set(rucksack[: len(rucksack) // 2]), set(rucksack[len(rucksack) // 2 :]))
        for rucksack in parsed_data
    ]
    # a list containing tuples which represent the rucksacks which contain
    # two sets that represent the two compartments
    total: int = 0
    for comp_1, comp_2 in rucksacks:
        common_item: str = comp_1.intersection(comp_2).pop()
        total += ascii_letters.index(common_item) + 1
    return total


def total_priority_2(input_file: str) -> int:
    """
    Returns the total priority of common items in rucksacks
    of groups of three elves from a given input file
    """
    parsed_data: list[str] = parse(input_file)
    cp_parsed_data: list[str] = parsed_data
    total: int = 0
    for _ in range(len(list(parsed_data)) // 3):
        elf_1, elf_2, elf_3, *rest = cp_parsed_data
        common_item_set: set[str] = set(elf_1).intersection(
            set(elf_2).intersection(set(elf_3))
        )
        common_item: str = common_item_set.pop()
        total += ascii_letters.index(common_item) + 1
        cp_parsed_data = rest
    return total

print(total_priority("2022/day_3/input.txt"))
print(total_priority_2("2022/day_3/input.txt"))
