"""
Find the max geodes produced from a blueprint of the amount
of ore needed to build a robot that harvests that ore in 24 minutes
"""

from re import findall
from math import ceil


def parse(input_file):
    """
    Return a list of blueprints and a list of the max amount of
    resources needed for each blue print from the given input file
    """
    in_file = open(input_file, "r", encoding="utf-8")
    with open(input_file, encoding="utf-8") as in_file:
        input_data = in_file.read()
    blue_prints = []
    max_items = []
    numbers = [int(num) for num in findall(r"\d+", input_data)]
    num_of_bp = numbers[-7]
    length = len(numbers)
    partition = length // num_of_bp
    for num in range(num_of_bp):
        ores = numbers[(partition * num) + 1 : (num + 1) * partition]
        blue_prints.append(
            [
                [(ores[0], 0)],
                [(ores[1], 0)],
                [(ores[2], 0), (ores[3], 1)],
                [(ores[4], 0), (ores[5], 2)],
            ]
        )
        max_ore = max(ores[0], ores[1], ores[2], ores[4])
        max_clay = ores[3]
        max_obs = ores[5]
        max_items.append([max_ore, max_clay, max_obs])
    return blue_prints, max_items
