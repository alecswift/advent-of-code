from collections import deque
from re import findall
from typing import TextIO

cache = set()
# cache is necessary testing length of string to reduce searches
# checking length seemed to increase the search time as well
def main():
    replacements, molecule = parse("2015/day_19/input_test.txt")
    rev_replacements = [(to_str, from_str) for from_str, to_str in replacements]
    num_possibilities, _ = find_molecules(molecule, replacements)
    print(num_possibilities)
    print(search('e', molecule, replacements))
    

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
    return len(possibilities), possibilities

class Node:

    def __init__(self, val=None, parent=None):
        self._val = val
        self._parent = parent

    def get_val(self):
        return self._val

    def get_parent(self):
        return self._parent

def search(start, target, replacements):
    queue = deque([Node(start)])

    not_found = True
    while not_found:
        for neighbor in find_molecules(queue[0].get_val(), replacements)[1]:
            if len(target) < len(neighbor):
                continue
            if neighbor in cache:
                continue
            if neighbor == target:
                found_node = Node(neighbor, queue[0])
                not_found = False
                break
            queue.append(Node(neighbor, queue[0]))
            cache.add(neighbor)
        queue.popleft()

    steps = 0
    current_node = found_node
    while current_node.get_parent():
        current_node = current_node.get_parent()
        steps += 1

    return steps

if __name__ == "__main__":
    main()
