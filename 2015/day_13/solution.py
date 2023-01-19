"""Puzzle explanation: https://adventofcode.com/2015/day/13"""

from itertools import permutations
import re


def main():
    people = parse("2015/day_13/input.txt")
    part_1 = find_optimal_arrangement_of(people)
    part_2 = find_optimal_arrangement_of(people, True)
    print(
        "The optimal seating arrangement without me",
        f"leads to a happiness level of: {part_1}"
    )
    print(
        "The optimal seating arrangement with me",
        f"leads to a happiness level of: {part_2}"
    )

def parse(input_file):
    in_file = open(input_file, "r", encoding="utf-8")
    with open(input_file, encoding="utf-8") as in_file:
        input_data = in_file.read()
    split_lines = input_data.split("\n")
    people = {}
    for line in split_lines:
        person, operator, change, neighbor = re.findall(
            r"^\S+|lose|gain|\d+|\S+(?=\.)", line
        )
        change = -int(change) if operator == "lose" else int(change)
        if person in people:
            people[person][neighbor] = change
        else:
            people[person] = {neighbor: change}
    return people

def find_optimal_arrangement_of(people, plus_one = False):
    if plus_one:
        arrangements = list(permutations(list(people), len(people)))
        arrangements = [[0] + list(arrangement) for arrangement in arrangements]
    else:
        first, *people_minus_1 = list(people)
        arrangements = list(permutations(people_minus_1, len(people_minus_1)))
        arrangements = [[first] + list(arrangement) for arrangement in arrangements]
    return max(find_happiness_of(arrangement, people) for arrangement in arrangements)

def find_happiness_of(arrangement, people):
    length = len(arrangement)
    happiness = 0
    for index, person in enumerate(arrangement):
        if not person:
            continue
        left = arrangement[(index - 1) % length]
        right = arrangement[(index + 1) % length]
        if not left:
            happiness += people[person][right]
        elif not right:
            happiness += people[person][left]
        else:
            happiness += (people[person][left] + people[person][right])
    return happiness

if __name__ == "__main__":
    main()
