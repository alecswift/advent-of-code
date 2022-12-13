from typing import TextIO

class TreeGrid:

    def __init__(self, data):
        self.rows = data
        self.columns = [[]]

    def set_columns(self, count = 0):
        for row in self.rows:
            self.columns[count].append(row[count])
        if count < len(self.rows) - 1:
            self.columns.append([])
            count += 1
            return self.set_columns(count)
        return None


        


def parse(input_file: str):
    in_file: TextIO = open(input_file, 'r', encoding = 'utf-8')
    with open(input_file, encoding = 'utf-8') as in_file:
        input_data: str = in_file.read()
    split_lines = input_data.split('\n')
    parsed_data = [list(map(int, list(line))) for line in split_lines]
    return parsed_data

# tree_grid = TreeGrid(parse('/home/alec/Desktop/code/advent_of_code/2022/day_8/input.txt'))
# print(tree_grid.rows)
# tree_grid.set_columns()
# print(tree_grid.columns)
