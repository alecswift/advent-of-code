"""Puzzle explanation: https://adventofcode.com/2015/day/5"""

from re import findall, search, split

def main():
    input_file = "2015/day_05/input.txt"
    with open(input_file, "r", encoding="utf-8") as in_file:
        input_data = in_file.read()

    strings = split(r"\n", input_data)
    num_1 = naughty_or_nice(strings)
    num_2 = naughty_or_nice(strings, False)
    print(f"For part one {num_1} strings are nice.")
    print(f"For part two {num_2} strings are nice.")

def naughty_or_nice(strings, part1 = True):
    """
    Search a list of strings and count the strings that match
    specified patterns
    """
    count = 0
    for string in strings:
        if part1:
            vowels = findall(r"[aeiou]", string)
            atleast_three_vowels = 3 <= len(vowels)
            repeat_char = search(r"(.)\1", string)
            disallowed = search(r"xy|ab|cd|pq", string)
            if atleast_three_vowels and repeat_char and not disallowed:
                count += 1
        else:
            there_are_pairs = False
            pairs = [string[num - 2: num] for num in range(2, len(string) + 1)]
            for index, pair in enumerate(pairs):
                if pair in pairs[index + 2:]:
                    there_are_pairs = True
            alternating_repeats = search(r"(.).\1", string)

            if there_are_pairs and alternating_repeats:
                count += 1
    return count

if __name__ == "__main__":
    main()
