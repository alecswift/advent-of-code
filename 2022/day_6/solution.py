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

def sub_routine(input_file: str, num_digits: int) -> int:
    """
    return a marker location for 4 distinct characters from an input file
    """
    buffer: str = parse(input_file)
    for num in range(len(buffer) - (num_digits - 1)):
        sequence: str = buffer[num: num + num_digits]
        if len(set(sequence)) == num_digits:
            marker_location: int = num + num_digits
            break
    return marker_location

print(sub_routine('2022/day_6/input.txt', 4))
print(sub_routine('2022/day_6/input.txt', 14))
