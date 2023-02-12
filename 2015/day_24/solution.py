from typing import TextIO


def main() -> None:
    weights = [11,10,9,8,7,5,4,3,2,1]
    target = sum(weights) // 3
    part_1 = dfs(weights, target, 0, (), [None, None])
    print(part_1)

def parse(input_file: str) -> list[int]:
    with open(input_file, encoding="utf-8") as in_file:
        in_file: TextIO
        weights: list[int] = [int(line) for line in in_file]
    return weights

def find_optimal_subset(props, container):
    min_product, min_packages = props
    if min_product is not None:
        min_packages, min_product = len(container), entanglement(container)
    else:
        min_product = entanglement(container)
        min_packages = len(container)
    props.clear()
    props.extend([min_product, min_packages])

subsets = set()

def dfs(weights, target, sum_weights, subset, props):
    if subset in subsets:
        return
    for weight in weights:
        min_product, min_packages = props
        if min_packages is not None:
            if min_packages < len(subset):
                return
            if min_product <= entanglement(subset):
                return
        if target < sum_weights:
            return
        if sum_weights == target:
            subsets.add(subset)
            find_optimal_subset(props, subset)
            return
        dfs(weights, target, sum_weights + weight, (*subset, weight), props)
    return props[0]

def entanglement(container: list[int]) -> int:
    product = 1
    for weight in container:
        product *= weight
    return product


if __name__ == "__main__":
    main()
