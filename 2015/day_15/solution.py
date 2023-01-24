from copy import deepcopy
from re import findall, split


def main():
    ingredients = parse("2015/day_15/input.txt")
    combo = [0, 0, 0, 0]
    ingredients = [ingredient[:-1] for ingredient in ingredients]
    num_of_ingredients = len(ingredients)
    print(find_best_cookie(num_of_ingredients, 100, ingredients, combo))


def parse(input_file):
    in_file = open(input_file, "r", encoding="utf-8")
    with open(input_file, encoding="utf-8") as in_file:
        input_data = in_file.read()
    ingredients = [
        [int(num) for num in findall(r"-?\d+", line)]
        for line in split("\n", input_data)
    ]
    return ingredients


def find_best_cookie(num_of_ingredients, number, ingredients, combo):
    max_score = 0
    if num_of_ingredients == 1:
        combo[num_of_ingredients - 1] = number
        return calc_score(combo, ingredients)
    for num in range(number - 1, 0, -1):
        combo[num_of_ingredients - 1] = num
        max_score = max(
            max_score,
            find_best_cookie(
                num_of_ingredients - 1, number - num, ingredients, deepcopy(combo)
            ),
        )
    return max_score


def calc_score(combo, ingredients):
    combo_score = 1
    for column in range(len(ingredients)):
        curr_sum = 0
        for idx, tspoon in enumerate(combo):
            curr_sum += tspoon * ingredients[idx][column]
        curr_sum = max(curr_sum, 0)
        combo_score *= curr_sum
    return combo_score


if __name__ == "__main__":
    main()
