"""Puzzle explanation: https://adventofcode.com/2015/day/7"""

from collections import deque
from re import findall, split

def main():
    wires, instructions = parse("2015/day_7/input.txt")
    wires_1, instructions_1 = parse("2015/day_7/input_2.txt")
    print(emulate_circuit(wires, instructions))
    print(emulate_circuit(wires_1, instructions_1))

def parse(input_file):
    with open(input_file, encoding = "utf-8") as in_file:
        input_data = in_file.read()
    split_lines = split(r"\n", input_data)
    # Wire names mapped to their signal
    wires = {}
    # The instructions to build the circuit: operands, operator, result
    instructions = []
    for line in split_lines:
        wire_names = findall(r"[a-z]+", line)
        wires.update({name: None for name in wire_names})

        operator = findall(r"[A-Z]+", line)
        if not operator:
            source, dest = findall(r"\d+|[a-z]+", line)
            if source.isdigit():
                source = int(source)
            instructions.append(([source], "=", dest))
            continue
        operator, = operator
        if operator == "NOT":
            source, dest = wire_names
            instructions.append(([source], operator, dest))
        else:
            nums = findall(r"\d+", line)
            if nums:
                num, = nums
                source, dest = wire_names
                instructions.append(([source, int(num)], operator, dest))
            else:
                source_1, source_2, dest = wire_names
                instructions.append(([source_1, source_2], operator, dest))
    return wires, instructions

def emulate_circuit(wires, instructions):
    queue = deque(instructions)
    # rotate the queue of instructions until the circuit is complete
    while queue:
        sources, operator, dest = queue[0]
        nums = []
        for source in sources:
            if isinstance(source, int):
                nums.append(source)
            else:
                nums.append(wires[source])
        if None in nums:
            queue.rotate()
            continue
        wires[dest] = operation(operator, *nums)
        queue.popleft()
    return wires["a"]


def operation(operator, *nums):
    if len(nums) == 2:
        num_1, num_2 = nums
        match operator:
            case "AND":
                return num_1 & num_2
            case "OR":
                return num_1 | num_2
            case "LSHIFT":
                return num_1 << num_2
            case "RSHIFT":
                return num_1 >> num_2
    else:
        num, = nums
        if operator == "NOT":
            return ~num
        return num

if __name__ == "__main__":
    main()
