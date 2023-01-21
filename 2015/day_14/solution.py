from re import findall

def main():
    reindeers = parse("2015/day_14/input.txt")
    print(max(race_1(reindeer, 2503) for reindeer in reindeers))
    print(race_2(reindeers, 2503))

def parse(input_file):
    in_file = open(input_file, "r", encoding="utf-8")
    with open(input_file, encoding="utf-8") as in_file:
        input_data = in_file.read()
    split_lines = input_data.split("\n")
    reindeers = [list(map(int, findall(r"\d+", line))) for line in split_lines]
    return reindeers

def race_1(reindeer, seconds):
    speed, time, rest = reindeer
    total_time, distance_per_cycle = time + rest, speed * time
    num_of_cycles, remaining_time = divmod(seconds, total_time)
    initial_distance = num_of_cycles * distance_per_cycle
    if remaining_time < time:
        return initial_distance + (speed * remaining_time)
    return initial_distance + distance_per_cycle

def race_2(reindeers, seconds):
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
    return max(scores)

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