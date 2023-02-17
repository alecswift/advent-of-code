"""Puzzle explanation: https://adventofcode.com/2016/day/7"""

from typing import TextIO


def main():
    data = parse("2016/day_07/input.txt")
    count_tls, count_ssl = count_valid(data)
    print(f"{count_tls} IPs support TLS")
    print(f"{count_ssl} IPs support SSL")


def parse(input_file: str) -> list:
    in_file: TextIO
    with open(input_file, encoding="utf-8") as in_file:
        input_data = in_file.read()
    split_lines = input_data.split("\n")
    data = []
    for line in split_lines[:-1]:
        hypernets = []
        supernets = []
        is_hypernet = False
        hypernet = ""
        supernet = ""
        for char in line:
            if char == "[":
                supernets.append(supernet)
                supernet = ""
                is_hypernet = True
            elif char == "]":
                hypernets.append(hypernet)
                hypernet = ""
                is_hypernet = False
            elif is_hypernet:
                hypernet += char
            else:
                supernet += char
        supernets.append(supernet)
        data.append((supernets, hypernets))
    return data


def count_valid(data: list) -> tuple[int, int]:
    count_tls = 0
    count_ssl = 0
    for supernets, hypernets in data:
        sup_has_abba, _ = contains_abba(supernets, 4)
        hyp_has_abba, _ = contains_abba(hypernets, 4)
        if sup_has_abba and not hyp_has_abba:
            count_tls += 1

        _, sup_abas = contains_abba(supernets, 3)
        _, hyp_abas = contains_abba(hypernets, 3)
        sup_babs = set(sup_aba[1] + sup_aba[0] + sup_aba[1] for sup_aba in sup_abas)
        for hyp_aba in hyp_abas:
            if hyp_aba in sup_babs:
                count_ssl += 1
                break
    return count_tls, count_ssl


def contains_abba(sequences: list[str], sub_seq_length) -> tuple[bool, list[str]]:
    abbas = []
    for sequence in sequences:
        for idx in range(sub_seq_length, len(sequence) + 1):
            sub_seq = sequence[idx - sub_seq_length : idx]
            if is_abba(sub_seq):
                abbas.append(sub_seq)
    return (True, abbas) if abbas else (False, abbas)


def is_abba(sequence: str) -> bool:
    all_same_char: bool = True
    for idx in range(1, len(sequence)):
        if sequence[idx - 1] != sequence[idx]:
            all_same_char = False
    return sequence == sequence[::-1] and not all_same_char


if __name__ == "__main__":
    main()
