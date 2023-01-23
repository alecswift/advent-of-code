from itertools import combinations, permutations
from re import findall, split


def main():
    ingredients = parse("2015/day_15/input.txt")
    print(find_x_sums_of(4, 4))


def parse(input_file):
    in_file = open(input_file, "r", encoding="utf-8")
    with open(input_file, encoding="utf-8") as in_file:
        input_data = in_file.read()
    ingredients = [
        [int(num) for num in findall(r"-?\d+", line)] for line in split("\n", input_data)
    ]
    return ingredients

def find_x_sums_of(x, number):
    if x == 1:
        print(number)
        print("hello")
        return 1
    y = 0
    for num in range(number, -1, -1):
        if x == 4:
            pass
            # print("\n")
        print(num)
        y = y + find_x_sums_of(x - 1, number - num)
    return y



if __name__ == "__main__":
    main()
