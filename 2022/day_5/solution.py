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
                parsed_diagram[count].insert(0, row[index])
            index += 4
            count += 1
    return parsed_diagram, parsed_proc

def rearrange(input_file: str) -> str:
    """
    Return the rearranged diagram with the given input_file that
    includes the original diagram and the procedures
    """
    diagram: list[list[str]]
    procedure: list[tuple[str, str, str]]
    diagram, procedure = parse(input_file)
    for line in procedure:
        num_crates: str
        stack_from: str
        stack_to: str
        num_crates, stack_from, stack_to = line
        move: list[str] = diagram[int(stack_from) - 1][:-int(num_crates) - 1:-1]
        diagram[int(stack_from) - 1] = diagram[int(stack_from) - 1][0:-int(num_crates)]
        diagram[int(stack_to) - 1] += move
    return "".join([column[-1] for column in diagram])

print(rearrange("/home/alec/Desktop/code/advent_of_code/2022/day_5/input.txt"))
