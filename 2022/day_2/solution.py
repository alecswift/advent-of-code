"""
Finds the total score for a rock, paper, scissor tournament given the input file
"""
import re
from typing import TextIO


def parse(input_file: str) -> list[tuple[str, str]]:
    """
    Returns a list of tuples of each rock, paper, scissors round
    from a given input file
    """
    in_file: TextIO = open(input_file, "r", encoding="utf-8")
    with open(input_file, encoding="utf-8") as in_file:
        input_data: str = in_file.read()
    parsed_data: list[tuple[str, str]] = re.findall(r"([A-C]) ([X-Z])", input_data)
    return parsed_data
