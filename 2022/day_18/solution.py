# split into combinations, go through each combination and check if it's the same but off by one, if it is count = 1
from itertools import combinations
from re import findall

def parse(input_file):
    in_file = open(input_file, 'r', encoding = 'utf-8')
    with open(input_file, encoding = 'utf-8') as in_file:
        input_data = in_file.read()
    split_lines = input_data.split('\n')
    coords = [findall(r'(\d+),(\d+),(\d+)', line)[0] for line in split_lines]
    return [tuple(map(int, coord)) for coord in coords]
