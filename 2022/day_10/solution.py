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
        # state of register during each cycle
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

class CRT:
    """
    Represents a CRT screen that draws pixels based on instructions
    """

    def __init__(self):
        self.screen = [['.' for _ in range(40)] for _ in range(6)]

    def draw_pixels(self, cpu):
        """
        Returns a modified screen based on a cpu's execution cycles
        """
        states = cpu.states
        for cycle, register in states.items():
            row = cycle // 40
            row_num = (cycle -1) % 40
            if register == -1:
                sprite_position = (0, 1)
            elif register == -1:
                sprite_position = (0, 2)
            else:
                sprite_position = (register - 1, register + 2)
            start, end = sprite_position
            # sprite = self.screen[row][start: end]
            if row_num in range(start, end):
                self.screen[row][row_num] = '#'
        return self.screen

    def print_screen(self):
        """Prints the screen in human readable form"""
        str_screen = ''
        for row in self.screen:
            str_row = ''.join(row)
            str_screen = f'{str_screen}{str_row}\n'
        print(str_screen)



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


cpu_1 = CPU(parse("2022/day_10/input.txt"))
cpu_1.execute_instructions()
print(cpu_1.sum_signal_strength())
crt = CRT()
crt.draw_pixels(cpu_1)
crt.print_screen()
