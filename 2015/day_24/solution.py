from typing import TextIO
from itertools import combinations


def main() -> None:
    weights = [11,10,9,8,7,5,4,3,2,1]
    target = sum(weights) // 3
    min_length = find_min_length(weights, target)
    part_1 = find_optimal(weights, min_length, target)
    print(part_1)

def parse(input_file: str) -> list[int]:
    with open(input_file, encoding="utf-8") as in_file:
        in_file: TextIO
        weights: list[int] = [int(line) for line in in_file]
    return weights

def find_min_length(weights, target):
    max_idx = len(weights) - 1
    stack = []
    sum_weights = 0
    pos = 0
    while sum_weights != target:
        current = weights[pos]
        if max_idx < pos:
            last_weight, last_pos = stack.pop()
            sum_weights -= last_weight
            pos = last_pos + 1
        if target < sum_weights:
            stack.pop()
            sum_weights -= current
            pos += 1
        else:
            stack.append((current, pos))
            sum_weights += current
            pos += 1
    return len(stack)

def find_optimal(weights, min_length, target):
    minimum = None
    for subset in combinations(weights, min_length):
        if sum(subset) == target:
            if minimum is not None and entanglement(subset) < minimum:
                minimum = entanglement(subset)
            else:
                minimum = entanglement(subset)
    return minimum

def entanglement(container: list[int]) -> int:
    product = 1
    for weight in container:
        product *= weight
    return product


if __name__ == "__main__":
    main()
