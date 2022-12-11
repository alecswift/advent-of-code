"""
Finds the sections in pairs of elves that both overlap completely or partially
"""
import re
from typing import TextIO


def parse(input_file: str) -> list[tuple[str, str]]:
    """
    Returns parsed data from a given input file
    Parsed data is in the format of a list containing
    tuples that represent elves and contain strings
    that represent section ranges
    """
    in_file: TextIO = open(input_file, "r", encoding="utf-8")
    with open(input_file, encoding="utf-8") as in_file:
        input_data: str = in_file.read()
    parsed_data: list[tuple[str, str]] = re.findall(r"(\d+)-(\d+)", input_data)
    return parsed_data


def overlap(input_file: str) -> int:
    """
    Return the sum of sections that overlap completely in
    pairs of elves from a given input file
    """
    sections: list[tuple[str, str]] = parse(input_file)
    cp_sections: list[tuple[str, str]] = sections
    total: int = 0

    for _ in range(len(sections) // 2):
        elf_1: tuple[str, str]
        elf_2: tuple[str, str]
        elf_1, elf_2, *rest = cp_sections

        num_1: str
        num_2: str
        num_3: str
        num_4: str
        num_1, num_2 = elf_1
        num_3, num_4 = elf_2

        cp_sections = rest
        if set(range(int(num_1), int(num_2) + 1)).issubset(
            set(range(int(num_3), int(num_4) + 1))
        ):
            total += 1
        elif set(range(int(num_1), int(num_2) + 1)).issuperset(
            set(range(int(num_3), int(num_4) + 1))
        ):
            total += 1
    return total


def overlap_2(input_file: str) -> int:
    """
    Return the sum of sections that overlap partially in
    pairs of elves from a given input file
    """
    sections: list[tuple[str, str]] = parse(input_file)
    cp_sections: list[tuple[str, str]] = sections
    total: int = 0

    for _ in range(len(sections) // 2):
        elf_1: tuple[str, str]
        elf_2: tuple[str, str]
        elf_1, elf_2, *rest = cp_sections

        num_1: str
        num_2: str
        num_3: str
        num_4: str
        num_1, num_2 = elf_1
        num_3, num_4 = elf_2

        cp_sections = rest
        if set(range(int(num_1), int(num_2) + 1)).intersection(
            set(range(int(num_3), int(num_4) + 1))
        ):
            total += 1
    return total


print(overlap("2022/day_4/input.txt"))
print(overlap_2("2022/day_4/input.txt"))
