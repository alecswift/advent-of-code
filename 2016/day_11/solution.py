from collections import deque
from re import findall
from typing import TextIO
from copy import deepcopy


def main():
    floors = parse("2016/day_11/input.txt")
    target = sum(len(items) for items in floors.values())
    steps = bfs(floors, target)
    print(steps)


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

    # represents each item as a complex number
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
    def __init__(self, floors, curr_floor, steps, bottom_floor):
        self.floors = floors
        self.curr_floor = curr_floor
        self.steps = steps
        self.bottom_floor = bottom_floor


def bfs(floors, target):
    """
    Breadth first search of paths to get all items
    on the fourth floor
    """
    curr_floor = 1
    root = Node(floors, 1, 0, 1)
    queue = deque([root])
    while len(queue[0].floors[4]) != target:
        curr_node = queue[0]
        if not curr_node.floors[curr_node.bottom_floor]:
            del curr_node.floors[curr_node.bottom_floor]
            curr_node.bottom_floor += 1
        direction = 1
        curr_floor = curr_node.curr_floor
        if curr_floor != 4:
            handle_moves(curr_node, direction, queue)
        direction = -1
        if curr_floor != curr_node.bottom_floor:
            handle_moves(curr_node, direction, queue)
        queue.popleft()
    return queue[0].steps


def handle_moves(curr_node, direction, queue):
    cache = {} # state = dict[int, set]: move = (direction, items)
    curr_floor = curr_node.curr_floor
    curr_floors = curr_node.floors
    curr_floor_items = set(curr_floors[curr_floor])
    # how to handle two item move?
    for item in curr_floor_items:
        next_floor = curr_floor + direction
        item_is_microchip = item.imag == 0
        if item_is_microchip:
            new_node = move_item(curr_floors, curr_node, next_floor, item)
            if new_node is not None:
                queue.append(new_node)
                new_floors = new_node.floors
                if direction != -1:
                    for item in set(new_floors[curr_floor]):
                        new_node = move_item(new_floors, curr_node, next_floor, item)
                        if new_node is not None:
                            queue.append(new_node)
            if direction == 1:
                if item + 1j in curr_floors[curr_floor]:
                    cp_floors = deepcopy(curr_floors)
                    cp_floors[curr_node.curr_floor].remove(item)
                    cp_floors[next_floor].add(item)
                    cp_floors[curr_node.curr_floor].remove(item + 1j)
                    cp_floors[next_floor].add(item + 1j)
                    new_node = Node(cp_floors, next_floor, curr_node.steps + 1, curr_node.bottom_floor)
                    queue.append(new_node)


def move_item(curr_floors, curr_node, next_floor, item):
    """Move item to another floor if possible"""
    if move_possible(curr_floors, next_floor, item):
        # handle single move
        cp_floors = deepcopy(curr_floors)
        cp_floors[curr_node.curr_floor].remove(item)
        cp_floors[next_floor].add(item)
        new_node = Node(cp_floors, next_floor, curr_node.steps + 1, curr_node.bottom_floor)
        return new_node
    return None


def move_possible(floors, next_floor, item):
    """Check if a moving an item is possible"""
    if next_floor not in floors:
        return False

    ele, gen_or_micro = item.real, item.imag
    next_floor_items = floors[next_floor]
    for item_2 in next_floor_items:
        gen_or_micro_2 = item_2.imag
        other_type_on_next_floor = gen_or_micro != gen_or_micro_2
        is_compatible_item = complex(ele, gen_or_micro_2) in next_floor_items
        if other_type_on_next_floor and not is_compatible_item:
            return False
    return True


if __name__ == "__main__":
    main()
