"""Puzzle explanation: https://adventofcode.com/2015/day/17"""

from itertools import combinations
from typing import TextIO


def main():
    in_file: TextIO
    with open("2015/day_17/input.txt", encoding = "utf-8") as in_file:
        input_data: str = in_file.read()
    data: list[int] = [int(num) for num in input_data.split("\n")]
    combos, combos_min_containers = find_subsets_with_sum_of_150(data)
    print(combos, combos_min_containers)


def find_subsets_with_sum_of_150(data):
    combos = 0
    combos_min_containers = 0
    first_hit = False
    min_containers = -1
    # we know that there are no 3 combinations that add up to 150
    for num in range(4, len(data)):
        for combo in combinations(data, num):
            if sum(combo) == 150:
                combos += 1
                if not first_hit:
                    min_containers = num
                    first_hit = True
        if num == min_containers:
            combos_min_containers = combos
    return combos, combos_min_containers


if __name__ == "__main__":
    main()
