from re import split, sub

def main():
    solution_1, solution_2 = parse("2015/day_8/input.txt")
    print(f"{solution_1}\n{solution_2}")

def parse(input_file):
    in_file = open(input_file, "r", encoding = "utf-8")
    with open(input_file, encoding = "utf-8") as in_file:
        input_data = in_file.read()
    split_lines = split(r"\n", input_data)
    # remove quotes around the string to assist with parsing
    split_lines = [line[1:-1] for line in split_lines]
    solution_1 = 0
    solution_2 = 0
    for line in split_lines:
        # Two is added back on to length because of the removed quotes
        length = len(line) + 2
        remove_escapes = sub(r"\\\"", " ", line)
        remove_escapes = sub(r"\\\\", " ", remove_escapes)
        remove_escapes = sub(r"\\x[0-9a-f][0-9a-f]", " ", remove_escapes)
        difference_1 = length  - len(remove_escapes)
        solution_1 += difference_1
        
        encode_string = sub(r"\\\"", "1234", line)
        encode_string = sub(r"\\\\", "1234", encode_string)
        encode_string = sub(r"\\x[0-9a-f][0-9a-f]", "12345", encode_string)
        # 6 is added on to length for the escaped quotes: "\"string\""
        new_length = len(encode_string) + 6
        difference_2 = new_length - length
        solution_2 += difference_2
    return solution_1, solution_2

if __name__ == "__main__":
    main()
