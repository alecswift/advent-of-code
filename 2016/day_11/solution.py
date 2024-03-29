"""Puzzle Explanation: https://adventofcode.com/2016/day/11"""

from collections import deque
from itertools import combinations
from re import findall
from typing import TextIO
from copy import deepcopy


def main():
    floors = parse("2016/day_11/input.txt")
    target = sum(len(items) for items in floors.values())
    steps = bfs(floors, target)
    print(steps)
    part_2_floors = parse("2016/day_11/input_part_2.txt")
    part_2_target = sum(len(items) for items in part_2_floors.values())
    part_2_steps = bfs(part_2_floors, part_2_target)
    print(part_2_steps)


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
    curr_state = None
    queue = deque([root])
    while len(queue[0].floors[4]) != target:
        curr_node = queue[0]
        curr_state = build_state(curr_node.floors)
        curr_floor = curr_node.curr_floor
        if (curr_floor, curr_node.steps, curr_state) in seen:
            queue.popleft()
            continue
        if not curr_node.floors[curr_node.bottom_floor]:
            curr_node.bottom_floor += 1

        direction = 1
        if curr_floor != 4:
            steps = check_items(curr_node, direction, queue, target)

        direction = -1
        if curr_floor != curr_node.bottom_floor:
            steps = check_items(curr_node, direction, queue, target)
        if steps is not None:
            return steps
        seen.add((curr_floor, curr_node.steps, curr_state))
        queue.popleft()
    return queue[0].steps


def check_items(curr_node, dire, queue, target):
    curr_floor = curr_node.curr_floor
    curr_floors = curr_node.floors
    curr_floor_items = curr_floors[curr_floor]
    next_floor = curr_floor + dire
    next_floor_items = curr_floors[next_floor]
    double_move_up = False
    single_move_down = False
    for move in potential_moves(curr_floor_items, dire):
        if double_move_up and len(move) == 1 and dire == 1:
            break
        if single_move_down and len(move) == 2 and dire == -1:
            break
        new_curr_floor = curr_floor_items.difference(set(move))
        new_next_floor = set(next_floor_items)
        new_next_floor.update(set(move))
        move_is_possible = test_move(new_next_floor) and test_move(new_curr_floor)
        if move_is_possible:
            if len(move) == 1:
                single_move_down = True
            if len(move) == 2:
                double_move_up = True
            new_floors = deepcopy(curr_floors)
            new_floors[curr_floor] = new_curr_floor
            new_floors[next_floor] = new_next_floor
            new_node = Node(
                new_floors, next_floor, curr_node.steps + 1, curr_node.bottom_floor
            )
            if len(new_floors[4]) == target:
                return new_node.steps
            queue.append(new_node)


def potential_moves(curr_floor_items, dire):
    moves = []
    if dire == -1:
        moves.extend(combinations(curr_floor_items, 1))
    if 1 < len(curr_floor_items):
        moves.extend(combinations(curr_floor_items, 2))
    if dire == 1:
        moves.extend(combinations(curr_floor_items, 1))
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
