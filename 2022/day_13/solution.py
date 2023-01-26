"""
Find the decoder key and the sum of the indices of pairs of packets
that are in the correct order from the given list data
"""

from typing import TextIO
from collections import deque
from itertools import zip_longest
from numpy import prod


class Node:
    """Represents a node with initial data and children"""

    def __init__(self, data):
        self.data = data
        self.children = []


def split(input_file: str) -> list[list[str, str]]:
    """Split pairs of packets from a given input file"""
    with open(input_file, encoding="utf-8") as in_file:
        input_data: str = in_file.read()
    split_lines = input_data.split("\n\n")
    split_pairs = [line.split("\n") for line in split_lines]
    return split_pairs


def list_parser(lst_data):
    """
    Returns a tree representation of a list
    from a given string representation of a list
    """
    remove_brackets = lst_data[1:-1]
    root_node = Node(remove_brackets)
    node_number = 0
    node_queue = deque([root_node])
    digit_is_10 = False
    inner_node = 0
    while node_queue:
        for index, item in enumerate(node_queue[0].data):
            if digit_is_10:
                digit_is_10 = False
                continue
            if item.isdigit():
                if inner_node:
                    continue
                if (index != len(node_queue[0].data) - 1) and (
                    node_queue[0].data[index + 1] == "0"
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
                    node_queue.append(node)
        node_queue.popleft()
    return root_node


def compare_int(left, right):
    """
    Returns a value depending on the comparison of two integers
    """
    if left > right:
        return 0
    if left < right:
        return 1
    return 2


def compare_packet(root_1, root_2):
    """
    Compares to lists to see which one is the smallest. Returns
    True if the first given list is smaller and False otherwise
    """
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
            packet_queue.extendleft(
                list(zip_longest(left.children, right.children))[::-1]
            )


def compare_pairs(input_file):
    """
    From a given file with list data return the
    sum of indices of packets that are ordered correctly
    """
    indices = []
    split_packets = split(input_file)
    for index, pair in enumerate(split_packets):
        left, right = pair
        root_left = list_parser(left)
        root_right = list_parser(right)
        if compare_packet(root_left, root_right):
            indices.append(index + 1)
    return sum(indices)


def decoder_key(input_file):
    """Returns the product of the location of dividers from the given list data"""
    dividers = [list_parser("[[2]]"), list_parser("[[6]]")]
    packets = [
        list_parser(lst_data) for packets in split(input_file) for lst_data in packets
    ]
    weights = []
    for divider in dividers:
        weight = 1
        for packet in packets:
            if compare_packet(packet, divider):
                weight += 1
        weights.append(weight)
    weights[1] += 1
    return prod(weights)


print(compare_pairs("2022/day_13/input.txt"))
print(decoder_key("2022/day_13/input.txt"))
