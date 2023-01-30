# between 573 and 694 noninclusive
from re import findall
from typing import TextIO

def main():
    replacements, molecule = parse("2015/day_19/input.txt")
    print(find_molecules(molecule, replacements))
    

def parse(input_file: str):
    in_file: TextIO
    with open(input_file, "r", encoding="utf-8") as in_file:
        input_data = in_file.read()
    raw_replacements, molecule = input_data.split("\n\n")
    replacements = []
    for line in raw_replacements.split("\n"):
        replacements.append(*findall(r'(\w+) => (\w+)', line))
    return replacements, molecule

def find_molecules(molecule, replacements):
    length = len(molecule)
    possibilities = set()
    for from_str, to_str in replacements:
        step = len(from_str)
        for idx in range(step, length + 1):
            scan = molecule[idx - step: idx]
            if scan == from_str:
                possibilities.add(f"{molecule[:idx - step]}{to_str}{molecule[idx:]}")
    print(possibilities)
    return len(possibilities)




if __name__ == "__main__":
    main()