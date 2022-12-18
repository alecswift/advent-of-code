from typing import TextIO
from collections import deque
from itertools import zip_longest


class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []  # contains leaves and nodes


def split(input_file: str) -> list[list[str, str]]:
    """
    Returns ________________
    from a given input file
    """
    in_file: TextIO = open(input_file, "r", encoding="utf-8")
    with open(input_file, encoding="utf-8") as in_file:
        input_data: str = in_file.read()
    split_lines = input_data.split("\n\n")
    split_pairs = [line.split("\n") for line in split_lines]
    return split_pairs


def list_parser(lst_data):
    nodes = {}
    remove_brackets = lst_data[1:-1]
    root_node = Node(remove_brackets)
    node_number = 0
    nodes[node_number] = root_node
    node_queue = deque([root_node])
    digit_is_10 = False
    inner_node = 0
    while node_queue:
        for index, item in enumerate(node_queue[0].data):
            if digit_is_10:
                digit_is_10 = False
            elif item.isdigit():
                if inner_node:
                    continue
                if (index != len(remove_brackets) - 1) and (
                    not remove_brackets[index + 1]
                ):
                    digit_is_10 = True
                    node_queue[0].children.append(10)
                else:
                    node_queue[0].children.append(int(item))
            elif item == "[":
                if not inner_node:
                    start_index = index
                inner_node += 1
            elif item == "]":
                inner_node -= 1
                if not inner_node:
                    end_index = index
                    node_lst_data = node_queue[0].data[start_index + 1 : end_index]
                    node = Node(node_lst_data)
                    node_queue[0].children.append(node)
                    node_number += 1
                    nodes[node_number] = node
                    node_queue.append(node)
        node_queue.popleft()
    return root_node

"""def tree_to_list(nodes, root_node):
    current_node = root_node
    for index, item in enumerate(current_node.children):
        if not isinstance(item, int):
            root_node.children[index] = item.children
            return tree_to_list(nodes, item)
    return nodes[0].children"""


def compare_int(left, right):
    if left > right:
        return 0
    if left < right:
        return 1
    return 2

def compare_packet(root_1, root_2):
    packet_queue = deque(zip_longest(root_1.children, root_2.children))
    while packet_queue:
        left, right = packet_queue[0]
        if (left is None) or (right is None):
            if left is None:
                return True
            if right is None:
                return False
        if isinstance(left, int) and isinstance(right, int):
            if not compare_int(left, right):
                return False
            if compare_int(left, right) == 1:
                return True
            if compare_int(left, right) == 2:
                packet_queue.popleft()
                continue
        elif isinstance(left, int) or isinstance(right, int):
            if isinstance(left, int):
                packet_queue.popleft()
                packet_queue.extendleft(list(zip_longest([left], right.children))[::-1])
            if isinstance(right, int):
                packet_queue.popleft()
                packet_queue.extendleft(list(zip_longest(left.children, [right]))[::-1])
        else:
            packet_queue.popleft()
            packet_queue.extendleft(list(zip_longest(left.children, right.children))[::-1])

def compare_packets(input_file):
    indices = []
    split_packets = split(input_file)
    for index, pair in enumerate(split_packets):
        left, right = pair
        root_left = list_parser(left)
        root_right = list_parser(right)
        if compare_packet(root_left, root_right):
            indices.append(index + 1)
    return sum(indices)


print(compare_packets('2022/day_13/input_test.txt'))
# first test list parser create lists then compare string to string
