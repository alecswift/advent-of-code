"""Puzzle explanation: https://adventofcode.com/2016/day/8"""

from __future__ import annotations
from re import findall
from typing import TextIO


def main():
    instructions = parse("2016/day_08/input.txt")
    screen = Screen(6, 50)
    screen.execute(instructions)
    print(f"{screen.count_lit_pixels()} pixels are lit after the instructions\n")
    print(str(screen))


def parse(input_file: str) -> list[list[str]]:
    in_file: TextIO
    instructions = []
    with open(input_file, encoding="utf-8") as in_file:
        for line in in_file:
            instruction = []
            if "rotate column" in line:
                instruction.append("rotate_column")
            elif "row" in line:
                instruction.append("rotate_row")
            else:
                instruction.append("rect")
            instruction.extend(findall(r"\d+", line))
            instructions.append(instruction)
    return instructions


class Screen:
    def __init__(self, rows: int, columns: int):
        self._rows = rows
        self._columns = columns
        self._grid: list[list[str]] = [["."] * columns for _ in range(rows)]

    def rotate_row(self, row: int, rot: int) -> None:
        for _ in range(rot):
            start = self._grid[row].pop()
            self._grid[row].insert(0, start)

    def rotate_column(self, col: int, rot: int) -> None:
        for _ in range(rot):
            last_val = self._grid[-1][col]
            for row in range(self._rows - 2, -1, -1):
                curr_val = self._grid[row][col]
                self._grid[row + 1][col] = curr_val
            self._grid[0][col] = last_val

    def rect(self, length: int, width: int) -> None:
        for row in range(width):
            for col in range(length):
                self._grid[row][col] = "#"

    def execute(self, instructions: list[list[str]]):
        for line in instructions:
            instruction, *operands = line
            usable = map(int, operands)
            getattr(self, instruction)(*usable)

    def count_lit_pixels(self) -> int:
        return sum(1 for row in self._grid for pix in row if pix == "#")

    def __str__(self) -> str:
        return "\n".join(["".join(row) for row in self._grid])


if __name__ == "__main__":
    main()
