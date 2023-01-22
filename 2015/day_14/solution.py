"""Puzzle explanation: https://adventofcode.com/2015/day/14"""

from re import findall


def main():
    reindeers = parse("2015/day_14/input.txt")
    max_dist, high_score = race(reindeers, 2503)
    print(f"For part 1, the winning reindeer traveled {max_dist} km")
    print(f"For part 2, the winning reindeer scored {high_score} points")


def parse(input_file):
    in_file = open(input_file, "r", encoding="utf-8")
    with open(input_file, encoding="utf-8") as in_file:
        input_data = in_file.read()
    split_lines = input_data.split("\n")
    reindeers = [list(map(int, findall(r"\d+", line))) for line in split_lines]
    return reindeers


def race(reindeers, seconds):
    length = len(reindeers)
    distances = [0] * length
    scores = [0] * length
    for sec in range(1, seconds + 1):
        for index, reindeer in enumerate(reindeers):
            speed, time, rest = reindeer
            cycle_time = time + rest
            if sec % cycle_time in list(range(1, time + 1)):
                distances[index] += speed
        top_scores = find_top_score_positions(distances)
        for index in top_scores:
            scores[index] += 1
    return max(distances), max(scores)


def find_top_score_positions(distances):
    index = 1
    maxes = [0]
    while index < len(distances):
        if distances[maxes[0]] < distances[index]:
            maxes = []
            maxes.append(index)
        elif distances[maxes[0]] == distances[index]:
            maxes.append(index)
        index += 1
    return maxes


if __name__ == "__main__":
    main()
