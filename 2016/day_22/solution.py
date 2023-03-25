from __future__ import annotations
from re import findall
from typing import TextIO

def main():
    nodes = parse("2016/day_22/input.txt")
    pairs = find_pairs(nodes)
    print(len(pairs))

def parse(input_file: str) -> dict[complex, Node]:
    in_file: TextIO
    with open(input_file, "r", encoding="utf-8") as in_file:
        input_data = in_file.read()
    nodes = {}
    for line in input_data.split("\n")[2:]:
        x_coord, y_coord, size, used, avail, use_perc = findall('\d+', line)
        pos = complex(int(x_coord), int(y_coord))
        nodes[pos] = Node(pos, int(size), int(used), int(avail), int(use_perc))
    return nodes

def find_pairs(nodes: dict[complex, Node]) -> int:
    pairs = set()
    for node_a in nodes.values():
        for node_b in nodes.values():
            if node_a.used == 0: 
                continue
            if node_a == node_b:
                continue
            if node_a.used < node_b.avail:
                pairs.add(frozenset([node_a, node_b]))
    return pairs



class Node:

    def __init__(self, pos, size, used, avail, use_perc):
        self.pos = pos
        self.size = size
        self.used = used
        self.avail = avail
        self.use_perc = use_perc

if __name__ == "__main__":
    main()