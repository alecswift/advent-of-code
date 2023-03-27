"""Puzzle explanation: https://adventofcode.com/2016/day/22"""

from __future__ import annotations
from collections import deque
from copy import deepcopy
from re import findall
from typing import TextIO

def main():
    nodes = parse("2016/day_22/input.txt")
    pairs = find_pairs(nodes)
    print(len(pairs))
    print(shortest_path())

def parse(input_file: str) -> dict[complex, Node]:
    in_file: TextIO
    with open(input_file, "r", encoding="utf-8") as in_file:
        input_data = in_file.read()
    nodes = {}
    for line in input_data.split("\n")[2:]:
        x_coord, y_coord, size, used, avail, use_perc = findall('\d+', line)
        pos = complex(int(x_coord), int(y_coord))
        nodes[pos] = Node(int(size), int(used), int(avail), int(use_perc))
    return nodes

def shortest_path():
    steps = 0
    start = (17,22) # one empty node
    mid = (0,13) # only path through y = 13
    steps += taxicab_distance(start, mid)
    end = (36, 0)
    steps += taxicab_distance(mid, end)
    steps += 1 # move goal one further
    steps += (36*5) # move goal one further than move empty space around goal 36 times
    return steps


def taxicab_distance(start, end):
    x_1, y_1 = start
    x_2, y_2 = end
    return abs(x_1 - x_2) + abs(y_1 - y_2)


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

    def __init__(self, size, used, avail, use_perc):
        self.size = size
        self.used = used
        self.avail = avail
        self.use_perc = use_perc
        self.can_receive = False

if __name__ == "__main__":
    main()