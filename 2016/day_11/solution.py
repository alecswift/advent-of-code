from collections import deque
from itertools import combinations, product
from re import findall
from typing import TextIO
from copy import deepcopy

# check items function does not work
# iterates through items that have already been added to nodes
# Consider changing to finding potential combinations of moves (all 1 or 2 combos)
# iterate through those, first check if it's a possible move
# check this by seeing if there is a microchip
# And comparing it to the floor we're moving to
# to see if there are any incompatible parts
# Check the directions again for conditions!
# then create the new node

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
    seen = set()
    curr_floor = 1
    root = Node(floors, 1, 0, 1)
    queue = deque([root])
    while len(queue[0].floors[4]) != target:
        curr_node = queue[0]
        curr_state = build_state(curr_node.floors)
        if (curr_floor, curr_node.steps, curr_state) in seen:
            queue.popleft()
            continue
        if not curr_node.floors[curr_node.bottom_floor]:
            curr_node.bottom_floor += 1
        direction = 1
        curr_floor = curr_node.curr_floor
        if curr_floor != 4:
            check_items(curr_node, direction, queue)

        direction = -1
        if curr_floor != curr_node.bottom_floor:
            check_items(curr_node, direction, queue)
        seen.add((curr_floor, curr_node.steps, curr_state))
        queue.popleft()
    return queue[0].steps


def check_items(curr_node, direction, queue):
    curr_floor = curr_node.curr_floor
    curr_floors = curr_node.floors
    curr_floor_items = curr_floors[curr_floor]
    next_floor = curr_floor + direction
    next_floor_items = curr_floors[next_floor]
    # how to handle two item move?
    for move in possible_moves(curr_floor_items):
        new_curr_floor = curr_floor_items.difference(set(move))
        new_next_floor = set(next_floor_items)
        new_next_floor.update(set(move))
        move_is_possible = test_move(new_next_floor) and test_move(new_curr_floor)
        if move_is_possible:
            new_floors = deepcopy(curr_floors)
            new_floors[curr_floor] = new_curr_floor
            new_floors[next_floor] = new_next_floor
            new_node = Node(new_floors, next_floor, curr_node.steps + 1, curr_node.bottom_floor)
            queue.append(new_node)

def possible_moves(curr_floor_items):
    moves = []
    moves.extend(combinations(curr_floor_items, 1))
    if 1 < len(curr_floor_items):
        moves.extend(combinations(curr_floor_items, 2))
    return moves

def test_move(floor_items):
    gens = [item for item in floor_items if item.imag == 1]
    if not gens:
        return True
    micros = [item for item in floor_items if item.imag == 0]
    if gens and micros:
        for micro in micros:
            ele = micro.real
            if complex(ele, 1) not in floor_items:
                return False
    return True


def build_state(curr_floors):
    state = []
    for floor, items in curr_floors.items():
        state_items = []
        for item in items:
            ele, gen_or_micro = item.real, item.imag
            pair_floor = find_floor_pair(curr_floors, ele, gen_or_micro)
            state_items.append((gen_or_micro, pair_floor))
        state.append((floor, tuple(state_items)))
    return tuple(state)

def find_floor_pair(curr_floors, ele, gen_or_micro):
    other_type = 1 if gen_or_micro == 0 else 1
    for floor, items in curr_floors.items():
        for item in items:
            if item.imag == other_type and item.real == ele:
                return floor


if __name__ == "__main__":
    main()
