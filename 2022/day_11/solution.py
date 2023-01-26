"""
Find the total monkey business from a given input file
"""

from typing import TextIO
from re import split, findall
from math import floor

def common_multiple(monkeys):
    """
    Return the least common multiple for the
    divisor test number of each monkey
    """
    result = 1
    for monkey in monkeys.values():
        result *= monkey.factor
    return result
        
def build_monkeys(input_file):
    """
    Create a dictionary of monkey objects with the given data
    """
    data = parse(input_file)
    monkeys = {}
    for monkey in data:
        monkeys[monkey[0]] = Monkey(monkey)
    return monkeys

def what_operation(num_1, operator, num_2):
    """Match strings to corresponding operators and numbers"""
    if num_2.isdigit():
        match operator:
            case "*":
                return (int(num_1) * int(num_2)) % 9699690
            case "+":
                return (int(num_1) + int(num_2)) % 9699690
    return (int(num_1) * int(num_1)) % 9699690


class Monkey:
    """Represents a monkey with a list items"""

    def __init__(self, data):
        number, starting_items, operation, test = data
        self.number = number
        self.items = starting_items
        operator, constant = operation
        self.operator = operator
        self.constant = constant
        factor, monkey_1, monkey_2 = test
        self.factor = int(factor)
        self.monkey_1 = int(monkey_1)
        self.monkey_2 = int(monkey_2)
        self.inspection_times = 0

    def inspect(self, item):
        """
        Return the new worry level of an item based on an operation
        """
        self.inspection_times += 1
        worry_level = what_operation(item, self.operator, self.constant)
        return worry_level

def parse(input_file: str):
    """Return parsed data from a given input file"""
    with open(input_file, encoding="utf-8") as in_file:
        input_data: str = in_file.read()
    initial_split = input_data.split('Monkey ')[1:]
    second_split = [split(r'\n\s+', monkey) for monkey in initial_split]
    split_monkeys = [monkey[:-1] for monkey in second_split]
    parsed_data = [[num] for num in range(len(split_monkeys))]
    for index, monkey in enumerate(split_monkeys):
        for inner_index, line in enumerate(monkey):
            if inner_index == 1:
                parsed_data[index].append(findall(r'\d+', line))
            elif inner_index == 2:
                parsed_data[index].append([line[21], line[23:]])
            elif inner_index >= 3:
                if inner_index == 3:
                    parsed_data[index].append([])
                parsed_data[index][3].append(findall(r'\d+', line)[0])
    parsed_data[-1][3].append('2')
    return parsed_data

def throwing(monkeys):
    """
    Modify the items of each monkey based on how they throw the items
    """
    for _ in range(10000):
        for monkey in monkeys.values():
            for item in list(monkey.items):
                new = monkey.inspect(int(item))
                if new % monkey.factor == 0:
                    monkey.items.pop(0)
                    monkeys[monkey.monkey_1].items.append(new)
                else:
                    monkey.items.pop(0)
                    monkeys[monkey.monkey_2].items.append(new)



monkey_dict = build_monkeys("/home/alec/Desktop/code/advent_of_code/2022/day_11/input.txt")
print(common_multiple(monkey_dict))
throwing(monkey_dict)
inspections = [monkey.inspection_times for monkey in monkey_dict.values()]
first = max(inspections)
inspections.remove(max(inspections))
second = max(inspections)
print(first * second)