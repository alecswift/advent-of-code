"""Puzzle explanation: https://adventofcode.com/2015/day/23"""

from re import findall
from typing import Callable, TextIO

def main():
    instructions: dict[str, Callable] = {
        "hlf": lambda reg: reg // 2,
        "tpl": lambda reg: reg * 3,
        "inc": lambda reg: reg + 1,
        "jmp": lambda idx, offset: idx + offset,
        "jie": 1,
        "jio": 1,
    }
    print(parse("2015/day_23/input.txt"))

def parse(input_file: str):
    in_file: TextIO
    with open(input_file, encoding="utf-8") as in_file:
        input_data: str = in_file.read()
    lines = findall(r"(\w+) (\w+)", input_data)
    print(lines)



if __name__ == "__main__":
    main()
