"""Puzzle explanation: https://adventofcode.com/2015/day/23"""

from re import findall
from typing import Callable, TextIO

def main():
    jump: Callable = lambda idx, offset: idx + offset
    instructions: dict[str, Callable] = {
        "hlf": lambda reg: reg // 2,
        "tpl": lambda reg: reg * 3,
        "inc": lambda reg: reg + 1,
        "jmp": jump,
        "jio": jump,
        "jie": jump,
    }
    code = parse("2015/day_23/input.txt")
    part1 = execute(code, instructions)
    print(part1)
    part2 = execute(code, instructions, False)
    print(part2)

def parse(input_file: str) -> list[list[str]]:
    in_file: TextIO
    with open(input_file, encoding="utf-8") as in_file:
        input_data: str = in_file.read()
    split_lines: list[str] = input_data.split("\n")[:-1]
    code = [findall(r"[a-z0-9+-]+", line) for line in split_lines]
    return code

code: list[list[str]]
instructions: dict[str, str]
part1: bool

def execute(code, instructions, part1=True) -> int:

    if part1:
        registers: dict[str,int] = {'a': 0 , 'b': 0}
    else:
        registers = {'a': 1 , 'b': 0}

    pos: int = 0
    while pos < len(code):
        instruction, *operands = code[pos]
        reg = operands[0]
        operation = instructions[instruction]
        if instruction == "jmp":
            offset = int(reg)
            pos = operation(pos, offset)
        elif instruction == "jio":
            if registers[reg] == 1:
                offset = int(operands[1])
                pos = operation(pos, offset)
            else:
                pos += 1
        elif instruction == "jie":
            if registers[reg] % 2 == 0:
                offset = int(operands[1])
                pos = operation(pos, offset)
            else:
                pos += 1
        else:
            reg_value = registers[reg]
            registers[reg] = operation(reg_value)
            pos += 1
    return registers['b']

if __name__ == "__main__":
    main()
