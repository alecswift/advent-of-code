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

def search(blue_print, max_item, cache, time_rem, robots, ores):
    """Depth first search to find the max geodes for each blueprint"""
    if time_rem == 0:
        return ores[3]
    key = tuple([time_rem, *robots, *ores])
    if key in cache:
        return cache[key]

    max_geodes = ores[3] + robots[3] * time_rem

    for robot, type_ores in enumerate(blue_print):
        if robot != 3 and robots[robot] >= max_item[robot]:
            continue
        wait = 0
        for item_amt, item_type in type_ores:
            if robots[item_type] == 0:
                break
            wait = max(wait, ceil((item_amt - ores[item_type]) / robots[item_type]))
        else:
            remtime = time_rem - wait - 1
            if remtime <= 0:
                continue
            robots_ = robots[:]
            ores_ = [x + y * (wait + 1) for x, y in zip(ores, robots)]
            for item_amt, item_type in type_ores:
                ores_[item_type] -= item_amt
            robots_[robot] += 1
            for i in range(3):
                ores_[i] = min(ores_[i], max_item[i] * remtime)
            max_geodes = max(
                max_geodes, search(blue_print, max_item, cache, remtime, robots_, ores_)
            )

    cache[key] = max_geodes
    return max_geodes

