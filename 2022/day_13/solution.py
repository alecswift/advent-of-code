from typing import TextIO


def parse(input_file: str):
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

def build_items(items_data):
    level = 0
    items = {}
    check = False
    for index, item in enumerate(items_data):
        if check:
            check = False
            continue
        if item == '[':
            level += 1
            items[level] = []
        elif item == ']':
            level -= 1
        elif items_data[index: index + 2].isdigit():
            check = True
            items[level].append(int(items_data[index: index + 2]))
        elif item.isdigit():
            items[level].append(int(item))
        else:
            continue
    return items


def build_pairs(input_file):
    input_data = parse(input_file)
    pairs = []
    for item_1, item_2 in input_data:
        pass
        

print(parse('/home/alec/Desktop/code/advent_of_code/2022/day_13/input_test.txt'))
print(build_items('[1,[2,[3,[4,[5,6,0]]]],8,9]'))