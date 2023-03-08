from collections import deque
from re import findall
from typing import TextIO
from copy import deepcopy


def main():
    floors = parse("2016/day_11/input.txt")
    target = sum(len(items) for items in floors.values())
    print(floors, target)

def parse(input_file):
    in_file: TextIO
    floors = {}
    with open(input_file, encoding="utf-8") as in_file:
        for idx, line in enumerate(in_file):
            data = findall(r"\w+ generator|[\w-]+ microchip", line)
            items = set()
            for val in data:
                if "generator" in val:
                    item = (val.split(" ")[0], 1)
                else:
                    item = (val.split("-")[0], 0)
                items.add(item)
            floors[idx + 1] = items

    # represent each item as a complex number 
    # real part = element, imaginary part = microchip (0) or generator (1)
    codes = {}
    count = 0
    for floor, items in floors.items():
        for item in set(items):
            ele, type_item = item
            if ele not in codes:
                codes[ele] = count
                floors[floor].remove(item)
                floors[floor].add(complex(count, type_item))
                count += 1
            else:
                code = codes[ele]
                floors[floor].remove(item)
                floors[floor].add(complex(code, type_item))
    return floors

class Node:

    def __init__(self, floors, steps):
        self.floors = floors
        self.steps = steps


def bfs(floors, target):
    curr_floor = 1
    root = Node(floors, 0)
    queue = deque([root])
    while True:
        direction = 1
        for item in floors[curr_floor]:
            if move_possible(floors, curr_floor + direction, item):
                pass

        direction = -1

def move_possible(floors, next_floor, item):
    if next_floor not in floors:
        return False

    ele, gen_or_micro = item
    next_floor_items = floors[next_floor]
    for item_2 in next_floor_items:
        _, gen_or_micro_2 = item_2
        other_type_on_next_floor = gen_or_micro != gen_or_micro_2
        is_compatible_item = complex(ele, gen_or_micro_2) in next_floor_items
        if other_type_on_next_floor and not is_compatible_item:
            return False
    return True



            
            

if __name__ == "__main__":
    main()