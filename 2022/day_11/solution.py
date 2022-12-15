from typing import TextIO


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
        self.factor = factor
        self.monkey_1 = monkey_1
        self.monkey_2 = monkey_2

    def inspection(self, item):
        worry_level = what_operation(item, self.operator, self.constant)
        return worry_level

    def throw(self, item, monkey_dict):
        if item % self.factor == 0:
            pass
            # access dictionary of monkeys and throw to self.monkey_1
            # remove item from list, add item to other monkey's list at the end
        else:
            pass
            # access dictionary of monkeys and throw to self.monkey_1
            # remove item from list, add item to other monkey's list at the end


def parse(input_file: str):
    in_file: TextIO = open(input_file, "r", encoding="utf-8")
    with open(input_file, encoding="utf-8") as in_file:
        input_data: str = in_file.read()
