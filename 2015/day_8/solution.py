from re import split, findall, sub

def parse(input_file):
    in_file = open(input_file, "r", encoding = "utf-8")
    with open(input_file, encoding = "utf-8") as in_file:
        input_data = in_file.read()
    split_lines = split(r"\n", input_data)
    split_lines = [line[1:-1] for line in split_lines]
    total_answer = 0
    for line in split_lines:
        length = len(line)
        line = sub(r"\\\"", " ", line)
        line = sub(r"\\\\", " ", line)
        line = sub(r"\\x[0-9a-f][0-9a-f]", " ", line)
        new_length = len(line)
        answer = (length + 2) - new_length
        total_answer += answer
    return total_answer


print(parse("2015/day_8/input.txt"))
