from re import findall, split

def main():
    instructions, intervals = parse("day_6/input.txt")
    print(light_show(instructions, intervals))
    print(light_show_2(instructions, intervals))

def parse(input_file):
    in_file = open(input_file, "r", encoding = "utf-8")
    with open(input_file, encoding = "utf-8") as in_file:
        input_data = in_file.read()
    split_lines = split(r"\n", input_data)

    instructions = []
    intervals = []
    for line in split_lines:
        interval = [int(num) for num in findall(r"\d+", line)]
        intervals.append(interval)
        if "on" in line:
            instruction = 1
        elif "off" in line:
            instruction = 0
        else:
            instruction = -1
        instructions.append(instruction)
    return instructions, intervals

def light_show(instructions, intervals):
    lights_on = set()
    for index, interval in enumerate(intervals):
        x_1, y_1, x_2, y_2 = interval
        for x_coord in range(x_1, x_2 + 1):
            for y_coord in range(y_1, y_2 + 1):
                coord = complex(x_coord, y_coord)
                if instructions[index] == 1:
                    if coord not in lights_on:
                        lights_on.add(coord)
                elif instructions[index] == 0:
                    if coord in lights_on:
                        lights_on.remove(coord)
                else:
                    if coord in lights_on:
                        lights_on.remove(coord)
                    else:
                        lights_on.add(coord)
    return len(lights_on)

def light_show_2(instructions, intervals):
    lights_on = {}
    for index, interval in enumerate(intervals):
        x_1, y_1, x_2, y_2 = interval
        for x_coord in range(x_1, x_2 + 1):
            for y_coord in range(y_1, y_2 + 1):
                coord = complex(x_coord, y_coord)
                if instructions[index] == 1:
                    lights_on[coord] = lights_on.setdefault(coord, 0) + 1
                elif instructions[index] == 0:
                    if lights_on.get(coord):
                        lights_on[coord] -= 1
                else:
                    lights_on[coord] = lights_on.setdefault(coord, 0) + 2
    return sum(lights_on.values())




        
if __name__ == "__main__":
    main()

    