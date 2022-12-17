from typing import TextIO
from collections import deque

class Node:

    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = [] # contains leaves and nodes
        

def split(input_file: str):
    """
    Returns ________________
    from a given input file
    """
    in_file: TextIO = open(input_file, "r", encoding="utf-8")
    with open(input_file, encoding="utf-8") as in_file:
        input_data: str = in_file.read()
    split_lines = input_data.split('\n\n')
    split_pairs = [line.split('\n') for line in split_lines]
    return split_pairs

def list_parser(lst_data):
    nodes = {}
    remove_brackets = lst_data[1:-1]
    root_node = Node(remove_brackets)
    nodes[remove_brackets] = root_node
    queue = deque([root_node])
    digit_is_10 = False
    inner_node = 0
    while queue:
        for index, item in enumerate(queue[0].data):
            if digit_is_10:
                digit_is_10 = False
            elif item.isdigit():
                if inner_node:
                    continue
                if (index != len(remove_brackets) -1) and (not remove_brackets[index + 1]):
                    digit_is_10 = True
                    queue[0].children.append(10)
                else:
                    queue[0].children.append(item)
            elif item == '[':
                if not inner_node:
                    start_index = index
                inner_node += 1
            elif item == ']':
                inner_node -= 1
                if not inner_node:
                    end_index = index
                    node_lst_data = queue[0].data[start_index + 1: end_index]
                    node = Node(node_lst_data)
                    queue[0].children.append(node)
                    nodes[node_lst_data] = node
                    queue.append(node)
        queue.popleft()
    return nodes


# print(list_parser('[1,[2,[3,[4,[5,6,0]]]],8,9]'))
for node_1 in list_parser('[[4,4],4,4,4]').values():
    print(node_1.children)

# add to queue when you hit opening bracket [ keep track of  exiting/entering with 0 +-1 for []