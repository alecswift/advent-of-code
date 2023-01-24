from copy import deepcopy
from itertools import combinations, permutations
from re import findall, split


def main():
    ingredients = parse("2015/day_15/input.txt")
    # print(ingredients)
    combos = []
    combo = [0,0,0,0]
    find_x_sums_of(4, 100, combos, combo)
    ingredients = [ingredient[:-1] for ingredient in ingredients]
    print(find_best_cookie(combos, ingredients))



def parse(input_file):
    in_file = open(input_file, "r", encoding="utf-8")
    with open(input_file, encoding="utf-8") as in_file:
        input_data = in_file.read()
    ingredients = [
        [int(num) for num in findall(r"-?\d+", line)] for line in split("\n", input_data)
    ]
    return ingredients

def find_x_sums_of(x, number, combos, combo):
    if x == 1:
        # print(number)
        combo[x - 1] = number
        combos.append(combo)
        # print("\n")
        return None
    for num in range(number - 1, 0, -1):
        # print(num)
        combo[x - 1] = num
        find_x_sums_of(x - 1, number - num, combos, deepcopy(combo))

def find_best_cookie(combos, ingredients):
    max_score = 0
    for combo in combos:
        combo_score = 1
        for column in range(len(ingredients[0])):
            curr_sum = 0
            for idx, tspoon in enumerate(combo):
                curr_sum += (tspoon * ingredients[idx][column])
            if curr_sum < 0:
                curr_sum = 0
            combo_score *= curr_sum
        max_score = max(max_score, combo_score)
    return max_score
    
            

            


if __name__ == "__main__":
    main()
