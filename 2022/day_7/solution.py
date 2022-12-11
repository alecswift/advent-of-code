import re
from typing import TextIO

def parse(input_file: str):
    in_file: TextIO = open(input_file, 'r', encoding ='utf-8')
    with open(input_file, encoding = 'utf-8') as in_file:
        input_data = in_file.read()
    split_lines = input_data.split('\n')
    split_lines.pop(-1)
    parsed_data = [[]]
    count = 0
    for index, line in enumerate(split_lines):
        if line[0].isdigit():
            if not split_lines[index - 1][0].isdigit():
                parsed_data.append([])
                parsed_data[count].append(re.findall(r'\d+', line)[0])
                count += 1
            else:
                parsed_data[count - 1].append(re.findall(r'\d+', line)[0])
    return parsed_data

print(parse('2022/day_7/input.txt'))