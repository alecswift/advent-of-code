"""
Find the sum of signal strength during the
20th, 60th, 100th, and 140th cycle of a CPU
"""

from typing import TextIO
from re import findall


class CPU:
    """
    Represents a CPU with a register and clock circuit
    that can execute instructions
    """

    def __init__(self, instructions):
        self.instructions = instructions
        self.register = 1
        self.cycle = 0
        self.states = {}

    def execute_instructions(self):
        """
        Modifies the register value, cycle, and states
        based on the arguments in the instructions
        """
        value = 0
        for cmd, arg in self.instructions:
            self.register += int(value)
            value = 0
            if cmd == "noop":
                self.cycle += 1
            if cmd == "addx":
                self.cycle += 1
                self.states[self.cycle] = self.register
                self.cycle += 1
                value = arg
            self.states[self.cycle] = self.register

    def sum_signal_strength(self):
        """
        Returns the sum of the states value at specified cycles
        multiplied by the cycle number
        """
        total = 0
        for num in range(20, 221, 40):
            total += self.states[num] * num
        return total


def parse(input_file: str) -> list[tuple[str, int | None]]:
    """
    Return a list of commands for execution
    of a CPU from a given input file
    """
    in_file: TextIO = open(input_file, "r", encoding="utf-8")
    with open(input_file, encoding="utf-8") as in_file:
        input_data: str = in_file.read()
    split_lines: list[str] = input_data.split("\n")
    parsed_data: list[tuple[str, int | None]] = [
        findall(r"(addx) ([-\d]+)", line)[0] if "addx" in line else (line, None)
        for line in split_lines
    ]
    return parsed_data
