"""Puzzle explanation: https://adventofcode.com/2015/day/15"""

from copy import deepcopy
from re import findall, split


def main():
    ingredients = parse("2015/day_15/input.txt")
    num_of_ingredients = len(ingredients)
    combo = [0] * len(ingredients)
    part_1 = find_best_cookie(num_of_ingredients, 100, ingredients, combo, True)
    part_2 = find_best_cookie(num_of_ingredients, 100, ingredients, combo, False)
    print(f"The best cookie scores {part_1} points")
    print(f"The best cookie with only 500 calories scores {part_2} points")


def parse(input_file):
    in_file = open(input_file, "r", encoding="utf-8")
    with open(input_file, encoding="utf-8") as in_file:
        input_data = in_file.read()
    ingredients = [
        [int(num) for num in findall(r"-?\d+", line)]
        for line in split("\n", input_data)
    ]
    return ingredients


def find_best_cookie(num_of_ingredients, number, ingredients, combo, part_1):
    max_score = 0
    if num_of_ingredients == 1:
        combo[num_of_ingredients - 1] = number
        return calc_score(combo, ingredients, part_1)
    for num in range(number - 1, 0, -1):
        combo[num_of_ingredients - 1] = num
        max_score = max(
            max_score,
            find_best_cookie(
                num_of_ingredients - 1,
                number - num,
                ingredients,
                deepcopy(combo),
                part_1,
            ),
        )
    return max_score


def calc_score(combo, ingredients, part_1):
    combo_score = 1
    for column in range(len(ingredients[0])):
        curr_sum = 0
        for idx, tspoon in enumerate(combo):
            curr_sum += tspoon * ingredients[idx][column]

        if column == len(ingredients[0]) - 1:
            cals = curr_sum
        else:
            curr_sum = max(curr_sum, 0)
            combo_score *= curr_sum
    return combo_score if cals == 500 or part_1 else 0


if __name__ == "__main__":
    main()
