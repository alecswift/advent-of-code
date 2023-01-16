"""Puzzle explanation: https://adventofcode.com/2015/day/10"""

from itertools import groupby


def main():
    sequence = "1113222113"
    part_1, part_2 = parse(sequence)
    print(part_1)
    print(part_2)


def parse(sequence):
    sequence = list(map(int, sequence))
    for num in range(1,51):
        new_sequence = []
        for number, sub_sequence in groupby(sequence):
            length = len(list(sub_sequence))
            new_sequence.extend([length, number])
        sequence = new_sequence
        if num == 40:
            part_1 = len(sequence)
    return part_1, len(sequence)


if __name__ == "__main__":
    main()
