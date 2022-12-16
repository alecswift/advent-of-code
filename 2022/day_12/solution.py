from typing import TextIO
from string import ascii_letters
from itertools import product

class Matrix:

    def __init__(self, rows):
        self.rows = rows
        self.columns = [[]]
        self.num_rows = len(rows)
        self.num_cols = len(rows[0])

    def set_columns(self, count = 0):
        for row in self.rows:
            self.columns[count].append(row[count])
        if count < len(self.rows) - 1:
            self.columns.append([])
            count += 1
            return self.set_columns(count)
        return self.columns

    def multiply_matrix(self, matrix_object):
        matrix_prod = [[] for _ in range(len(self.rows))]
        columns = matrix_object.set_columns()
        cart_product = list(product(self.rows, columns))
        for index, pair in enumerate(cart_product):
            row, column = pair
            new_num = 0
            row_index = index // self.num_rows
            for num_1, num_2 in zip(row, column):
                new_num += num_1 * num_2
            matrix_prod[row_index].append(new_num)
        return matrix_prod

def parse(input_file: str):
    in_file: TextIO = open(input_file, "r", encoding="utf-8")
    with open(input_file, encoding="utf-8") as in_file:
        input_data: str = in_file.read()
    split_lines = input_data.split('\n')
    split_chars = [list(line) for line in split_lines]
    return split_chars

def build_locations(input_file):
    input_data = parse(input_file)
    locations = {}
    vertex = 0
    for row_num, row in enumerate(input_data):
        for column_num, location in enumerate(row):
            locations[(row_num, column_num, vertex)] = ascii_letters.index(location)
            vertex += 1
    return locations

def start_end(locations):
    for location, value in locations.items():
        if value == 44:
            locations[location] = 0
            start = location
        if value == 30:
            # changed for test from 25 to 5
            locations[location] = 25
            end = location
    return start, end

def adjacent(pair_locations):
    location_1, location_2 = pair_locations
    row_1, column_1, _ = location_1
    row_2, column_2, _ = location_2
    if (row_1 + 1, column_1) == (row_2, column_2):
        return True
    if (row_1 - 1, column_1) == (row_2, column_2):
        return True
    if (row_1, column_1 + 1) == (row_2, column_2):
        return True
    if (row_1, column_1 - 1) == (row_2, column_2):
        return True
    return False


def adjacency_matrix(locations):
    matrix = [[0 for _ in range(len(locations))] for _ in range(len(locations))]
    cart_product = list(product(locations, locations))
    for pair in cart_product:
            location_1, location_2 = pair
            if adjacent(pair):
                if locations[location_1] >= (locations[location_2] - 1):
                    matrix[location_1[2]][location_2[2]] = 1
    return matrix
    # could be problems here
                
#print(build_locations('2022/day_12/input_test.txt'))
locations_1 = build_locations('2022/day_12/input_test.txt')
# print(start_end(locations_1))
print(start_end(locations_1))
adj_matrix = Matrix(adjacency_matrix(locations_1))
adj_matrix.rows
adj_matrix_1 = Matrix(adjacency_matrix(locations_1))
square = Matrix(adj_matrix.multiply_matrix(adj_matrix_1))
count = 2
while not square.rows[0][21]:
    square = Matrix(adj_matrix.multiply_matrix(square))
    count += 1
print(count)
# while not square.rows[0][8]:
    # square = Matrix(adj_matrix.multiply_matrix(square))
    # count += 1
# print(square.rows)

