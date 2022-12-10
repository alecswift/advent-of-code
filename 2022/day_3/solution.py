"""
Finds the total priorities of common items
in two compartments of a list of rucksacks
"""
from typing import TextIO
def parse(input_file: str) -> list[tuple[set[str], set[str]]]:
    in_file: TextIO = open(input_file, 'r', encoding = 'utf-8')
    with open(input_file, encoding = 'utf-8') as in_file:
        input_data: str = in_file.read()
    parsed_data: list[tuple[set[str], set[str]]] = [
        (set(rucksack[:len(rucksack) // 2]), set(rucksack[len(rucksack) // 2:]))
        for rucksack in input_data.splitlines()
    ]
    return parsed_data

print(parse('2022/day_3/input.txt'))
