
from itertools import pairwise
import re
from typing import TextIO

def parse(input_file: str) -> list[tuple[tuple[str, str]]]:
    in_file: TextIO = open(input_file, 'r', encoding = 'utf-8')
    with open(input_file, encoding = 'utf-8') as in_file:
        input_data: str = in_file.read()
    split_ranges: list[tuple[str, str]] = re.findall(r'(\d+)-(\d+)', input_data)
    parsed_data: list[tuple[tuple[str, str]]] = list(pairwise(split_ranges))
    return parsed_data

print(parse('2022/day_4/input.txt'))
