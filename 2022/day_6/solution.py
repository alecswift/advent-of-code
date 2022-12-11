"""
Find a marker of 4 distinct digits and 14 distinct digits
from a given input file that contains a string of characters
"""

from typing import TextIO

def parse(input_file: str) -> str:
    """
    Return a string of characters representing a data bufferstream
    from a given input file
    """
    in_file: TextIO = open(input_file, 'r', encoding = 'utf-8')
    with open(input_file, encoding = 'utf-8') as in_file:
        input_data: str = in_file.read()
    return input_data

def sub_routine(input_file: str) -> int:
    """
    return a marker location for 4 distinct characters from an input file
    """
    buffer: str = parse(input_file)
    for num in range(len(buffer) - 3):
        sequence: str = buffer[num: num + 4]
        if len(set(sequence)) == 4:
            marker_location: int = num + 4
            break
    return marker_location

def sub_routine_2(input_file: str) -> int:
    """
    return a marker location for 14 distinct characters from an input file
    """
    buffer: str = parse(input_file)
    for num in range(len(buffer) - 13):
        sequence: str = buffer[num: num + 14]
        if len(set(sequence)) == 14:
            marker_location: int = num + 14
            break
    return marker_location

print(sub_routine('2022/day_6/input.txt'))
print(sub_routine_2('2022/day_6/input.txt'))
