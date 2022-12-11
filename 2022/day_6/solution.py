from typing import TextIO

def parse(input_file: str) -> str:
    in_file: TextIO = open(input_file, 'r', encoding = 'utf-8')
    with open(input_file, encoding = 'utf-8') as in_file:
        input_data: str = in_file.read()
    return input_data

def sub_routine(input_file: str) -> int:
    buffer: str = parse(input_file)
    for num in range(len(buffer) - 3):
        sequence: str = buffer[num: num + 4]
        if len(set(sequence)) == 4:
            marker_location: int = num + 4
            break
    return marker_location