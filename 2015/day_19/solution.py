"""Puzzle explanation: https://adventofcode.com/2015/day/19"""

from re import findall
from typing import TextIO

def main():
    replacements, molecule = parse("2015/day_19/input.txt")
    num_possibilities = find_molecules(molecule, replacements)
    print(num_possibilities)
    print(part2(molecule))

def parse(input_file: str) -> tuple[list[tuple[str, str]], str]:
    in_file: TextIO
    with open(input_file, "r", encoding="utf-8") as in_file:
        input_data: str = in_file.read()
    raw_replacements: str
    molecule: str
    raw_replacements, molecule = input_data.split("\n\n")
    replacements: list[tuple[str, str]] = []
    for line in raw_replacements.split("\n"):
        replacements.append(*findall(r'(\w+) => (\w+)', line))
    return replacements, molecule

def find_molecules(molecule: str, replacements: list[tuple[str, str]]) -> int:
    length: int = len(molecule)
    possibilities: set[str] = set()
    for from_str, to_str in replacements:
        step: int = len(from_str)
        for idx in range(step, length + 1):
            scan: str = molecule[idx - step: idx]
            if scan == from_str:
                possibilities.add(f"{molecule[:idx - step]}{to_str}{molecule[idx:]}")
    return len(possibilities)

def part2(molecule: str) -> int:
    count_elements: int = sum(1 for char in molecule if char.isupper())
    count_y: int = len(findall(r"Y", molecule))
    count_ar_rn: int = len(findall(r"Rn|Ar", molecule))
    return count_elements - count_ar_rn - (count_y * 2) - 1

if __name__ == "__main__":
    main()
