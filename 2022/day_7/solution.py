"""
Find the total size of all directories that have a size 
of less than 100,000 from file system browsing data
"""

from typing import TextIO


def parse(input_file: str) -> list[str]:
    in_file: TextIO = open(input_file, "r", encoding="utf-8")
    with open(input_file, encoding="utf-8") as in_file:
        input_data: str = in_file.read()
    return input_data.split("\n")
